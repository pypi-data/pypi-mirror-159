from __future__ import annotations

import jax

from .decorator_util import cached_property
from .tree_util import is_treeclass_leaf
from .tree_viz import tree_indent, tree_str


class treeBase:
    @property
    def tree_fields(self):
        static, dynamic = dict(), dict()

        for field in self.__dataclass_fields__.values():
            if field.name in self.__dict__:
                value = self.__dict__[field.name]
            else:
                # the user did not declare all variables defined in fields
                raise ValueError(f"field={field.name} is not declared.")

            excluded_by_type = isinstance(value, str)
            excluded_by_meta = ("static" in field.metadata) and field.metadata[
                "static"
            ] is True

            if excluded_by_type or excluded_by_meta:
                static[field.name] = value

            else:
                dynamic[field.name] = value

        return (dynamic, static)

    def tree_flatten(self):
        dynamic, static = self.tree_fields
        return (dynamic.values(), (dynamic.keys(), static))

    @classmethod
    def tree_unflatten(cls, aux, children):
        dynamic_vals, dynamic_keys = children, aux[0]

        static_keys, static_vals = aux[1].keys(), aux[1].values()
        attrs = dict(zip((*dynamic_keys, *static_keys), (*dynamic_vals, *static_vals)))

        newCls = cls.__new__(cls)
        for k, v in attrs.items():
            object.__setattr__(newCls, k, v)
        return newCls

    @cached_property
    def treeclass_leaves(self):
        return jax.tree_util.tree_leaves(self, is_treeclass_leaf)

    @cached_property
    def flatten_leaves(self):
        return jax.tree_util.tree_flatten(self)

    def __hash__(self):
        return hash(tuple(jax.tree_flatten(self)[0]))

    @cached_property
    def __treeclass_repr__(self):
        return tree_indent(self)

    @cached_property
    def __treeclass_str__(self):
        return tree_str(self)

    def __repr__(self):
        return self.__treeclass_repr__

    def __str__(self):
        return self.__treeclass_str__

    def asdict(self):
        return {**self.tree_fields[0], **self.tree_fields[1]}
