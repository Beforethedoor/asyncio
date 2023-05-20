import asyncio


async def coro(message):
    print(message)
    await asyncio.sleep(1)
    print(message)  # dont print becouse main finish before


async def main():
    print("-- main beginning")
    asyncio.create_task(coro("text"))
    # print(asyncio.all_tasks())
    await asyncio.sleep(0.5)
    print("-- main done")


asyncio.run(main())
