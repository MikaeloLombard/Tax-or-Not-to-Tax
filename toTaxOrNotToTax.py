
# Calculate the total charge of an order, plus taxes, depending on the region.
# As an example Canada is used.
# Regions other than Canada and some provinces will not be taxed. 

startAgain = "yes"
while startAgain == "yes":
    
    country = input("Enter name of your country: ").upper()
    province = input("Enter name of your province: ").upper()
    orderTotal = float(input("What is your order total? $"))


    if country == "CANADA" and (province == "ONTARIO" or province == "NEW BRUNSWICK"): 
        print("Your total plus interest is: ")
        product = orderTotal * 0.0013 + orderTotal
        print (("${:,.2f}") .format(product))
        
    elif country == "CANADA" and province == "NOVA SCOTIA":
        print("Your total plus interest is: ")
        product = orderTotal * 0.0013 + orderTotal
        print (("${:,.2f}") .format(product))
        

    elif country == "CANADA" and province == "Alberta":
        print("Your total plus interest is: ")
        product = orderTotal * 0.0005 + orderTotal
        print (("${:,.2f}") .format(product))
        

    elif country == "CANADA":
        print("Your total plus interest is: ")
        product = orderTotal * 0.0011 + orderTotal
        print (("${:,.2f}") .format(product))
        

    else:
        print("Your total is: ")
        product = int((orderTotal))
        print (("${:,.2f}") .format(product))
       
    startAgain = input("Do you want to start again? ")


    
        
        
        


    




