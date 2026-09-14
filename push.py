import sys
import subprocess
from pathlib import Path
from datetime import datetime


def run_command(command, cwd):
    """Spustí příkaz v daném adresáři a zkontroluje návratový kód."""
    result = subprocess.run(command, cwd=cwd, shell=True)
    if result.returncode != 0:
        print(f"\n[CHYBA] Příkaz selhal s kódem {result.returncode}: {command}")
        sys.exit(result.returncode)


def main():
    repo_dir = Path(__file__).resolve().parent

    # Výchozí název commitu nebo volitelný argument z příkazové řádky
    if len(sys.argv) > 1:
        commit_message = " ".join(sys.argv[1:])
    else:
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
        commit_message = f"aktualizace kódu ({timestamp})"

    print("=" * 50)
    print("🚀 Zahajuji nahrávání na GitHub...")
    print(f"📁 Složka: {repo_dir}")
    print(f"💬 Commit message: \"{commit_message}\"")
    print("=" * 50)

    # 1. git add .
    print("\n[1/3] Přidávám změny do stage (git add .)...")
    run_command("git add .", cwd=repo_dir)

    # Kontrola, zda jsou nějaké změny k commitu
    status_check = subprocess.run(
        "git status --porcelain",
        cwd=repo_dir,
        shell=True,
        capture_output=True,
        text=True
    )

    if not status_check.stdout.strip():
        print("ℹ️ Žádné nové změny k commitu.")
    else:
        # 2. git commit -m "..."
        print(f"\n[2/3] Vytvářím commit (git commit -m \"{commit_message}\")...")
        run_command(f'git commit -m "{commit_message}"', cwd=repo_dir)

    # 3. git push origin main
    print("\n[3/3] Odesílám na GitHub (git push origin main)...")
    run_command("git push origin main", cwd=repo_dir)

    print("\n" + "=" * 50)
    print("✅ Hotovo! Kód byl úspěšně nahrán na GitHub.")
    print("=" * 50)


if __name__ == "__main__":
    main()
