'''
deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
[1, 2, 3, 4, 5, 6, 7, 8]
>>> deep_flatten([[1, [2, 3]], 4, 5])
[1, 2, 3, 4, 5]

'''
def deep_flatten(nums):
    flat = []
    try:
        it = iter(nums)
        for item in it:
            if isinstance(item, str):
                flat.append(item)
            else:
                flat = flat + deep_flatten(item)
    except TypeError:
        flat.append(nums)
    return flat