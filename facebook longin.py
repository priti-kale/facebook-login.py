print("open facebook click creat accound")
first_name=input("enter the first name")
if first_name>="a" and first_name<="z"or first_name>="A" and first_name<="Z":
    last_name=input("enter the last name")
    if last_name>="a" and last_name<="z"or last_name>="A" and last_name<="Z":
        date=int(input("enter the birth_date"))
        month=int(input("enter the month"))
        year=int(input("enter the year"))
        if date>=1 and date<=31 and month>=1 and month<=12 and year>=1980 and year<=2021:
            print(date,"/",month,"/",year,"birth date is valid click next")
            gender=input("enter your gender")
            if gender=="male" or gender=="female":
                print("click next")
                otp=input("enter the otp")
                if len(otp)==6:
                    print("click next")
                    gmail=input("enter your gmail")
                    if gmail>="a" or gmail<="z" and gmail>="0" and gmail<="9":
                        print(gmail+"@gmail.com")
                        psd=input("enter the password")
                        if psd>="a" and psd<="z" or psd>="A"and psd<="Z" and psd>="1"and psd<=9 and psd=="@"or psd=="#"or  psd=="&" or psd=="$"or psd=="!":
                            print("click sine up")
                        
                            print("your accound is ready")
                        else:
                            print("enter the valid password")
                    else:
                        print("enter the valid gmail")
                else:
                    print("cheack massage")
            else:
                print("enter gender")
        else:
            print("enter the valid birth date")
    else:
        print("enter the vald first name")
else:
    print("enter the valid first name")


        
                





                     

                   
        

                





             





         
         

