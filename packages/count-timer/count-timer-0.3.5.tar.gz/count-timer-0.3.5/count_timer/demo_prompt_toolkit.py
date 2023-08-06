from time import sleep
from count_timer import CountTimer
from prompt_toolkit import prompt, print_formatted_text, ANSI
from prompt_toolkit.formatted_text import to_formatted_text

ANSI_RED = r"\x1b[31m"
ANSI_GREEN = r"\x1b[32m"
ANSI_YELLOW = r"\x1b[33m"
ANSI_BLUE = r"\x1b[34m"
ANSI_MAGENTA = r"\x1b[35m"
ANSI_NORMAL = r"\x1b[0m"

def main():
    duration = input("Enter countdown timer duration: ")
    counter = CountTimer(duration=float(duration))
    counter.start()

    print_formatted_text(ANSI(f"{ANSI_GREEN}Timer started.{ANSI_NORMAL}"))
    sleep(3)
    print_formatted_text(ANSI(f"{ANSI_YELLOW}Timer counting.{ANSI_NORMAL}"))
    sleep(3)
    print_formatted_text(ANSI(f"{ANSI_RED}Timer almost dead.{ANSI_NORMAL}"))
    sleep(3)
    print_formatted_text(ANSI(f"{ANSI_MAGENTA}Timer dead.{ANSI_NORMAL}"))

if __name__ == "__main__":
    main()
