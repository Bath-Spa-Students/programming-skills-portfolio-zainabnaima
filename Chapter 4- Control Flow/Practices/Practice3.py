'''Q3. Write a python program with nested decision structures that perform the following: If amount1
is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2'''

amount1 = 12  
amount2 = 80  

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1)
    else:
        print(amount2)
