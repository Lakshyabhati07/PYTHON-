n=int(input("Enter any binary no. inform of (1/0):"))
bin=int
oct=0
count=0
dec=0
i=0
while (bin > 0):
    rem= bin%10
    dec = dec + rem*(2)**i
    count=count+1
    i+=1
    if count==3:
        oct=dec
        count=0
        dec=0
        i=0
    bin/=10
oct=oct+dec*10
print("Equivalent octal no. is:",oct)
