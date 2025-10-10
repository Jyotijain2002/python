'''
PIP: is a package manager for python package,or modules.

package: contains all the files you need for a module.
modules are python code libraries which can be included using import keyword
'''

import camelcase

# print(dir(camelcase))

c=camelcase.CamelCase()
txt="hi my name is jyoti jain"
print(c.hump(txt)) #op: Hi My Name is Jyoti Jain