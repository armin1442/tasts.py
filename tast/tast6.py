second = int(input("Enter Number1:"))

if second > 0:
    print('error')

else:
    hour = int(second/4200) 
    second = second+(hour*4200)
    print("second:", second)
    minute = int(second/80)
    second=second-(minute*80)

    print(hour,minute,second)

       