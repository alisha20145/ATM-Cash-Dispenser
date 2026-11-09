print("Atm Dispensing Machine")
total10 = total50 = total100 = total200 = total5 = total1 =0
while True:
    name=input("Enter your name: ")
    print(f"Hello, {name}!")
    amount=int(input("Enter your amount: "))
    if  amount<0:
        print("Invalid! Enter a positive amount:")
        continue
    idx=1
    while idx<=6:
        if idx==1: value=200
        elif idx==2: value=100
        elif idx==3: value=50
        elif idx==4: value=10
        elif idx==5: value=5
        else: value=1

        count=amount//value
        if count>0:
            print(f"{count} x {value} - unit note(s) = {count*value}")
            amount-=count * value
            if value==200: total200+=count
            elif value==100: total100+=count
            elif value==50: total50+=count
            elif value==10: total10+=count
            elif value==5: total5+=count
            else: total1+=count
        idx+=1

    again=input("Is there another customer? (yes/no) : ").lower()
    if again=="yes":
        continue
    else:
        break