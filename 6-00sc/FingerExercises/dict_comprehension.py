def get_min(d):
    keys = list(d.keys())
    keys.sort()
    return [d[key] for key in keys]

d = { key: value for key, value in [("o", 1), ("t", 2), ("e", 3)] }
print(get_min(d))
