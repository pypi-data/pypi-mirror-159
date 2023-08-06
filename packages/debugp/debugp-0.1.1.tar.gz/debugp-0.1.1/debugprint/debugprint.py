from typing import Optional

from rich.console import Console
import inspect
import linecache
from .ast2py import *

MISSING = object()

console = Console()
last_line_no: int = -1
same_line_call_cache: Optional[list[ast.Call]] = None
same_line_counter: int = 0


def prepare(line_no, file, caller) -> ast.Call:
    """Prepare same_line_call_cache and returns correct arguments"""
    global same_line_counter, same_line_call_cache, last_line_no
    if line_no == last_line_no:
        same_line_counter += 1
        return same_line_call_cache[same_line_counter]

    tree = get_correct_tree(file, line_no)
    same_line_counter = 0
    last_line_no = line_no

    if len(tree.body) != 1:
        console.log(f"[{PSEUDO}][WARNING] Multiple statements on one line (semicolon),"
                    f" incorrect output expected[/{PSEUDO}]")
    same_line_call_cache = get_line_nodes(tree.body[0].value, caller.f_globals | caller.f_locals)
    return same_line_call_cache[0]


def debug_print(*objects, print_file=PRINT_FILE):
    """
    Print the debug info of a line with expr on the left and result on the right

    :param objects: objects to debug
    :param print_file: print the file path
    :return: the same object back (tuple if multiple)
    """
    global same_line_counter
    caller = inspect.currentframe().f_back
    line_no = caller.f_lineno
    file = caller.f_globals["__file__"]
    if print_file:
        console.log(f"[{PSEUDO}]Debug info of[/{PSEUDO}] [{CONSTANT}]'{file}'[/{CONSTANT}][{PSEUDO}],"
                    f" line [/{PSEUDO}]{line_no} in [{CONSTANT}]'{caller.f_code.co_name}'[/{CONSTANT}]:")
    else:
        console.log(f"[{PSEUDO}]Debug info of line [/{PSEUDO}]{line_no} [{PSEUDO}]in[/{PSEUDO}]"
                    f" [{CONSTANT}]{caller.f_code.co_name}:")

    tree = prepare(line_no, file, caller)
    # check if starred is in the first layer, if so it means do dp to each element rather than return a whole

    tree_args = list(tree.args)
    args = []
    starred_index = []
    for i, arg in enumerate(tree_args):
        if isinstance(arg, ast.Starred):
            starred_index.append(i)
            args.extend(process_args(arg.value.elts))
    for index_to_pop in reversed(starred_index):
        tree_args.pop(index_to_pop)

    args.extend(process_args(tree_args))

    for arg, obj in zip(args, objects):
        console.print(f"\t{arg}: {obj}")

    return objects if len(objects) > 1 else objects[0]


def get_correct_tree(file, line_no) -> ast.AST:
    """
    Read a line first, if syntax error, read additional char one by one

    :param file: file path
    :param line_no: start line number
    :return: string of code that is syntactically correct
    """
    guess = linecache.getline(file, line_no).strip()
    try:
        return ast.parse(guess)
    except SyntaxError:  # not single line
        pass

    while True:
        line_no += 1
        for char in linecache.getline(file, line_no).strip():
            guess += char
        try:
            return ast.parse(guess)
        except SyntaxError:
            pass


def get_line_nodes(tree, caller_ns) -> list[ast.Call]:
    """
    Returns a list of nodes which every single element is call of dp,
    and follows order of operation.

    :param tree: AST tree
    :param caller_ns: caller namespace
    :return: list of ast.Call
    """
    dps = []
    nodes = reverse_tree(tree)
    for call in nodes:
        try:
            func_name = call.func.id
        except AttributeError:
            continue
        func = caller_ns.get(func_name, MISSING)
        if func is dp:
            dps.append(call)
    sorter = sort_by_recursion_level(caller_ns)
    dps = list(sorted(dps, key=lambda _tree: sorter(_tree)))
    return dps


def sort_by_recursion_level(caller_ns):
    """
    Sort print calls from left to right, inner to outer

    :param caller_ns: caller namespace
    :return: the actuall function used to sort
    """

    def inner(tree, level=0, budget=1) -> tuple:
        offset = float("-inf") if not isinstance(tree, ast.Call) else tree.col_offset
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.Call):
                try:
                    if caller_ns.get(node.func.id, MISSING) is dp and budget:
                        level += 1
                        budget -= 1
                except AttributeError:
                    continue
            level, offset = max([(level, offset), inner(node, level)])
        return level, offset

    return inner


def reverse_tree(tree) -> list[ast.Call]:
    """
    Returns a list of ast.Calls with the correct order of visiting

    :param tree: AST tree
    :return: list of nodes
    """
    node_with_depth = {tree: 0}

    def get_node_with_depth(_tree, depth=1):
        for node in ast.iter_child_nodes(_tree):
            node_with_depth[node] = depth
            get_node_with_depth(node, depth + 1)

    get_node_with_depth(tree)
    nodes = sorted(node_with_depth.keys(), key=lambda key: node_with_depth[key], reverse=True)
    nodes = filter(lambda node: isinstance(node, ast.Call), nodes)
    return list(nodes)


dp = debug_print

__all__ = ["dp"]
