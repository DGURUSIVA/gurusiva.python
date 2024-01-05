password =input('enter a number')
validate ={'upper':False','lower':False ,'number':False ,'char':False }
if len(password)>=8   
       for char in password:
     if 'A'<=char <= 'z':
        validate['upper']=True
     elif 'a' <=char <= 'z':
        validate['lower']=True
     elif '0' <=char < '9':
        validate['char']=True
     elif char == ' ':
        validate['space']=True
     if (validate['upper'] and validate['lower'] and validate['char'] and validate['num'] and not validate['space'])

         print('password is valid')
     else:                                                                  
             print('password is invalid')   
    else:
          print('password is invalid')        
