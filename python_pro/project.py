print(' welcome to book my show')
name=input('please enter your name :- ')
seats=int(input('please enter the number of seats,you want book :- '))
category= int (input('please select 1.diamond class\n 2.gold class\n 3.silver class\n'))
if category == 1:
    amount = seats*200
elif category == 2:
    amount =seats*150
elif category == 3:
    amount =seats*10
print('f' hi{name} you have booked {seats} seats and total amount is {amount})   