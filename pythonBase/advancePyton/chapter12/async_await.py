# python在3.5之后为了语义更加明确，就引入async、await关键词用于定义原生协成


async def downloader(url):
    return "bobby"


async def downloader_url(url):
    html = await downloader(url)
    return html


if __name__ == '__main__':
    coro = downloader_url("http://www.imooc.com")
    # next(None)
    coro.send(None)

