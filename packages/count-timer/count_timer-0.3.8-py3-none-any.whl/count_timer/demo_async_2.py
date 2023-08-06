from count_timer import CountTimer
from blessed import Terminal
import asyncio

# A co-routine
async def add(x: int, y: int):
    return x + y

# Create a function to schedule co-routines on the event loop
# then print results
async def get_results():
    inputs = [(2,3), (4,5), (5,5), (7,2)]
    # Create a co-routine list
    cors = [add(x,y) for x,y in inputs]

    # Prints results of co-routines as they are ready
    # Beware of Non-deterministic ouput. The order can change based on
    # which co-routine finishes first
    for cor in asyncio.as_completed(cors):
        print(await cor)


asyncio.run(get_results())
