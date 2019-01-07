import asyncio
import time
from aiohttp import ClientSession
from inspect import isfunction
import csv

url = 'http://115.28.108.130:5000/sub/'


now = lambda: time.time()
async def req_get(url, headers=None, params=None):
    async with ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            return await response.text()

async def req_post(url, headers=None, params=None, data=None, json=None):
    async with ClientSession() as session:
        async with session.post(url, 
            headers=headers, 
            params=params, 
            data=data, 
            json=json) as response:
            return await response.text()


async def load_data():
    with open("data.csv") as f:
        data = csv.reader(f)
    return data


async def test_add():
    url = 'http://115.28.108.130:5000/add/?a=2&b=3'
    resp = await req_get(url=url)
    assert resp == '5'


async def test_add_2():
    url = 'http://115.28.108.130:5000/add/?a=-2&b=3'
    resp = await req_get(url=url)
    print("111")
    assert resp == '1'




if __name__ == '__main__':
    import sys
    start = now()
    loop = asyncio.get_event_loop()
    tasks = []
    data = load_data()
    for api in data:
        tasks.append("")
    # tasks.append(asyncio.ensure_future(test_add()))
    # tasks.append(asyncio.ensure_future(test_add_2()))
    # testcases = [ key for key in globals().keys() if key.startswith("test") and isfunction(globals()[key])]
    # print(testcases)
    # print(getattr(__name__, 'test_add'))
    # print(globals())
    # __import__("__main__")
    # m = sys.modules["__main__"]
    # print(getattr(m, 'test_add'))
    # for case in testcases:
        # obj = getattr(m,case)
        # print(obj.__call__())
        # tasks.append(asyncio.ensure_future(getattr(m, case).__call__()))
    # print(type(globals()['test_add']))
    # tasks = [asyncio.ensure_future(req_post(url, headers={"User-Agent": "Chrome"}, json={"a":1, "b": 3})) for i in range(2)]
    loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     print('Task ret: ', task.result())
    print('TIME: ', now() - start)