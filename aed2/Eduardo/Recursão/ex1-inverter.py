def inverterString(string, pos = 0):
    if pos >= len(string):
        return ''
    else:
        return inverterString(string, pos + 1) + string[pos]
    
print(inverterString('abcd'))

'''
return ''
return inverterString('abcd', 4) + d = '' + d = d
return inverterString('abcd', 3) + c = d + c = dc
return inverterString('abcd', 2) + b = db + b = dcb
return inverterString('abcd', 1) + a = dcb + a = dcba
'''