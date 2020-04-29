import re

pattern = re.compile('it')
this_string = 'yess dude it me again, and i see you can do it'
a=pattern.search(this_string)
c=pattern.findall(this_string)
b=pattern.match(this_string)
print(a.group())
print(b)
print(c)