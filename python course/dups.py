X = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
Y = list(dict.fromkeys(X))
Z = sorted(Y)
print(Z)
