def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield ''.join(list(map(str, lst[i:i + n])))