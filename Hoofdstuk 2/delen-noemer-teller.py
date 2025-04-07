teller = int(input("Voer het eerste getal in: "))
noemer = int(input("Voer het tweede getal in: "))

if noemer == 0:
    print ("Je kan niet door nul delen. (Je kan voor het tweede getal geen nul invoeren.)")

else:
    som = teller / noemer 
    print("Het antwoord is: "+ str(som) )
