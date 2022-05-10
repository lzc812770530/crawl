import aiohttp
import asyncio

# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, 'http://httpbin.org/headers')
#         print(html)





async def main():
    async with aiohttp.ClientSession() as session:
        params = {'key1':[1, 2], 'key2':2}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',}
        async with session.post('http://httpbin.org/post',params=params, headers=headers) as response:
            url = response.url
            print(url)
            html = await response.text()
            print(html)


















if __name__ == '__main__':
    asyncio.run(main())










