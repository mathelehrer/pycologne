import libcst

# AST
print(libcst.parse_statement('a = 1 # comment'))

print(libcst.parse_statement('if True:\n pass'))

libcst.parse_statement('a+b')

# libcst wird genutzt, um Code automatisch umzuschreiben.

d = {'a': 1, 'b': 2, 'd': 4}
a = [v ** 2 for k in ['a', 'b', 'c', 'd'] if (v := d.get(k))]


# python wats new