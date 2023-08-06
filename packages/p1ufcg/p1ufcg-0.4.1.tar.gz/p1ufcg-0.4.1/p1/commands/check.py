#!/bin/env python3
#
# Permite detectar se um conjunto de módulos Python atendem a
# especificações de design. As especificações consistem em duas
# categorias: REQUIRED e FORBIDEN. E o que pode ser requerido e
# proibido são tipos de nós da AST, calls invocados e módulos
# importados.
#
# Neste momento, a especificação é lida do arquivo
# chamado `design.yaml`.
import sys
import glob
import yaml
from pathlib import Path

from codequery import Module, CodeQueryException


def get_spec_property(prop):
    value = SPEC.get(prop, {})

    if type(value) is str:
        value = value.split()

    if type(value) is list:
        value = { v:v for v in value }

    return value


def check(condition, forbiden, fail_msg):
    fails = []
    for e in forbiden.keys():
        if not condition(e):
            fails.append(f"{fail_msg} {forbiden[e]}")

    return fails


def check_spec(path):
    try:
        mod = Module(filename=path)
    except CodeQueryException as e:
        return [f"{path}: -- módulo inválido --"]

    FORBIDEN_NODES = get_spec_property("forbiden-nodes")
    FORBIDEN_IMPORTS = get_spec_property("forbiden-imports")
    FORBIDEN_CALLS = get_spec_property("forbiden-calls")

    REQUIRED_NODES = get_spec_property("required-nodes")
    REQUIRED_IMPORTS = get_spec_property("required-imports")
    REQUIRED_CALLS = get_spec_property("required-calls")

    fails = []

    fails.extend(check(mod.uses_not, FORBIDEN_NODES, f"{path}: usa"))
    fails.extend(check(mod.imports_not, FORBIDEN_IMPORTS, f"{path}: importa"))
    fails.extend(check(mod.calls_not, FORBIDEN_CALLS, f"{path}: invoca"))

    fails.extend(check(mod.uses, REQUIRED_NODES, f"{path}: não usa"))
    fails.extend(check(mod.imports, REQUIRED_IMPORTS, f"{path}: não importa"))
    fails.extend(check(mod.calls, REQUIRED_CALLS, f"{path}: não invoca"))

    return fails


def assert_spec_is_valid(spec):
    return True


def main():
    global SPEC

    if "--spec" in sys.argv:
        idx = sys.argv.index("--spec") 
        path = sys.argv[idx + 1]
        sys.argv.pop(idx + 1)
        sys.argv.pop(idx)
    else:
        path = "design.yaml"

    if not Path(path).expanduser().exists():
        sys.exit(f"{path} não encontrado")

    SPEC = yaml.load(open(path).read(), Loader=yaml.Loader)
    assert_spec_is_valid(SPEC)

    mode_tst = False
    if '--tst' in sys.argv:
        idx = sys.argv.index("--tst") 
        sys.argv.pop(idx)
        mode_tst = True

    pattern = sys.argv[1] if len(sys.argv) > 1 else "*.py"
    if "*" in pattern or "." in pattern:
        paths = glob.glob(pattern)
    else:
        paths = glob.glob(f"*{pattern}*.py")

    if not paths:
        sys.exit("p1-check: nenhum arquivo identificado")

    if len(paths) > 1 and mode_tst:
        sys.exit("--tst não se aplica para mais de um arquivo")

    for p in paths:
        fails = check_spec(p)
        mode_tst and print("D" if fails else ".")
        for fail in fails:
            print(fail)


if __name__ == '__main__':
    main()
