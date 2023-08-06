from jinja2 import Template
from .types import type_simplification


def get_macro_by_own(env, own):
    return env.templates.get(
        own.removeprefix('macro.'), {}
    ), own

def get_macro_by_type(env, name, type):
    for t in type_simplification(type):
        macro = self.templates.get(f'{t}.{name}', {})
        if macro:
            return macro, f'macro.{t}.{name}'
    return {}, own


def get_op_macro(env, tmp, parts):
    return {}
