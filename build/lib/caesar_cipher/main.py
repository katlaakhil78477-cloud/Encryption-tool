import base64
import string
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule

app = typer.Typer(help="Enterprise Caesar Cipher Toolkit", rich_markup_mode="rich")
console = Console()
ALPHABET = string.ascii_uppercase


def shift_char(ch: str, key: int) -> str:
    if ch.upper() in ALPHABET:
        idx = ALPHABET.index(ch.upper())
        out = ALPHABET[(idx + key) % 26]
        return out if ch.isupper() else out.lower()
    return ch


def encrypt_text(text: str, key: int) -> str:
    return "".join(shift_char(c, key) for c in text)


def decrypt_text(text: str, key: int) -> str:
    return "".join(shift_char(c, -key) for c in text)


def smart_pack(text: str, key: int) -> str:
    payload = f"CS|{key}|{encrypt_text(text, key)}"
    return base64.b64encode(payload.encode("utf-8")).decode("ascii")


def smart_unpack(text: str):
    try:
        raw = base64.b64decode(text).decode("utf-8")
        if raw.startswith("CS|"):
            _, key_str, cipher = raw.split("|", 2)
            key = int(key_str)
            return key, decrypt_text(cipher, key)
    except Exception:
        return None
    return None


def banner(title: str) -> None:
    console.print(Rule(f"[bold cyan]{title}[/bold cyan]"))


@app.command()
def encrypt(
    text: str,
    key: int = typer.Option(..., help="Encryption key"),
    smart: bool = typer.Option(False, help="Guaranteed recovery mode"),
):
    banner("ENCRYPTION RESULT")
    result = smart_pack(text, key) if smart else encrypt_text(text, key)

    table = Table(show_header=False, expand=False)
    table.add_row("[bold green]Mode[/bold green]", "SMART GUARANTEED" if smart else "STANDARD")
    table.add_row("[bold yellow]Key[/bold yellow]", str(key))
    table.add_row("[bold magenta]Output[/bold magenta]", result)

    console.print(Panel(table, border_style="bright_blue", title="Caesar Cipher Toolkit"))


@app.command()
def decrypt(
    text: str,
    key: int = typer.Option(..., help="Decryption key"),
):
    banner("DECRYPTION RESULT")
    smart = smart_unpack(text)
    mode = "SMART AUTO-DETECTED" if smart else "STANDARD"
    result = smart[1] if smart else decrypt_text(text, key)

    table = Table(show_header=False, expand=False)
    table.add_row("[bold green]Mode[/bold green]", mode)
    table.add_row("[bold yellow]Recovered Text[/bold yellow]", result)

    console.print(Panel(table, border_style="green", title="Recovered Plaintext"))


@app.command()
def crack(text: str):
    banner("CRACK ANALYSIS")
    smart = smart_unpack(text)

    if smart:
        key, plaintext = smart
        table = Table(title="Guaranteed Smart Recovery", header_style="bold cyan")
        table.add_column("Status")
        table.add_column("Key")
        table.add_column("Recovered Text")
        table.add_row("SUCCESS", str(key), plaintext)
        console.print(table)
        return

    table = Table(title="Top Crack Candidates", header_style="bold cyan")
    table.add_column("Rank")
    table.add_column("Key")
    table.add_column("Candidate")

    common_words = ["THE", "AND", "IS", "THIS", "HELLO", "TEST", "OF", "TO", "IN", "A"]
    scored = []

    for key in range(26):
        candidate = decrypt_text(text, key)
        score = sum(10 for w in common_words if w in candidate.upper())
        score += sum(1 for c in candidate.upper() if c in "AEIOU")
        scored.append((score, key, candidate))

    scored.sort(reverse=True)

    for rank, (_, key, candidate) in enumerate(scored[:10], start=1):
        table.add_row(str(rank), str(key), candidate)

    console.print(table)
