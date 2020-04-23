def fibonacci(n):
    res = []
    if n < 0:
        return res
    if n == 0:
        res.append(0)
        return res
    if n == 1:
        res.extend(fibonacci(n-1))
        res.append(1)
        return res
    if n > 1:
        res.extend(fibonacci(n-1))
        res.append(res[n-1]+res[n-2])
        return res