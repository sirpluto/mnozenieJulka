import os
import subprocess
import sys
import random

nagrody = {1  : ["Barbie w swiecie mody",                   "https://www.youtube.com/watch?v=P0oaTAuzB70"],
           2  : ["Barbie i Jej Siostry w Krainie Kucykow",  "https://www.youtube.com/watch?v=oMeH-3IZ04o"],
           3  : ["Barbie: Tajne agentki",                   "https://www.youtube.com/watch?v=tE5tYShcAs0"],
           4  : ["Barbie w swiecie gier ",                  "https://www.youtube.com/watch?v=GLbJH6E-8BQ"],
           5  : ["Barbie i Tajemnicze Drzwi",               "https://www.youtube.com/watch?v=1dwxBP0zed4"],
           6  : ["Barbie i magiczne baletki",               "https://www.youtube.com/watch?v=G0W3p0mrHK0"],
           7  : ["Barbie i Akademia Ksiezniczek",           "https://www.youtube.com/watch?v=iiij2ApJg_c"],
           8  : ["WIELKI WYSCIG ",                          "https://www.youtube.com/watch?v=ISnS0z4TkHk&t=443s"],
           9  : ["DZIECIAKI MOJEJ SIOSTRY W AFRYCE",        "https://www.youtube.com/watch?v=g96u-yBL1-s"],
           10 : ["DZIECI Z BULLERBYN ",                     "https://www.youtube.com/watch?v=yVgSgxtqjNU"],
           11 : ["Beethoven",                               "https://www.cda.pl/video/51526636"],
           12 : ["Dzieciak rzadzi",                         "https://www.cda.pl/video/14296411e"],
           13 : ["Kacper / Casper",                         "https://www.cda.pl/video/1110078ea"],
           14 : ["Zwierzogrod",                             "http://ekino-tv.pl/movie/show/zwierzogrod-hd-zootopia-2016-dubbing/15191"],
           15 : ["High School Musical",                     "https://www.cda.pl/video/561057e7"],
           16 : ["Asterix misja Kleopatra",                 "https://www.cda.pl/video/138914f6"],
           17 : ["Emoticon",                                "https://www.cda.pl/video/1756135c3"],
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
    wybor = random.randint(1, 17)

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

