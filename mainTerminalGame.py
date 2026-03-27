import os
from game import*


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def print_board(board: list[list[str]]) -> None:
    if not board:
        return

    cols = len(board[0])

    print()
    print("    " + " ".join(f"{c:2}" for c in range(cols)))
    print("   " + "---" * cols)

    for r, row in enumerate(board):
        line = [f"{r:2}|"]
        for value in row:
            line.append(f" {value}")
        print("".join(line))
    print()


def print_header(state: dict) -> None:
    print(f" DEMINEUR TERMINAL - {state['difficulty']} :")
    print(f"Mines restantes : {state['mines_left']}")
    print(f"Temps : {state['time']} sec")
    print("Commandes :")
    print("  ligne,colonne (exemple : 9,5) -> ouvrir une case")
    print("  m ligne,colonne (exemple : 9,5) -> marquer (F -> ? -> vide)")
    print("  r    -> recommencer")
    print("  q    -> quitter")


def parse_command(command: str):
    command = command.strip().lower()

    if command == "q":
        return "q", None, None

    if command == "r":
        return "r", None, None

    if command.startswith("m "):
        coords = command[2:].strip()
        if "," not in coords:
            return "", None, None

        try:
            row_str, col_str = coords.split(",")
            return "m", int(row_str), int(col_str)
        except ValueError:
            return "", None, None

    if "," in command:
        try:
            row_str, col_str = command.split(",")
            return "o", int(row_str), int(col_str)
        except ValueError:
            return "", None, None

    return "", None, None


def choose_difficulty(game: Game) -> None:
    while True:
        clear_screen()
        print("Choisis une difficulté :")
        print("1 - Débutant      (9x9, 10 mines)")
        print("2 - Intermédiaire (12x12, 20 mines)")
        print("3 - Expert        (15x15, 35 mines)")

        choice = input("Ton choix (1/2/3) : ").strip()

        if game.new_game(choice):
            return

        input("Choix invalide. Appuie sur Entrée pour continuer...")


def main() -> None:
    game = Game()
    choose_difficulty(game)

    while True:
        clear_screen()
        state = game.get_state()
        print_header(state)
        print_board(state["board"])

        if state["status"] == "LOST":
            cmd = input("Tu as perdu... Tape 'r' pour recommencer ou 'q' pour quitter : ").strip().lower()
            if cmd == "r":
                choose_difficulty(game)
                continue
            if cmd == "q":
                break
            continue

        if state["status"] == "WON":
            cmd = input("BRAVOOO, tu as gagné. Tape 'r' pour recommencer ou 'q' pour quitter : ").strip().lower()
            if cmd == "r":
                choose_difficulty(game)
                continue
            if cmd == "q":
                break
            continue

        command = input("> ")
        action, row, col = parse_command(command)

        if action == "q":
            break

        if action == "r":
            choose_difficulty(game)
            continue

        if action == "o" and row is not None and col is not None:
            result = game.reveal(row, col)
            if result == "INVALID":
                input("Coordonnées invalides. Appuie sur Entrée...")
            continue

        if action == "m" and row is not None and col is not None:
            result = game.mark(row, col)
            if result == "INVALID":
                input("Coordonnées invalides. Appuie sur Entrée...")
            continue

        input("Commande invalide. Exemple : 3,4 ou m 3,4")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nJeu interrompu.")