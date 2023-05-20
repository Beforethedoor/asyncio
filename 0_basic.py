import asyncio


async def one():
    return 1


async def greet():
    await asyncio.sleep(2)
    return "Hello world"


# sync
async def smain():
    res1 = await one()
    res2 = await greet()
    print(res1)
    print(res2)


# async
async def amain():
    res1 = one()
    res2 = greet()
    print(await res1)
    print(await res2)


print("smain start")
asyncio.run(smain())

print("amain start")
asyncio.run(amain())
