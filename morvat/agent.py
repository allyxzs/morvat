from pathlib import Path
from typing import Dict, Any
from morvat.persona import get_morvat_commentary
from morvat.memory import EpisodicCrypt
from morvat.tools import perform_code_autopsy, scan_security_risks


class MorvatAgent:
    """Núcleo de decisão e diagnóstico do agente Morvat."""

    def __init__(self) -> None:
        self.memory = EpisodicCrypt()

    def audit_file(self, file_path: str) -> Dict[str, Any]:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"O arquivo '{file_path}' não existe neste plano astral.")

        source_code = path.read_text(encoding="utf-8")
        autopsy = perform_code_autopsy(source_code)
        security_findings = scan_security_risks(source_code)

        # Combina a entropia estrutural com o peso das falhas de segurança
        total_entropy = min(100, autopsy["entropy_score"] + (len(security_findings) * 25))
        total_issues_count = len(autopsy["issues"]) + len(security_findings)

        commentary = get_morvat_commentary(total_entropy)

        self.memory.record_audit(
            target_file=str(path),
            entropy_score=total_entropy,
            findings_count=total_issues_count,
            summary=commentary,
        )

        return {
            "target": str(path),
            "entropy_score": total_entropy,
            "commentary": commentary,
            "autopsy": autopsy,
            "security": security_findings,
        }

    def reply(self, user_message: str) -> str:
        """Simula a resposta conversacional do agente no modo interativo."""
        msg_lower = user_message.lower()
        if "legado" in msg_lower or "refatorar" in msg_lower:
            return (
                "🐦‍⬛ Morvat: Traga-me o arquivo e execute `python main.py audit <caminho>`. "
                "Vou dissecar cada função sem tipagem e expurgar as gambiarras."
            )
        if "segurança" in msg_lower or "senha" in msg_lower:
            return (
                "🐦‍⬛ Morvat: Credenciais no código-fonte são convites abertos para o desastre. "
                "Use variáveis de ambiente (.env) ou cofres de segredos imediatamente."
            )
        return (
            "🐦‍⬛ Morvat: Estou ouvindo das sombras. Posso auditar seus scripts Python, "
            "caçar vulnerabilidades ou revisar sua arquitetura. Qual é o nosso alvo hoje?"
        )
