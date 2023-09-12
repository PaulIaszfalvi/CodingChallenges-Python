def compress(chars):
    if not chars:
        return []
    
    char = chars[0]
    result = []
    count = 0

    for i, c in enumerate(chars):
        if i > 0 and chars[i-1] != c:
            result.append(char)
            result.append(str(count))
            count = 1
            char = c
        else:
            count += 1
    result.append(char)
    result.append(str(count))

    return ''.join(result)

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))