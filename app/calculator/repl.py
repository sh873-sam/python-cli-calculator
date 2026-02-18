from dataclasses import dataclass, field
from typing import List, Optional

from app.calculation.factory import CalculationFactory


HELP_TEXT = """Commands:
  help     Show this help message
  history  Show calculation history
  exit     Quit the program

Operations:
  add or +        subtract or -
  multiply or *   divide or /
"""


@dataclass
class Session:
    history: List[str] = field(default_factory=list)

    def add_history(self, record: str) -> None:
        self.history.append(record)


def parse_number(text: str) -> float:
    # EAFP: try conversion; fail cleanly
    try:
        return float(text)
    except ValueError as exc:
        raise ValueError(f"Invalid number: '{text}'. Please enter a numeric value.") from exc


def handle_command(command: str, session: Session) -> Optional[str]:
    cmd = command.strip().lower()
    if cmd == "help":
        return HELP_TEXT
    if cmd == "history":
        return "\n".join(session.history) if session.history else "No calculations yet."
    if cmd == "exit":
        return "exit"
    return None


def run_repl() -> None: # pragma: no cover
    session = Session()
    print("Welcome to the Calculator REPL! Type 'help' for commands.")

    while True:
        user_input = input("\nEnter an operation (or help/history/exit): ").strip()

        cmd_result = handle_command(user_input, session)
        if cmd_result == "exit":
            print("Goodbye!")
            break
        if cmd_result is not None:
            print(cmd_result)
            continue

        a_text = input("Enter the first number: ").strip()
        b_text = input("Enter the second number: ").strip()

        try:
            a = parse_number(a_text)
            b = parse_number(b_text)

            calc = CalculationFactory.create(user_input, a, b)
            result = calc.compute()

            record = f"{calc} = {result}"
            session.add_history(record)

            print(f"Result: {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
if __name__ == "__main__":  # pragma: no cover
    run_repl()
