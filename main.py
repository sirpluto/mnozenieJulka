import random
import os
#import webbrowser
import subprocess
import time
import sys

nagrody = {1  : ["Barbie w świecie mody",                   "https://www.youtube.com/watch?v=P0oaTAuzB70"],
           2  : ["Barbie i Jej Siostry w Krainie Kucyków",  "https://www.youtube.com/watch?v=oMeH-3IZ04o"],
           3  : ["Barbie: Tajne agentki",                   "https://www.youtube.com/watch?v=tE5tYShcAs0"],
           4  : ["Barbie w świecie gier ",                  "https://www.youtube.com/watch?v=GLbJH6E-8BQ"],
           5  : ["Barbie i Tajemnicze Drzwi",               "https://www.youtube.com/watch?v=1dwxBP0zed4"],
           6  : ["Barbie i magiczne baletki",               "https://www.youtube.com/watch?v=G0W3p0mrHK0"],
           7  : ["Barbie i Akademia Księżniczek",           "https://www.youtube.com/watch?v=iiij2ApJg_c"],
           8  : ["WIELKI WYŚCIG ",                          "https://www.youtube.com/watch?v=ISnS0z4TkHk&t=443s"],
           9  : ["DZIECIAKI MOJEJ SIOSTRY W AFRYCE",        "https://www.youtube.com/watch?v=g96u-yBL1-s"],
           10 : ["DZIECI Z BULLERBYN ",                     "https://www.youtube.com/watch?v=yVgSgxtqjNU"],
           11 : ["Beethoven",                               "https://www.cda.pl/video/51526636"],
           12 : ["Dzieciak rządzi",                         "https://www.cda.pl/video/14296411e"],
           13 : ["Kacper / Casper",                         "https://www.cda.pl/video/1110078ea"],
           14 : ["Zwierzogród",                             "http://ekino-tv.pl/movie/show/zwierzogrod-hd-zootopia-2016-dubbing/15191"],
           15 : ["High School Musical",                     "https://www.cda.pl/video/561057e7"],
           16 : ["Asterix misja Kleopatra",                 "https://www.cda.pl/video/138914f6"],
           }

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

def losuj_dzialanie():
    tmp = random.randint(1, 100)
    if (tmp%2 == 0):
        wynik = '*'
    else:
        wynik = '/'

    return wynik

def losuj_liczby(dzialanie):
    if (dzialanie == '*'):
        a = random.randint(minLiMnozenie, maxLiMnozenie)
        b = random.randint(minLiMnozenie, maxLiMnozenie)
    else: #dzielenie
        a = 2
        b = 3
        while ((a%b != 0) or (a / b > 10)):
            a = random.randint(minLiADzielenie, maxLiADzielenie)
            b = random.randint(minLiBDzielenie, maxLiBDzielenie)
    wynik_tmp = a / b
    return a, b


def oblicz_wynik(a, b, dzialanie):
    if (dzialanie == '*'):
        wynik = a * b
    elif (dzialanie == '/'):
        wynik = a / b
    else:
        print("Bledne dzialanie w oblicz_wynik()")
    return wynik

def nauka_mnozenia(a, b):
    wynik = 0

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
        wynik = 1;
    else:
        print("Sprobjemy inne dzialanie")
    return wynik
1
def nauka_dzielenia(a, b):
    wynik = 0

    c = a/b;
    print("Podaj wynik mnozenia {}*{}".format(b, int(c)))
    wynik = wczytaj_wynik();
    if (wynik == b*c):
        print("Brawo :)")
    else:
        print(":(")
        print("Prawidłowa odpowież to: []".format(b*c))
    print("Teraz znasz juz odpowiedz na {}/{}".format(a, b))
    wynik = wczytaj_wynik()
    if (wynik == a/b):
        print("Brawo")
        wynik = 1;
    else:
        print("Spróbujemy inne działanie")

    return wynik

maxOk = 200
czasNagrody = 900;
maxLiMnozenie   =   9
minLiMnozenie   =   2
maxLiADzielenie =   100
minLiADzielenie =   2
maxLiBDzielenie =   9
minLiBDzielenie =   2
a     =   0
b     =   0
ileOk =   0

while ileOk < maxOk:
    czysc_ekran()
    print("Pozostało {} poprawna odpowiedzi aby otrzymac nagrode".format(maxOk-ileOk))
    print('' *10)
    dzialanie = losuj_dzialanie()
    a, b = losuj_liczby(dzialanie)
    print("Podaj wynik mnozenia {}{}{}".format(a, dzialanie, b))
    timeStart = time.perf_counter()
    wynik = wczytaj_wynik()
    timeStop = time.perf_counter()
    if (wynik == oblicz_wynik(a, b, dzialanie)):
        ileOk += ile_pkt(timeStart, timeStop)
        separator_print()
    else:
        roznica = wynik - oblicz_wynik(a, b, dzialanie)
        if (roznica >= 3 or roznica <= -3):
            print("Duzy blad :( - punk karny")
            ileOk -= 1
        if (dzialanie == '*'):
            #nauka mnożenia
            ileOk += nauka_mnozenia(a, b)
        else:
            #nauka dzielenia
            ileOk +=nauka_dzielenia(a,b)
        separator_print()
p = run_game()
time.sleep(czasNagrody)
stop_game(p)

#print(p)
#p = subprocess.Popen("start chrome /new-tab www.google.com",shell = True)
#time.sleep(10) #delay of 10 seconds
#p.kill()
#p.terminate()
#print(p.pid)