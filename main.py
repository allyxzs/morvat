import sys
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from morvat.agent import MorvatAgent

app = typer.Typer(help="🐦‍⬛ MORVAT — Digital Necromancer & Legacy Code Auditor CLI")
console = Console()


@app.command()
def audit(file_path: str = typer.Argument(..., help="Caminho do arquivo Python para autópsia")):
    """Realiza uma autópsia completa de código e segurança em um arquivo."""
    agent = MorvatAgent()
    try:
        report = agent.audit_file(file_path)
    except FileNotFoundError as exc:
        console.print(f"[bold red]Erro:[/bold red] {exc}")
        raise typer.Exit(code=1)

    entropy = report["entropy_score"]
    color = "red" if entropy >= 50 else ("yellow" if entropy >= 25 else "green")

    console.print(
        Panel.fit(
            f"[bold magenta]🐦‍⬛ MORVAT v1.0.0 — RELATÓRIO DE AUTÓPSIA DIGITAL[/bold magenta]\n"
            f"[bold]Alvo:[/bold] {report['target']}\n"
            f"[bold]Índice de Entropia:[/bold] [{color}]{entropy}/100[/{color}]\n"
            f"[italic]"{report['commentary']}"[/italic]",
            border_style="magenta",
        )
    )

    if report["security"]:
        sec_table = Table(title="☣️ Vulnerabilidades de Segurança Detectadas", style="red")
        sec_table.add_column("Linha", justify="center", style="bold")
        sec_table.add_column("Descrição")
        sec_table.add_column("Trecho")
        for item in report["security"]:
            sec_table.add_row(item["line"], item["description"], item["snippet"])
        console.print(sec_table)

    if report["autopsy"]["issues"]:
        console.print("\n[bold yellow]🩸 Diagnóstico Estrutural (Code Smells):[/bold yellow]")
        for issue in report["autopsy"]["issues"]:
            console.print(f"  • {issue}")
    else:
        console.print("\n[bold green]✨ Nenhum problema estrutural grave encontrado![/bold green]")


@app.command()
def history():
    """Exibe o histórico de auditorias salvas na Cripta de Memória (SQLite)."""
    agent = MorvatAgent()
    records = agent.memory.get_recent_audits()
    if not records:
        console.print("[yellow]A cripta de memória ainda está vazia.[/yellow]")
        return

    table = Table(title="📜 Cripta de Memória — Histórico de Auditorias")
    table.add_column("ID", justify="right")
    table.add_column("Data/Hora")
    table.add_column("Arquivo")
    table.add_column("Entropia", justify="center")
    table.add_column("Achados", justify="center")
    for r in records:
        table.add_row(
            str(r["id"]),
            r["timestamp"],
            r["target_file"],
            f"{r['entropy_score']}/100",
            str(r["findings_count"]),
        )
    console.print(table)


@app.command()
def chat():
    """Inicia um terminal de conversa interativa com o Morvat."""
    agent = MorvatAgent()
    console.print(
        Panel(
            "[bold magenta]🐦‍⬛ Terminal Interativo MORVAT[/bold magenta]\n"
            "Digite sua pergunta técnica ou [bold]'sair'[/bold] para encerrar.",
            border_style="magenta",
        )
    )
    while True:
        try:
            user_input = console.input("[bold cyan]Você > [/bold cyan]")
            if user_input.strip().lower() in {"sair", "exit", "quit"}:
                console.print("[magenta]🐦‍⬛ Morvat retorna às sombras...[/magenta]")
                break
            response = agent.reply(user_input)
            console.print(f"[bold magenta]{response}[/bold magenta]\n")
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == "__main__":
    app()
