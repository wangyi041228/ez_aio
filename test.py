from ez_aio import aio, header0
from time import perf_counter as perf
import timeit
from statistics import mean, stdev


def get_test():
    # 单次请求，返回response.text()
    # url = 'https://www.baidu.com'
    # result = aio.get(url, headers=header0)
    # print(result)

    # 单次请求，执行func(response.text())，返回该函数结果
    # url = 'https://www.baidu.com'
    # result = aio.get(url, func=print, headers=header0)

    # 同时请求，session上限默认99，session太多（几千）会崩溃
    urls = ['https://www.baidu.com'] * 100
    # urls = [f'https://api.bilibili.com/x/relation/followers?vmid={n+10698608}' for n in range(100)] # 会被叔叔封
    print(f'GET TEST\n{len(urls) = }')
    for limit in [10, 50, 100]:
        start = perf()
        results = aio.get(urls, li=limit, headers=header0)
        # results = aio.get(urls, li=limit, func=print, proxy=proxy0, headers=header0)
        print(f"{limit = }, time used = {perf() - start}s")
    print()


def post_test():
    urls = ['https://httpbin.org/post'] * 100
    data = [{'a': n} for n in range(100)]

    print(f'POST TEST\n{len(urls) = }')
    start = perf()
    results = [aio.post(urls, data=data, func=print, headers=header0)]
    print(f"time used = {perf() - start}s")
    print()


def speedtest():
    a = timeit.repeat("requests.get('https://www.baidu.com', headers=header0)",
                      setup='import requests\nfrom ez_aio import header0', repeat=10, number=1)
    b = timeit.repeat("aio.get(['https://www.baidu.com'], headers=header0)",
                      setup='from ez_aio import aio, header0',  repeat=10, number=1)
    for x, y in ((a, 'requests'), (b, 'aiohttp')):
        print(y)
        print(f'{mean(x):.3f} ± {stdev(x):.3f} s, (range) [{min(x):.3f}, {max(x):.3f}]')
        print()


if __name__ == '__main__':
    # get_test()
    # post_test()
    speedtest()
