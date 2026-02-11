import os
import subprocess
import sys
from pathlib import Path


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def discover_scripts():
    src_dir = Path("src")
    return sorted(
        [
            f.name
            for f in src_dir.glob("*.py")
            if f.name != "utils.py" and not f.name.startswith("_")
        ]
    )


def show_menu(scripts):
    clear_screen()
    print("=== POML Runner ===\n")
    print("Escolha um script para executar:\n")

    for idx, script in enumerate(scripts, 1):
        print(f"  {idx}. {script}")

    print()


def get_user_choice(max_option):
    while True:
        try:
            choice = input("Digite o número (ou 'q' para sair): ").strip().lower()

            if choice == "q":
                return None

            try:
                num = int(choice)
                if 1 <= num <= max_option:
                    return num
                print(f"Opção inválida. Digite um número entre 1 e {max_option}.")
            except ValueError:
                print("Entrada inválida. Digite um número ou 'q' para sair.")
        except KeyboardInterrupt:
            print("\n")
            return None


def run_script(script_name):
    subprocess.run([sys.executable, f"src/{script_name}"])


def main():
    try:
        scripts = discover_scripts()
        if not scripts:
            print("Nenhum script encontrado em src/")
            return
        show_menu(scripts)
        choice = get_user_choice(len(scripts))
        if choice is None:
            return
        selected_script = scripts[choice - 1]
        print(f"\n▶ Executando {selected_script}...\n")
        run_script(selected_script)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
