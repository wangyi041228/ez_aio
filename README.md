# ez_aio
Easiest way to make tons of get/post requests with aiohttp.  
You need DIY to get/post with different proxy/headers/cookies, or delete/patch/put request.  
## Singel GET
    url = 'https://www.baidu.com'
    result = aio.get(url)[0]  # return a list by default
## Singel GET and print
    url = 'https://www.baidu.com'
    aio.get(url, func=print)
## x100 GET
    urls = ['https://www.baidu.com'] * 100
    results = aio.get(urls)
## x100 POST
    urls = ['https://httpbin.org/post'] * 100
    data = [{'a': n} for n in range(100)]
    results = [aio.post(urls, data=data, func=print)]
## Singel GET speedtest
    # requests might raise errors
    a = timeit.repeat("requests.get('https://www.baidu.com', headers=header0)",
                      setup='import requests\nfrom ez_aio import header0', repeat=10, number=1)
    b = timeit.repeat("aio.get(['https://www.baidu.com'], headers=header0)",
                      setup='from ez_aio import aio, header0',  repeat=10, number=1)
    for x, y in ((a, 'requests'), (b, 'aiohttp')):
        print(y)
        print(f'{mean(x):.3f} ± {stdev(x):.3f} s, (range) [{min(x):.3f}, {max(x):.3f}]')
## def
    get(urls, binary=False, func=None, fdata=None, li=99, forced=True, ssl=False, 
        proxy=None, headers=None, cookies=None):
    post(urls, data=None, binary=False, func=None, fdata=None, li=99, forced=True,
         ssl=False, proxy=None, headers=None, cookies=None):
* urls: url or list of url
* data: post(*, data=data[i], *) Change to json=data[i] if you want.
* binary: result = response.text() if binary else response.read()
* func: return func(result, *) if func else return result
* fdata: func(result, fdata[i] if fdata else func(result)
* li: max of session, 99 be default
* forced: only return response.status in [200, 403] if forced
* ssl: ssl
* proxy: proxy
* headers: headers
* cookies: cookies
* return: func(result, *) if func else result
## More
* [Learn more about aiohttp](https://docs.aiohttp.org)
* [Simple test with some libs](https://github.com/wangyi041228/http_libs_test)