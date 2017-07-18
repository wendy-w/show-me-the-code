# 1.使用多个界定符分割字符串
line = 'asdf fjdk; adfe, fejk,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))  #使用; ,和空格分割字符串（\s:表示空格)
print(re.split(r'(;|,|\s)\s*', line)) #注意与上不同，这种方法保留了分隔符
field = re.split(r'(;|,|\s)\s*', line)
values = field[::2]
delimiters = field[1::2]
print(delimiters, values)
print(''.join(v+d for v,d in zip(values,delimiters)))


# 2.字符串开头或结尾匹配
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('spam'))

import os
filenames = os.listdir('.')
print(filenames)