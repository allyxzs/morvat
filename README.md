# 🐦‍⬛ MORVAT — The Digital Necromancer & Legacy Code Auditor

> *"Onde você vê um sistema morto e dependências quebradas, eu vejo matéria-prima pronta para ressuscitar."*

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-7c3aed.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981.svg)](https://opensource.org/licenses/MIT)
[![Agent Architecture](https://img.shields.io/badge/Agent-Autonomous%20Auditor-f59e0b.svg)]()

**Morvat** é um Agente Autônomo de IA especializado em **Arqueologia de Software, Caça a Código Morto (Dead Code Hunting), Auditoria de Segurança e Refatoração de Sistemas Legados**.

Projetado com uma personalidade afiada, estética *Cyber-Gothic* e precisão cirúrgica, Morvat vasculha repositórios esquecidos, identifica vulnerabilidades ocultas, mapeia dívidas técnicas e propõe planos de "ressurreição" arquitetural.

---

## ✨ Identidade e Características do Agente

| Atributo | Especificação |
| :--- | :--- |
| **Nome / Codinome** | **MORVAT** (*Modular Override & Vulnerability Analysis Technician*) |
| **Arquétipo** | Necromante Digital / Arqueólogo de Sistemas |
| **Tom de Voz** | Analítico, direto, levemente sarcástico com gambiarras, mas extremamente leal à qualidade do código |
| **Especialidade Principal** | Refatoração de código legado, detecção de *code smells*, análise de entropia e blindagem de segurança |
| **Modo de Operação** | Autônomo (ReAct Loop: *Scan -> Diagnose -> Exorcise -> Resurrect*) |

---

## 🛠️ Capacidades & Ferramentas (Tools)

1. **`RepoAutopsy` (Autópsia de Repositório):** Analisa a árvore de arquivos, calcula a complexidade ciclomática estimada e detecta arquivos órfãos ou funções nunca invocadas.
2. **`DependencyExorcist` (Exorcista de Dependências):** Inspeciona pacotes desatualizados, bibliotecas abandonadas e potenciais brechas de segurança (CVEs).
3. **`NecroRefactor` (Ressurreição de Código):** Reescreve trechos legados aplicando padrões modernos (Clean Architecture, SOLID, Type Hints) mantendo a compatibilidade.
4. **`EpisodicCrypt` (Memória Persistente):** Armazena o histórico de auditorias em banco SQLite local para acompanhar a evolução (ou degradação) do projeto ao longo do tempo.

---

## 📂 Estrutura do Projeto

```text
morvat-agent/
├── morvat/
│   ├── __init__.py          # Metadados e versão do pacote
│   ├── config.py            # Configurações e variáveis de ambiente
│   ├── persona.py           # Definição de personalidade, prompts e frases de efeito
│   ├── memory.py            # Cripta de memória (SQLite) para histórico de sessões
│   ├── agent.py             # Core do Agente (Loop de raciocínio e execução)
│   └── tools/
│       ├── __init__.py
│       ├── code_autopsy.py  # Scanner estático de entropia e dívida técnica
│       └── security_scan.py # Detector de segredos expostos e más práticas
├── prompts/
│   └── system_prompt.md     # Prompt de sistema mestre do Morvat
├── examples/
│   └── sample_legacy.py     # Arquivo propositalmente caótico para testar o Morvat
├── tests/
│   └── test_morvat.py       # Testes unitários da suíte de diagnóstico
├── main.py                  # Interface de Linha de Comando (CLI) interativa com Rich
├── requirements.txt         # Dependências do projeto
├── .env.example             # Template de variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
└── LICENSE                  # Licença MIT
```

---

## 🚀 Instalação e Uso Rápido

### 1. Clone o repositório e instale as dependências

```bash
git clone https://github.com/seu-usuario/morvat-agent.git
cd morvat-agent
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure o ambiente

```bash
cp .env.example .env
# Edite o arquivo .env caso queira conectar uma chave real de LLM (OpenAI/Gemini)
# O Morvat também possui um modo Offline/Heurístico nativo que funciona sem API Key!
```

### 3. Execute o Morvat CLI

Para realizar uma autópsia completa no arquivo de exemplo legado:

```bash
python main.py audit examples/sample_legacy.py
```

Para iniciar o modo de consulta interativa no terminal:

```bash
python main.py chat
```

Para visualizar o histórico de auditorias salvas na Cripta de Memória:

```bash
python main.py history
```

---

## 🧪 Executando os Testes

```bash
pytest tests/
```

---

## 📜 Exemplo de Saída do Terminal

```text
╔══════════════════════════════════════════════════════════════════════╗
║ 🐦‍⬛ MORVAT v1.0.0 — PROTOCOLO DE AUTÓPSIA DIGITAL INICIADO            ║
╚══════════════════════════════════════════════════════════════════════╝
[ALVO]: examples/sample_legacy.py
[ÍNDICE DE ENTROPIA]: 78/100 (Estado Crítico - Putrefação Avançada)

🔍 DIAGNÓSTICO DO MORVAT:
"Encontrei credenciais hardcoded na linha 8 e um bloco try/except vazio na linha 24.
Quem escreveu isso não temia nem a produção nem o próprio destino."

⚡ PLANO DE RESSURREIÇÃO:
1. Extrair chaves sensíveis para variáveis de ambiente (.env).
2. Substituir captura genérica de exceções por logging estruturado.
3. Adicionar tipagem estática (Type Hints) nas funções de processamento.
```

---

## 🤝 Contribuindo

Pull requests são bem-vindos! Se você deseja adicionar novos rituais de análise estática ou expandir as ferramentas do **Morvat**, abra uma *issue* ou envie seu PR.
