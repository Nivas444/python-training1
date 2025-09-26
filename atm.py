while True:
    pin=(int(input("Enter the pin:")))
    if pin == 2005:
        print("pin is correct")
        break
    else:
        print("pin is incorrect")
        pas1=(int(input("To change pin press 1:")))
        if pas1==1:
            get_pass=(int(input("Enter a new pin:")))
            np=''
            get_pass=np
        if np == get_pass:
            print("pin has changed")
            print(f"your new pin is:",np,get_pass)
        
        

