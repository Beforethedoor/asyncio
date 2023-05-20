import asyncio

import aiohttp


class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as response:
        html = await response.text()
        return f"{url}: {html[:15]}"


class ServerError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


async def server_returns_error():
    await asyncio.sleep(2)
    raise ServerError("Failed to get data")


async def main():
    urls = [
        "https://pramp.com",
        "https://youtube.com",
        "https://google.com",
    ]
    coros = [check(url) for url in urls]

    for coro in asyncio.as_completed(coros):
        result = await coro
        print(result)

    # results = await asyncio.gather(
    #     *coros,
    #     server_returns_error(),
    #     return_exceptions=True,
    # )
    # for result in results:
    #     print(result)


asyncio.run(main())
