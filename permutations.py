def permutation(myStr, result = ''):
    l = []
    for i in range(len(myStr)):
        if len(myStr) > 1:
            l += permutation(myStr[:i] + myStr[i + 1:], result + myStr[i])
        else:
            return [result + myStr]
    return l
print(permutation('abcdef'))