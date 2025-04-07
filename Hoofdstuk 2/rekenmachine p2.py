#opdracht = input("Kies uit: delen, optellen, aftrekken, vermedigvuldigen. ")
#opdracht = input("Kies uit: /, +, -, x. ")


opdracht=""
while opdracht!="stop":

    opdracht = input("Kies uit: /, +, -, x. ")



    if opdracht == str("+"):
        teller = int(input("Voer het eerste getal in: "))
        noemer = int(input("Voer het tweede getal in: "))

        som = teller + noemer 
        print("Het antwoord is: "+ str(som) )

    elif opdracht == str("-"):
        teller = int(input("Voer het eerste getal in: "))
        noemer = int(input("Voer het tweede getal in: "))

        som = teller - noemer 
        print("Het antwoord is: "+ str(som) )

    elif opdracht == str("x"):
        teller = int(input("Voer het eerste getal in: "))
        noemer = int(input("Voer het tweede getal in: "))

        som = teller * noemer 
        print("Het antwoord is: "+ str(som) )

    elif opdracht == str("/"):
        teller = int(input("Voer het eerste getal in: "))
        noemer = int(input("Voer het tweede getal in: "))

        if noemer==0:
            print ("Je kan niet door nul delen. (Je kan voor het tweede getal geen nul invoeren als je kiest voor delen.)")
        else:
            som = teller / noemer 
            print("Het antwoord is: "+ str(som) )

    else:
        print("Je hebt geen +-x of / getypt")

    opdracht = input("Kies uit: /, +, -, x of 'stop' ")
