import asyncio
import signal
import sys
from count_timer import CountTimer
from blessings import Terminal

async def countdown(duration: float):

    global counter
    counter = CountTimer(duration=duration)
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

async def take_input():
    while True:
        loop = asyncio.get_event_loop()
        user_input = await loop.run_in_executor(None, input, "<SPACE> to pause/resume")
        if user_input == " ":
            counter.pause() if counter.paused else counter.resume()

async def main():
    duration = input("Enter countdown timer duration: ")
    global term
    term = Terminal()
    term.clear()
    tasks = [take_input(), countdown(float(duration))]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
sys.exit()
