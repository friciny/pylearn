import re

ss=re.match(r'^\d{3}[\s\-]+\d{3,8}','021 -3552345')
print(ss)

se=re.match(r'^(\d{3})[\s\-]+(\d{3,8})$','021 - 231242')
print(se.group(0))
print(se.group(1))
print(se.group(2))

#贪婪匹配&非贪婪匹配
sw=re.match(r'^(\d+)(0*)$','103000')
print(sw.group(1),sw.group(2))
sw=re.match(r'^(\d+?)(0*)$','103000')
print(sw.group(1),sw.group(2))
