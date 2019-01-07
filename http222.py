async def yaml_load(dir='', file=''):
    if dir:
        file = os.path.join(dir, file)
    async with aiofiles.open(file, 'r', encoding='utf-8', errors='ignore')
        data = await f.read()
    
    data = yaml.load(data)

    # 匹配函数调用形式的语法
    pattern_function = re.compile(r'^\${([A-Za-z_]+\w*\(.*\))}$')
    pattern_function2 = re.compile(r'^\${(.*)}$')
    # 匹配取默认值的语法
    pattern_function3 = re.compile(r'^\$\((.*)\)$')

    def my_iter(data):
        if isinstance(data, (list, tuple)):
            for index, _data in enumerate(data):
                data[index] = my_iter(_data) or _data
        elif isinstance(data, dict):
            for k, v in data.items():
                data[k] = my_iter(v) or v
        elif isinstance(data, (str, bytes)):
            m = pattern_function.match(data)
            if not m:
                m = pattern_function2.match(data)
            if m:
                return eval(m.group(1))
            if not m:
                m = pattern_function3.match(data)
            if m:
                K, k = m.group(1).split(":")
                return bxmat.default_values.get(K).get(k)
            return data
    my_iter(data)
    return BXMDict(data)


async def http(domain, *args, **kwargs):
    method, api = args
    arguments = kwargs.get("data") or kwargs.get("params") or kwargs.get("json") or {}
    kwargs.setdefault("headers", {}).update({'token': bxmat.token})

    url = ''.join([domain, api])

    async with ClientSession() as session:
        async with session.request(method, url, **kwargs) as response:
            res = await response_handle(response)
            return {
                'response': res,
                'url': url,
                'arguments': arguments
            }


async def one(case_dir='', case_name='', semaphore=None):
    async with semaphore:
        project_name = case_name.split(os.sep)[1]
        domain = bxmat.url.get(project_name)
        test_data = await yaml_load(dir=case_dir, file=case_name)