import re
from typing import List, Dict

SECRET_PATTERNS = [
    (r"(?i)(api_key|apikey|secret|password|passwd|token)\s*=\s*['\"][^'\"]{6,}['\"]", "Credencial/Segredo hardcoded detectado"),
    (r"eval\s*\(", "Uso perigoso da função 'eval()' (risco de Code Injection)"),
    (r"exec\s*\(", "Uso perigoso da função 'exec()'"),
    (r"subprocess\..*shell\s*=\s*True", "Execução de subprocesso com 'shell=True' (risco de Command Injection)"),
]


def scan_security_risks(source_code: str) -> List[Dict[str, str]]:
    """Realiza varredura heurística por vulnerabilidades e segredos expostos."""
    findings: List[Dict[str, str]] = []
    lines = source_code.splitlines()

    for idx, line in enumerate(lines, start=1):
        for pattern, description in SECRET_PATTERNS:
            if re.search(pattern, line):
                findings.append(
                    {
                        "line": str(idx),
                        "description": description,
                        "snippet": line.strip()[:80],
                    }
                )
    return findings
