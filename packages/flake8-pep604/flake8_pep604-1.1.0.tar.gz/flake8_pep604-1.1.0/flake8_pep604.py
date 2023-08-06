from __future__ import annotations

import ast
import sys

if sys.version_info >= (3, 8):  # pragma: >=3.8 cover
    import importlib.metadata as importlib_metadata
else:  # pragma: <3.8 cover
    import importlib_metadata

from typing import Any, Generator

_MODULE_NAME = "typing"
_ATTR_NAME = "Union"
_FULLNAME = f"{_MODULE_NAME}.{_ATTR_NAME}"

MSG = f"UNT001 use `|` in place of `{_FULLNAME}`. See PEP-604"


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        visitor = _Visitor()
        visitor.visit(self._tree)

        for line, col in visitor.union_imports:
            yield line, col, MSG, type(self)


class _Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.union_imports: list[tuple[int, int]] = []
        self.aliased_imports: set[str] = set()

    def visit_Import(self, node: ast.Import) -> None:
        for name in node.names:
            if name.name == _FULLNAME:
                self.union_imports.append((node.lineno, node.col_offset))
            elif name.name == _MODULE_NAME and name.asname:
                self.aliased_imports.add(name.asname)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module == _MODULE_NAME:
            for name in node.names:
                if name.name == _ATTR_NAME:
                    self.union_imports.append((node.lineno, node.col_offset))
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if (
            isinstance(node.value, ast.Name)
            and (node.value.id in self.aliased_imports or node.value.id == _MODULE_NAME)
            and node.attr == _ATTR_NAME
        ):
            self.union_imports.append((node.lineno, node.col_offset))
        self.generic_visit(node)
