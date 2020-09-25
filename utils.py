import os
import subprocess
import sys
import random

nagrody_girl = {1  : ["Barbie w swiecie mody",                   "https://www.youtube.com/watch?v=MVt4CiCbU9s"],
                2  : ["Barbie i Jej Siostry w Krainie Kucykow",  "https://www.youtube.com/watch?v=8KyCaPaOJjc"],
                3  : ["Barbie: Tajne agentki",                   "https://www.youtube.com/watch?v=Qnyyc6JEgv8"],
                4  : ["Barbie w swiecie gier ",                  "https://www.youtube.com/watch?v=zxGeFeTerA0"],
                5  : ["Barbie i Tajemnicze Drzwi",               "https://www.youtube.com/watch?v=1dwxBP0zed4"],
                6  : ["Barbie i magiczne baletki",               "https://www.youtube.com/watch?v=G0W3p0mrHK0"],
                7  : ["Barbie i Akademia Ksiezniczek",           "https://www.youtube.com/watch?v=T6rx-BeRQEQ"],
                8  : ["WIELKI WYSCIG ",                          "https://www.youtube.com/watch?v=ISnS0z4TkHk&t=443s"],
                9  : ["DZIECIAKI MOJEJ SIOSTRY W AFRYCE",        "https://www.youtube.com/watch?v=g96u-yBL1-s"],
                }

nagrody_boy = {1  : ["Jak zrobic terenowego gokarta",            "https://www.youtube.com/watch?v=p-h9rGPah3Q"],
               2  : ["Jak zbudować, zrobić gokarta",             "https://www.youtube.com/watch?v=JRRo4WvGf9o"],
               3  : ["Szukanie prawidłowej linii",               "https://www.youtube.com/watch?v=tGnbs3f_Vlg"],
               4  : ["Jazda gokartem 390cc (13KM)",              "https://www.youtube.com/watch?v=pwrfG88L_bo"],
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

def run_game(login):
    #webbrowser.open_new("https://www.youtube.com/watch?v=pt35aFuCaW8")
    #os.system("start microsoft-edge:https://www.youtube.com/watch?v=kC50nvw9xXI")
    #for nr in nagrody:
    #    print(str(nr) + " : " + nagrody[nr][0])
    #wybor = int(input("Wybierz nagrode: "))

    if user_type(login) == 'girl':
        tab_nagrody = nagrody_girl
    else:
        tab_nagrody = nagrody_boy
    wybor = random.randint(1, len(tab_nagrody))

    proc = subprocess.Popen(str(webBrowser[ver_os()] + tab_nagrody[wybor][1]), shell = True)
    return proc

def user_type(login):
    value = ''
    if login == 'julka':
        value = 'girl'
    elif login == 'jas':
        value = 'boy'
    else:
        valur = 'girl'

    return value

def stop_game(proc):
    proc.terminate()
    print(proc.pid)
    os.kill(proc.pid, 0)
    if ver_os() == "win":
        os.system("Taskkill /IM MicrosoftEdge.exe /F")
    elif ver_os() == "mac":
        os.system("killall Safari")

