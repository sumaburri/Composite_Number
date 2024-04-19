number=int(input('Enter  Number :'))
count=0
for fact in range(1,number+1):
    if number%fact==0:
        count=count+1
if count>2:
    print('Composite Number')
else:
     print('Not a Composite Number')
    
