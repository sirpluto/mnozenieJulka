import os
import subprocess
import sys
import random

nagrody = {1  : ["Barbie w swiecie mody",                   "https://www.youtube.com/watch?v=MVt4CiCbU9s"],
           2  : ["Barbie i Jej Siostry w Krainie Kucykow",  "https://www.youtube.com/watch?v=8KyCaPaOJjc"],
           3  : ["Barbie: Tajne agentki",                   "https://www.youtube.com/watch?v=Qnyyc6JEgv8"],
           4  : ["Barbie w swiecie gier ",                  "https://www.youtube.com/watch?v=zxGeFeTerA0"],
           5  : ["Barbie i Tajemnicze Drzwi",               "https://www.youtube.com/watch?v=1dwxBP0zed4"],
           6  : ["Barbie i magiczne baletki",               "https://www.youtube.com/watch?v=G0W3p0mrHK0"],
           7  : ["Barbie i Akademia Ksiezniczek",           "https://www.youtube.com/watch?v=T6rx-BeRQEQ"],
           8  : ["WIELKI WYSCIG ",                          "https://www.youtube.com/watch?v=ISnS0z4TkHk&t=443s"],
           9  : ["DZIECIAKI MOJEJ SIOSTRY W AFRYCE",        "https://www.youtube.com/watch?v=g96u-yBL1-s"],
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
    #for nr in nagrody:
    #    print(str(nr) + " : " + nagrody[nr][0])
    #wybor = int(input("Wybierz nagrode: "))
    wybor = random.randint(1, 9)

    proc = subprocess.Popen(str(webBrowser[ver_os()] + nagrody[wybor][1]), shell = True)
    return proc

def stop_game(proc):
    proc.terminate()
    print(proc.pid)
    os.kill(proc.pid, 0)
    if ver_os() == "win":
        os.system("Taskkill /IM MicrosoftEdge.exe /F")
    elif ver_os() == "mac":
        os.system("killall Safari")

