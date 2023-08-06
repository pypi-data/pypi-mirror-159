import ast
from itertools import zip_longest

from .config import *

BIN_OP_MAP = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.MatMult: "@", ast.Div: "/", ast.Mod: "%",
              ast.Pow: "**", ast.LShift: "<<", ast.RShift: ">>", ast.BitOr: "|", ast.BitXor: "^",
              ast.BitAnd: "&", ast.FloorDiv: "//"}
UNARY_OP_MAP = {ast.Invert: "~", ast.Not: "not ", ast.USub: "-", ast.UAdd: "+"}
COMP_MAP = {ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">=",
            ast.Is: "is", ast.IsNot: "is not", ast.In: "in", ast.NotIn: "not in"}


def process_args(args, depth=0, calling=False) -> list[str]:
    """Entry Point of Every Thing"""
    representation = []
    for arg in args:
        representation.append(process_by_type(arg, depth, calling=calling))
    return representation


def process_arguments(tree, depth) -> str:
    """Process arguments for lambda expressions"""
    reversed_arg_repr = []
    i = 1
    for i, (arg, default) in enumerate(zip_longest(tree.args[::-1], tree.defaults[::-1], fillvalue=None), start=2):
        if default is None:
            reversed_arg_repr.append(f"[{ARGUMENT}]{arg.arg}[/{ARGUMENT}]")
        else:
            reversed_arg_repr.append(
                f"[{ARGUMENT}]{arg.arg}[/{ARGUMENT}][{PSEUDO}]=[/{PSEUDO}]"
                f"{process_by_type(default, depth)}"
            )
        if i == len(tree.args) + 1:
            break

    if poa := tree.posonlyargs:
        reversed_arg_repr.append("[{PSEUDO}]/[/{PSEUDO}]")
        if len(tree.defaults) > len(tree.args):
            for pos_only_arg, default in zip_longest(poa[::-1], tree.defaults[-i::-1], fillvalue=None):
                if default is None:
                    reversed_arg_repr.append(f"[{ARGUMENT}]{pos_only_arg.arg}[/{ARGUMENT}]")
                else:
                    reversed_arg_repr.append(
                        f"[{ARGUMENT}]{pos_only_arg.arg}[/{ARGUMENT}][{PSEUDO}]=[/{PSEUDO}]"
                        f"{process_by_type(default, depth)}"
                    )
        else:
            for pos_only_arg in poa[::-1]:
                reversed_arg_repr.append(f"[{ARGUMENT}]{pos_only_arg.arg}[/{ARGUMENT}]")

    representation = list(reversed(reversed_arg_repr))

    if tree.vararg is not None:
        representation.append(f"[{ARGUMENT}]{tree.vararg.arg}[/{ARGUMENT}]")
    elif tree.kwonlyargs:
        representation.append("[{PSEUDO}]*[/{PSEUDO}]")

    for kwarg, kwdef in zip(tree.kwonlyargs, tree.kw_defaults):
        if kwdef is None:
            representation.append(f"[{ARGUMENT}]{kwarg.arg}[/{ARGUMENT}]")
        else:
            representation.append(
                f"[{ARGUMENT}]{kwarg.arg}[/{ARGUMENT}][{PSEUDO}]=[/{PSEUDO}]"
                f"{process_by_type(kwdef, depth)}"
            )

    if tree.kwarg is not None:
        representation.append(f"[{ARGUMENT}]**{tree.kwarg.arg}[/{ARGUMENT}]")

    return "[{PUNCTUATION}], [/{PUNCTUATION}]".join(representation)


def process_attr(tree, depth, call=False) -> str:
    if call is False:
        return f"{process_by_type(tree.value, depth)}[{PUNCTUATION}].[/{PUNCTUATION}][white]{tree.attr}[/white]"
    return f"{process_by_type(tree.value, depth)}[{PUNCTUATION}].[/{PUNCTUATION}][{CONSTANT}]{tree.attr}[/{CONSTANT}]"


def process_await(tree, depth) -> str:
    return f"[{PSEUDO}]await[/{PSEUDO}] {process_by_type(tree.value, depth)}"


def process_bin_op(tree, depth) -> str:
    representation = [process_by_type(tree.left, depth),
                      f"[{PSEUDO}]{BIN_OP_MAP[type(tree.op)]}[/{PSEUDO}]",
                      process_by_type(tree.right, depth)]
    return " ".join(representation)


def process_built_ins(tree, left, right, depth) -> str:
    raw = process_tuple(tree, depth, True)
    return f"[{PUNCTUATION}]{left}[/{PUNCTUATION}]{raw}[{PUNCTUATION}]{right}[/{PUNCTUATION}]"


def get_func_name(tree, depth):
    if isinstance(tree, ast.Name):
        return tree.id
    elif isinstance(tree, ast.Attribute):
        return process_attr(tree, depth, True)


def process_call(call_tree, depth) -> str:
    func_name = get_func_name(call_tree.func, depth)
    if depth >= 3:
        return "..."
    representation = f"{func_name}[{PUNCTUATION}]([/{PUNCTUATION}]"
    args = process_args(call_tree.args, depth, calling=True)
    args.extend(process_kwargs(call_tree.keywords, depth))
    return f"{representation}{f'[{PUNCTUATION}], [/{PUNCTUATION}]'.join(args)}[{PUNCTUATION}])[/{PUNCTUATION}]"


def process_comp(tree, depth) -> str:
    representation = [f"[{PSEUDO}]for[/{PSEUDO}]", process_by_type(tree.target, depth, True),
                      f"[{PSEUDO}]in[/{PSEUDO}]", process_by_type(tree.iter, depth)]

    for condition in tree.ifs:
        representation.append("[{PSEUDO}]if[/{PSEUDO}]")
        representation.append(process_by_type(condition, depth))

    return " ".join(representation)


def process_compare(tree, depth) -> str:
    representation = [process_by_type(tree.left, depth)]

    for op, arg in zip(tree.ops, tree.comparators):
        representation.append(f"[{PSEUDO}]{COMP_MAP[type(op)]}[/{PSEUDO}]")
        representation.append(process_by_type(arg, depth))

    return " ".join(representation)


def process_dict(tree, depth) -> str:
    representation = []
    for k, v in zip(tree.keys, tree.values):
        representation.append(f"{process_by_type(k, depth)}[{PSEUDO}]:[/{PSEUDO}] {process_by_type(v, depth)}")
    return f"[{PUNCTUATION}]{{[/{PUNCTUATION}]" \
           f"{'[{PUNCTUATION}], [/{PUNCTUATION}]'.join(representation)}[{PUNCTUATION}]}}[/{PUNCTUATION}]"


def process_dict_comp(tree, depth) -> str:
    if depth >= 3:
        return "..."
    representation = [process_by_type(tree.key, depth), "[{PSEUDO}]: [/{PSEUDO}]", process_by_type(tree.value, depth)]
    for gen in tree.generators:
        representation.append(process_comp(gen, depth))

    return f"[{PUNCTUATION}]{{[/{PUNCTUATION}]{' '.join(representation)}[{PUNCTUATION}]}}[/{PUNCTUATION}]"


def process_formatted_value(tree, depth) -> str:
    _format = [process_by_type(tree.value, depth)]
    if tree.conversion != -1:
        _format.append(f"[{ESCAPE_CHAR}]!{chr(tree.conversion)}[/{ESCAPE_CHAR}]")
    if tree.format_spec is not None:
        _format.append(
            f"[{ESCAPE_CHAR}]:[/{ESCAPE_CHAR}][{STRING}]{process_f_str(tree.format_spec, depth, True)}[/{STRING}]")
    return f"[{F_STR_BRACE}]{{[/{F_STR_BRACE}]" \
           f"{''.join(_format)}" \
           f"[{F_STR_BRACE}]}}[/{F_STR_BRACE}]"


def process_f_str(tree, depth, is_formatting=False) -> str:
    representations = [process_by_type(_f, depth, f_str=True) for _f in tree.values]
    if is_formatting:
        return f'{"".join(representations)}'
    return f'[{STRING}]f\'[/{STRING}]{"".join(representations)}[{STRING}]\'[/{STRING}]'


def process_gen_exp(tree, depth, calling) -> str:
    if depth >= 3:
        return "..."
    representation = [process_by_type(tree.elt, depth)]
    for gen in tree.generators:
        representation.append(process_comp(gen, depth))

    if calling:
        return ' '.join(representation)
    else:
        return f"[{PUNCTUATION}]([/{PUNCTUATION}]{' '.join(representation)}[{PUNCTUATION}])[/{PUNCTUATION}]"


def process_kwargs(kwargs, depth) -> list[str]:
    representation = []
    for kw in kwargs:
        key = kw.arg
        if key is None:
            # dict unpacking
            representation.append(f"[{PSEUDO}]**[/{PSEUDO}]{process_dict(kw.value, depth)}")
            continue
        val = process_by_type(kw.value, depth)
        representation.append(f"{key}={val}")
    return representation


def process_lambda(tree, depth) -> str:
    representation = ["[{PSEUDO}]lambda[/{PSEUDO}]"]
    if not any([getattr(tree.args, field) for field in tree.args._fields]):
        representation.append(f"[{PSEUDO}]:[/{PSEUDO}] {process_by_type(tree.body, depth)}")
        return "".join(representation)

    representation.append(f"{process_arguments(tree.args, depth)}[{PSEUDO}]:[/{PSEUDO}]")
    representation.append(f"{process_by_type(tree.body, depth)}")

    return " ".join(representation)


def process_list_comp(tree, left, right, depth) -> str:
    if depth >= 3:
        return "..."
    representation = [process_by_type(tree.elt, depth)]
    for gen in tree.generators:
        representation.append(process_comp(gen, depth))
    return f"[{PUNCTUATION}]{left}[/{PUNCTUATION}]{' '.join(representation)}[{PUNCTUATION}]{right}[/{PUNCTUATION}]"


def process_slice(tree, depth) -> str:
    representation = [process_by_type(tree.lower, depth) if tree.lower is not None else "",
                      process_by_type(tree.upper, depth) if tree.upper is not None else "",
                      process_by_type(tree.step, depth) if tree.step is not None else ""]
    if tree.step is None:
        representation.pop(-1)
    return "[{PSEUDO}]:[/{PSEUDO}]".join(representation)


def process_starred(tree, depth) -> str:
    return f"[{PSEUDO}]*[/{PSEUDO}]{process_by_type(tree.value, depth)}"


def process_subscript(tree, depth) -> str:
    left = process_by_type(tree.value, depth)
    right = process_by_type(tree.slice, depth, unpack=True)
    return f"{left}[{PUNCTUATION}][[/{PUNCTUATION}]{right}[{PUNCTUATION}]][/{PUNCTUATION}]"


def process_ternary(tree, depth, nest_level=0) -> str:
    if nest_level >= 2:
        return "..."
    or_else = process_by_type(tree.orelse, depth) if not isinstance(tree.orelse, ast.IfExp) \
        else process_ternary(tree.orelse, depth, nest_level + 1)
    return f"{process_by_type(tree.body, depth)} [{PSEUDO}]if[/{PSEUDO}] {process_by_type(tree.test, depth)} " \
           f"[{PSEUDO}]else[/{PSEUDO}] {or_else}"


def process_tuple(tree, depth, unpack=False, nested=False) -> str:
    representation = []
    for sub_comp in tree.elts:
        if isinstance(sub_comp, ast.Tuple):
            representation.append(process_tuple(sub_comp, depth, unpack, True))
            continue
        representation.append(process_by_type(sub_comp, depth))
    ret = f"[{PUNCTUATION}], [/{PUNCTUATION}]".join(representation)
    if nested or not unpack:
        if len(representation) == 1:
            ret = f"[{PUNCTUATION}]([/{PUNCTUATION}]{ret}[{PUNCTUATION}],)[/{PUNCTUATION}]"
        else:
            ret = f"[{PUNCTUATION}]([/{PUNCTUATION}]{ret}[{PUNCTUATION}])[/{PUNCTUATION}]"
    return ret


def process_unary_op(tree, depth) -> str:
    return f"{UNARY_OP_MAP[type(tree.op)]}{process_by_type(tree.operand, depth)}"


def process_walrus(tree, depth) -> str:
    return f"{process_by_type(tree.target, depth)} [{PSEUDO}]:=[/{PSEUDO}] {process_by_type(tree.value, depth)}"


def process_yield_from(tree, depth) -> str:
    return f"[{PUNCTUATION}]([/{PUNCTUATION}][{PSEUDO}]yield from[/{PSEUDO}]" \
           f" {process_by_type(tree.value, depth)}[{PUNCTUATION}])[/{PUNCTUATION}]"


def format_str(_str):
    # match escape characters
    return _str.replace("'", f"[{ESCAPE_CHAR}]\\'[/{ESCAPE_CHAR}]") \
        .replace("\"", f"[{ESCAPE_CHAR}]\\\"[/{ESCAPE_CHAR}]") \
        .replace("\\", f"[{ESCAPE_CHAR}]\\\\[/{ESCAPE_CHAR}]") \
        .replace("\n", f"[{ESCAPE_CHAR}]\\n[/{ESCAPE_CHAR}]") \
        .replace("\r", f"[{ESCAPE_CHAR}]\\r[/{ESCAPE_CHAR}]") \
        .replace("\t", f"[{ESCAPE_CHAR}]\\t[/{ESCAPE_CHAR}]") \
        .replace("\b", f"[{ESCAPE_CHAR}]\\b[/{ESCAPE_CHAR}]") \
        .replace("\f", f"[{ESCAPE_CHAR}]\\t[/{ESCAPE_CHAR}]")


def process_by_type(tree, depth, unpack=False, calling=False, f_str=False):
    match type(tree):
        case ast.Attribute:
            return process_attr(tree, depth)
        case ast.Await:
            return process_await(tree, depth)
        case ast.BinOp:
            return process_bin_op(tree, depth)
        case ast.Call:
            return process_call(tree, depth + 1)
        case ast.Compare:
            return process_compare(tree, depth)
        case ast.Constant:
            return format_str(f"[{STRING}]{repr(tree.value)[1:-1]}[/{STRING}]") \
                if f_str else f"[{CONSTANT}]{tree.value!r}[/{CONSTANT}]"
        case ast.Dict:
            return process_dict(tree, depth)
        case ast.DictComp:
            return process_dict_comp(tree, depth)
        case ast.FormattedValue:
            return process_formatted_value(tree, depth)
        case ast.GeneratorExp:
            return process_gen_exp(tree, depth, calling)
        case ast.IfExp:
            return process_ternary(tree, depth)
        case ast.JoinedStr:
            return process_f_str(tree, depth)
        case ast.Lambda:
            return process_lambda(tree, depth)
        case ast.List:
            return process_built_ins(tree, "[", "]", depth)
        case ast.ListComp:
            return process_list_comp(tree, "[", "]", depth)
        case ast.Name:
            return f"[white]{tree.id!s}[/white]"
        case ast.NamedExpr:
            return process_walrus(tree, depth)
        case ast.Set:
            return process_built_ins(tree, "{", "}", depth)
        case ast.SetComp:
            return process_list_comp(tree, "{", "}", depth)
        case ast.Slice:
            return process_slice(tree, depth)
        case ast.Starred:
            return process_starred(tree, depth)
        case ast.Subscript:
            return process_subscript(tree, depth)
        case ast.Tuple:
            return process_tuple(tree, depth, unpack)
        case ast.UnaryOp:
            return process_unary_op(tree, depth)
        case ast.Yield:
            return f"[{PUNCTUATION}]([/{PUNCTUATION}][{PSEUDO}]yield[/{PSEUDO}][{PUNCTUATION}])[/{PUNCTUATION}]"
        case ast.YieldFrom:
            return process_yield_from(tree, depth)
        case _:
            print(astunparse.dump(tree))
            assert False, NotImplemented
