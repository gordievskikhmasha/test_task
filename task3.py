def func(path, obj):
    keys = path.split('.')

    for key in keys:
        obj = obj[key]

    return obj

data = {
    'a': {
        'b': {
            'c': '+++'
        }
    }
}

print(func('a.b.c', data)) 