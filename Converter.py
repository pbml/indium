import re
import pandas as pd
import os  
os.rename('input.htm','test.txt') 

fh = open('test.txt', 'r')
input_str = fh.read()
data = re.findall(r'(?i)<td.*?>([^<]+)</td.*?>', input_str)
fh.close()

f = open('output.txt', 'w')
x=0
length = len(data)
while x < length:
    s_no = data[x]
    tel_no = data[x+1]
    name=data[x+2]
    address=data[x+3]
    f.write(s_no+'\t'+tel_no+'\t'+name+'\t'+address+'\n')
    x=x+4

f.close()

df = pd.read_csv('output.txt',delimiter="\t")
df.to_csv('output.csv',encoding='utf-8', index=False)