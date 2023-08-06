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


def check_spec(path, SPEC):
    try:
        mod = Module(filename=path)
    except CodeQueryException as e:
        return [f"{path}: -- módulo inválido --"]

    fails = []

    # trata nós de invocação
    FORBIDEN_CALLS = get_spec_property("forbiden-calls")
    REQUIRED_CALLS = get_spec_property("required-calls")
    fails.extend(check(mod.not_calls, FORBIDEN_CALLS, f"{path}: invoca"))
    fails.extend(check(mod.calls, REQUIRED_CALLS, f"{path}: não invoca"))

    # trata imports
    REQUIRED_IMPORTS = set(get_spec_property("required-imports"))
    imported_from = {e.split(".", 1)[0] for e in mod.imported}
    missing_imports = REQUIRED_IMPORTS - mod.imported - imported_from
    for imp in missing_imports:
        fails.append(f"{path}: não importa {imp}")

    if "allowed-imports" in SPEC:
        allowed_imports = set(get_spec_property("allowed-imports"))
        illegal_imports = mod.imported - allowed_imports - REQUIRED_IMPORTS
        for imp in illegal_imports:
            fails.append(f"{path}: importa {imp}")

    elif "forbiden-imports" in SPEC:
        FORBIDEN_IMPORTS = get_spec_property("forbiden-imports")
        fails.extend(check(mod.not_imports, FORBIDEN_IMPORTS, f"{path}: importa"))
        fails.extend(check(mod.not_imports_from, FORBIDEN_IMPORTS, f"{path}: importa de"))

    # trata todos os tipos de nós
    FORBIDEN_NODES = get_spec_property("forbiden-nodes")
    REQUIRED_NODES = get_spec_property("required-nodes")
    fails.extend(check(mod.not_uses, FORBIDEN_NODES, f"{path}: usa"))
    fails.extend(check(mod.uses, REQUIRED_NODES, f"{path}: não usa"))

    return fails


def check_spec_validity(spec):
    # confirmar que spec tem alguma regra! não pode ser vazio
    # nesse caso, devemos dar um warning (já que em uma situação
    # em que seja gerado programaticamente pode até fazer sentido)
    num_rules = 0
    num_rules += len(spec.get("forbiden-calls", []))
    num_rules += len(spec.get("allowed-calls", []))
    num_rules += len(spec.get("required-calls", []))
    num_rules += len(spec.get("forbiden-imports", []))
    num_rules += len(spec.get("allowed-imports", []))
    num_rules += len(spec.get("required-imports", []))
    num_rules += len(spec.get("forbiden-nodes", []))
    num_rules += len(spec.get("required-nodes", []))
    if num_rules == 0:
        print("p1-check: nenhuma regra na especificação", file=sys.stderr)


    # se usa allowed-imports, não deve ter forbiden-imports porque todos
    # são proibidos, em princípio, nesse caso
    if spec.get('allowed-imports') and spec.get('forbiden-imports'):
        assert False, "p1-check: allowed-imports e forbiden-imports são mutuamente exclusivos"

    return True


def main():
    global SPEC
    if sys.argv[0].endswith("p1"):
        sys.argv.pop(0)

    for opt in ["--spec", "-s"]:
        if opt in sys.argv:
            idx = sys.argv.index(opt)
            assert len(sys.argv) > idx + 1, "arquivo de especificação não indicado"
            path = sys.argv[idx + 1]
            sys.argv.pop(idx + 1)
            sys.argv.pop(idx)
            break
    else:
        candidate_paths = glob.glob("*.yaml")
        assert len(candidate_paths), "nenhum arquivo yaml de especificação encontrado"
        if len(candidate_paths) > 1:
            msg = "múltiplos arquivos yaml de especificação encontrados\n"
            msg += "use --spec <arq> para indicar qual arquivo usar"
            assert False, msg
        path = candidate_paths[0]

    assert Path(path).expanduser().exists(), f"{path} não encontrado"

    try:
        SPEC = yaml.load(open(path).read(), Loader=yaml.Loader) or {}
    except yaml.scanner.ScannerError as e:
        assert False, "arquivo de especificação mal formado"

    check_spec_validity(SPEC)

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

    assert paths, "p1-check: nenhum arquivo python identificado"

    assert not mode_tst or len(paths) == 1, "--tst não se aplica para mais de um arquivo"

    for p in paths:
        fails = check_spec(p, SPEC)
        mode_tst and print("D" if fails else ".")
        for fail in fails:
            print(fail)


if __name__ == '__main__':
    main()
