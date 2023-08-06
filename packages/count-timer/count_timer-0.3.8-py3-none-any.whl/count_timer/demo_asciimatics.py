from time import sleep
from count_timer import CountTimer
from asciimatics.screen import ManagedScreen


def main():
    duration = input("Enter countdown timer duration: ")
    counter = CountTimer(duration=float(duration))
    counter.start()

    with ManagedScreen as screen:
        screen.print_at(counter.remaining, 0, 0)
        while counter.remaining > 10:
            screen.print_at(counter.remaining, 0, 0)
            screen.refresh()
            sleep(0.1)
        while counter.remaining > 5:
            screen.print_at(counter.remaining, 0, 0)
            screen.refresh()
            sleep(0.1)
        while counter.remaining > 0:
            screen.print_at(counter.remaining, 0, 0)
            screen.refresh()
            sleep(0.1)
        screen.print_at("TIME'S UP!", 0, 0)

if __name__ == "__main__":
    main()
