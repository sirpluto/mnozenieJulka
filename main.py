import random
import os
#import webbrowser
import subprocess
import time
import sys

nagrody = {1  : ["Barbie w świecie mody",                   "https://www.youtube.com/watch?v=8zHVfRTNkrA"],
           2  : ["Barbie i Jej Siostry w Krainie Kucyków",  "https://www.youtube.com/watch?v=oMeH-3IZ04o"],
           3  : ["Barbie: Tajne agentki",                   "https://www.youtube.com/watch?v=tE5tYShcAs0"],
           4  : ["Barbie w świecie gier ",                  "https://www.youtube.com/watch?v=GLbJH6E-8BQ"],
           5  : ["Barbie i Tajemnicze Drzwi",               "https://www.youtube.com/watch?v=1dwxBP0zed4"],
           6  : ["Barbie: Tajne agentki",                   "https://www.youtube.com/watch?v=tE5tYShcAs0&t=2s"],
           7  : ["Barbie i Jej Siostry w Krainie Kucyków ", "https://www.youtube.com/watch?v=oMeH-3IZ04o&t=1s"],
           8  : ["Barbie i magiczne baletki",               "https://www.youtube.com/watch?v=G0W3p0mrHK0"],
           9  : ["Barbie i Akademia Księżniczek",           "https://www.youtube.com/watch?v=iiij2ApJg_c"],
           10 : ["WIELKI WYŚCIG ",                          "https://www.youtube.com/watch?v=ISnS0z4TkHk&t=443s"],
           11 : ["DZIECIAKI MOJEJ SIOSTRY W AFRYCE",        "https://www.youtube.com/watch?v=g96u-yBL1-s"],
           12 : ["DZIECI Z BULLERBYN ",                     "https://www.youtube.com/watch?v=yVgSgxtqjNU"],}

webBrowser = {"win"   : "start microsoft-edge:",
              "mac"   : "open -a safari ",
              "linux" : "open"}


def ver_os():
    platform = sys.platform
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "mac"
    elif platform == "win32":
        return "win"


def run_game():
    #webbrowser.open_new("https://www.youtube.com/watch?v=pt35aFuCaW8")
    #os.system("start microsoft-edge:https://www.youtube.com/watch?v=kC50nvw9xXI")
    for nr in nagrody:
        print(str(nr) + " : " + nagrody[nr][0])
    wybor = int(input("Wybierz nagrode: "))

    proc = subprocess.Popen(str(webBrowser[ver_os()] + nagrody[wybor][1]), shell = True)
    return proc

def stop_game(proc):
    proc.terminate()
    print(proc.pid)
    os.kill(proc.pid, 0)
    if (ver_os() == "win"):
        os.system("Taskkill /IM MicrosoftEdge.exe /F")
    elif (ver_os() == "mac"):
        os.system("killall Safari")


def separator_print():
    print('=' * 60)


def czysc_ekran():
    if (ver_os() == "win"):
        os.system("cls")
    else: #mac and linux
        os.system('clear')


def wczytaj_wynik():
    try:
        wynik = int(input("="))
    except ValueError:
        wynik = 0
    return wynik


def ile_pkt(start, stop):
    ilePkt = 1
    czasTmp = stop - start
    if (czasTmp < 10):
        ilePkt = 5
    return ilePkt

maxOk = 200
maxLi =   9
minLi =   2
a     =   0
b     =   0
ileOk =   0

while ileOk < maxOk:
    czysc_ekran()
    print("Pozostało {} poprawna odpowiedzi aby otrzymac nagrode".format(maxOk-ileOk))
    print('' *10)
    a = random.randint(minLi, maxLi)
    b = random.randint(minLi, maxLi)
    print("Podaj wynik mnozenia {}*{}".format(a, b))
    timeStart = time.perf_counter()
    wynik = wczytaj_wynik()
    timeStop = time.perf_counter()
    if (wynik == a*b):
        ileOk += ile_pkt(timeStart, timeStop)
        separator_print()
    else:
        roznica = wynik - (a*b)
        if (roznica >= 9 or roznica <= -9):
            print("Duzy blad :( - punk karny")
            ileOk -= 1
        print("Sprobujmy cos latwiejszego :)")
        for i in range(1, b+1):
            print("Podaj wynik mnozenia {}*{}".format(a, i))
            wynik = wczytaj_wynik()
            if (wynik == a*i):
                print("Brawo")
            else:
                print(":(")
                print("Prawidlowa odpowiedz to: {}".format(a*i))
        print("Teraz znasz juz odpowiedz na {}*{}".format(a,b))
        wynik = wczytaj_wynik()
        if (wynik == a*b):
            print("Brawo")
            ileOk += 1
        else:
            print("Sprobjemy inne dzialanie")
        separator_print()
p = run_game()
time.sleep(600)
stop_game(p)

#print(p)
#p = subprocess.Popen("start chrome /new-tab www.google.com",shell = True)
#time.sleep(10) #delay of 10 seconds
#p.kill()
#p.terminate()
#print(p.pid)