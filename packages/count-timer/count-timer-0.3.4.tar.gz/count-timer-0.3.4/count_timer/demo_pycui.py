import py_cui as pycui
from count_timer import CountTimer
from blessings import Terminal


def main():

    term = Terminal()
    term.clear()

    root = pycui.PyCUI(7,9)
    label = root.add_label('Label Text', 0, 0)
    button = root.add_button('Button Text', 1, 2, column_span=2, command=my_function)    # root.add_label("CountTimer Demo", 0, term.height-1)
    root.start()

    duration = input("Enter countdown timer duration: ")
    counter = CountTimer(duration=float(duration))

    counter.start()
    while counter.remaining > 10:
        print(
            term.bold
            + term.green
            + term.move_x(0)
            + term.move_up
            + term.clear_eol
            + str(round(counter.remaining, 3))
        )

    while counter.remaining > 5:
        print(
            term.bold
            + term.yellow
            + term.move_x(0)
            + term.move_up
            + term.clear_eol
            + str(round(counter.remaining, 3))
        )

    while counter.remaining > 0:
        print(
            term.bold
            + term.red
            + term.move_x(0)
            + term.move_up
            + term.clear_eol
            + str(round(counter.remaining, 3))
        )

    print(
        term.bold
        + term.magenta
        + term.move_x(0)
        + term.move_up
        + term.clear_eol
        + "TIME'S UP!"
    )
    term.clear()
    print(term.normal)


if __name__ == "__main__":
    main()
