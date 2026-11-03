import ast
from typing import Dict, Any, List


def perform_code_autopsy(source_code: str) -> Dict[str, Any]:
    """
    Analisa a árvore sintática abstrata (AST) de um código Python
    para detectar code smells, falta de tipagem e blocos perigosos.
    """
    issues: List[str] = []
    entropy_points = 0

    try:
        tree = ast.parse(source_code)
    except SyntaxError as exc:
        return {
            "valid_syntax": False,
            "entropy_score": 100,
            "issues": [f"Erro fatal de sintaxe na linha {exc.lineno}: {exc.msg}"],
            "stats": {},
        }

    functions_count = 0
    untyped_functions = 0
    bare_excepts = 0
    global_statements = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions_count += 1
            if node.returns is None:
                untyped_functions += 1
                issues.append(
                    f"Função '{node.name}' (linha {node.lineno}) não possui anotação de tipo de retorno."
                )
                entropy_points += 8

            if len(node.body) > 25:
                issues.append(
                    f"Função '{node.name}' (linha {node.lineno}) é longa demais ({len(node.body)} instruções). Considere quebrar responsabilidades."
                )
                entropy_points += 15

        elif isinstance(node, ast.ExceptHandler):
            if node.type is None:
                bare_excepts += 1
                issues.append(
                    f"Bloco 'except:' genérico detectado na linha {node.lineno}. Isso silencia erros críticos."
                )
                entropy_points += 20

        elif isinstance(node, ast.Global):
            global_statements += 1
            issues.append(
                f"Uso de variável 'global' na linha {node.lineno}. Alto risco de efeitos colaterais."
            )
            entropy_points += 15

    lines_count = len(source_code.splitlines())
    entropy_score = min(100, entropy_points)

    return {
        "valid_syntax": True,
        "entropy_score": entropy_score,
        "issues": issues,
        "stats": {
            "lines": lines_count,
            "functions": functions_count,
            "untyped_functions": untyped_functions,
            "bare_excepts": bare_excepts,
            "globals": global_statements,
        },
    }
