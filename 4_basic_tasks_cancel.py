import asyncio


async def greet(timeout):
    await asyncio.sleep(timeout)
    return 'Hello world'


async def main():
    long_task = asyncio.create_task(greet(60))

    seconds = 0

    while not long_task.done():
        await asyncio.sleep(1)
        seconds += 1

        if seconds == 5:
            long_task.cancel()

        print('Time passed', seconds)

    try:
        await long_task
    except asyncio.CancelledError:
        print('The long task cancelled')



asyncio.run(main())
