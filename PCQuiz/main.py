import time
import colorama

print('\033[33m'"""
 ________  ________          ________  ___  ___  ___  ________     
|\   __  \|\   ____\        |\   __  \|\  \|\  \|\  \|\_____  \    
\ \  \|\  \ \  \___|        \ \  \|\  \ \  \\\  \ \  \\|___/  /|   
 \ \   ____\ \  \            \ \  \\\  \ \  \\\  \ \  \   /  / /   
  \ \  \___|\ \  \____        \ \  \\\  \ \  \\\  \ \  \ /  /_/__  
   \ \__\    \ \_______\       \ \_____  \ \_______\ \__\\________\ 
    \|__|     \|_______|        \|___| \__\|_______|\|__|\|_______|
                                      \|__|                                                                                     
"""'\033[39m')


print("Welkom bij mijn quiz!")

playing = input("Wil je meedoen met mijn quiz? [Ja/Nee] ")
time.sleep(0.5)

if playing.lower() != "ja" :
    time.sleep(0.5)
    print("Nee? Oke dan, tot ziens!")
    time.sleep(0.5)
    quit()

print("Oke. Laten we beginnen!")

def main():

        score = 0

        answer = input("Waar staat" '\033[33m' " CPU "  '\033[39m' "voor? ")

        if answer.lower() == "central processing unit":
            print("Correct!")
            score += 1
        else: 
            print("Dat is helaas fout!")
            time.sleep(0.5)
            print("Het goeie antwoord is: " '\033[31m' "Central Processing Unit" '\033[39m')
            time.sleep(1)


        answer = input("Waar staat" '\033[33m' " GPU "  '\033[39m' "voor? ")

        if answer.lower() == "graphics processing unit":
            print("Correct!")
            score += 1
        else: 
            print("Dat is helaas fout!")
            time.sleep(0.5)
            print("Het goeie antwoord is: " '\033[31m' "Graphics Processing Unit" '\033[39m')
            time.sleep(1)


        answer = input("Waar staat" '\033[33m' " RAM "  '\033[39m' "voor? ")

        if answer.lower() == "random access memory":
            print("Correct!")
            score += 1
        else: 
            print("Dat is helaas fout!")
            time.sleep(0.5)
            print("Het goeie antwoord is: " '\033[31m' "Random Access Memory" '\033[39m')
            time.sleep(1)


        answer = input("Waar staat" '\033[33m' " PSU "  '\033[39m' "voor? ")

        if answer.lower() == "power supply":
            print("Correct!")
            score += 1
        else: 
            print("Dat is helaas fout!")
            time.sleep(0.5)
            print("Het goeie antwoord is: " '\033[31m' "Power Supply" '\033[39m')
            time.sleep(1)

        score0 = 0
        score1 = score
        score2 = 2

        if (score2 > score1 and score0 < score1):
            meervoud = "vraag"
        else:
            meervoud = "vragen"

        print("Je hebt " + str(score),meervoud + " goed!")
        print("Jouw score is: " '\033[32m' + str((score / 4) * 100) + "%" '\033[39m')
        time.sleep(3)


        restart = input("Wil je de quiz opnieuw doen? [Ja/Nee] ")
        if restart.lower() == "ja":
            time.sleep(0.5)
            main()
        else:
            time.sleep(0.5)
            print("Nee? Oke dan, tot ziens!")
            time.sleep(0.5)
            quit()
main()