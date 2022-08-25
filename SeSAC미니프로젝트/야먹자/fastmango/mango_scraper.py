from bs4 import BeautifulSoup
import aiohttp
import asyncio
import time
from fake_useragent import UserAgent

BASE_URL = "https://www.mangoplate.com/search/"

async def fetch(session, url):
    async with session.get(url) as response:
        # time.sleep(1)
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        data = soup.find("ul", "list-restaurants")
        title = data.find("h2", 'title').text()
        place_url = data.find("a", "only-desktop_not").text()
        
async def main(keyword):
    ua = UserAgent(verify_ssl=False)
    userAgent = ua.random
    headers = {"User-Agent" : userAgent}
    urls = [f"{BASE_URL}{keyword}?keyword={keyword}&page={i}" for i in range(1, 5)]
    async with aiohttp.ClientSession(headers=headers) as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])
    
    
if __name__ == "__main__":
    asyncio.run(main('한림'))
    # keyword = '한림'
    # BASE_URL = "https://www.mangoplate.com/search/"
    # print(f"{BASE_URL}{keyword}?keyword={keyword}&page={1}")