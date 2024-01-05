import re
st = 'the data isJDEPD9619A'
data=re.findall('[A-Z]{5}\d{4}[A-Z]',st)
print(data)
