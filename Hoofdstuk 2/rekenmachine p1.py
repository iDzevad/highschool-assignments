teller = int(input("Voer het eerste getal in: "))
opdracht = input("Kies uit: /, +, -, x. ")
noemer = int(input("Voer het tweede getal in: "))
#opdracht = input("Kies uit: delen, optellen, aftrekken, vermedigvuldigen. ")
#opdracht = input("Kies uit: /, +, -, x. ")

if opdracht == str("+"):
    som = teller + noemer 
    print("Het antwoord is: "+ str(som) )

elif opdracht == str("-"):
    som = teller - noemer 
    print("Het antwoord is: "+ str(som) )

elif opdracht == str("x"):
    som = teller * noemer 
    print("Het antwoord is: "+ str(som) )

elif noemer == 0:
    print ("Je kan niet door nul delen. (Je kan voor het tweede getal geen nul invoeren als je kiest voor delen.)")

elif noemer > 0:
    som = teller / noemer
    print("Het antwoord is: "+ str(som) )

#else:
 #   som = teller / noemer 
  #  print("Het antwoord is: "+ str(som) )
