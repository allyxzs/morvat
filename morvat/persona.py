import random

QUIPS_CRITICAL = [
    "Quem escreveu esse código claramente tinha um pacto com o caos.",
    "Encontrei tanta dívida técnica aqui que o banco central acabou de ligar.",
    "Esse bloco try/except vazio está escondendo mais segredos que uma cripta medieval.",
    "Variáveis de uma única letra e credenciais hardcoded. Corajoso, porém trágico.",
]

QUIPS_CLEAN = [
    "Surpreendente. O código respira, tem tipagem e não tenta explodir a memória.",
    "Pouca necrose encontrada. Apenas alguns ajustes estéticos necessários.",
    "Uma arquitetura digna. Meus instrumentos cirúrgicos quase não tiveram trabalho.",
]


def get_morvat_commentary(entropy_score: int) -> str:
    """Retorna um comentário característico do Morvat baseado no nível de entropia."""
    if entropy_score >= 50:
        return random.choice(QUIPS_CRITICAL)
    return random.choice(QUIPS_CLEAN)
