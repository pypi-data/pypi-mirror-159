import asyncio
from pathlib import Path
from time import sleep
from count_timer import CountTimer
from austin_tui.view import View, ViewBuilder


class MinimalView(View):
    def on_quit(self, data=None):
        raise KeyboardInterrupt("quit signal")


def main():
    with open(Path.cwd() / "count_timer" / "minimal-view.xml") as view_stream:
        view = ViewBuilder.from_stream(view_stream)
        view.open()

    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        view.close()
        print("Bye!")


if __name__ == "__main__":
    main()
