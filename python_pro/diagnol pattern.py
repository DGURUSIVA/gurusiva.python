# 
    
# row = int(input('enter rows:-'))
# row = int(input('enter rows:-'))
# for i in range(1,row+1):
#     print('* '*i)

row = int(input('enter rows:-'))
for i in range(1,row+1):
    print('  '*(row-i) ,'* '*i)