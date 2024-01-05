import re
st='gurusiva14896@gmail.com'
data=re.findall('[a-zA-Z]+[a-zA-Z0-9]*\@gmail\.com',st)
print(data)
