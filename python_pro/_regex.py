import re  
st = 'the data is 04/01/2024'
data=re.findall('\d',st)
print(data)