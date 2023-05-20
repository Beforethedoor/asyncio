import asyncio


async def greet(timeout):
    await asyncio.sleep(timeout)
    return "Hello world"


async def main():
    res2 = asyncio.create_task(greet(2))
    res3 = asyncio.create_task(greet(3))
    res4 = asyncio.create_task(greet(20))
    res5 = asyncio.create_task(greet(3))
    res6 = asyncio.create_task(greet(2))

    print(await res2)
    print(await res3)
    print(await res4)
    print(await res5)
    print(await res6)


asyncio.run(main())
