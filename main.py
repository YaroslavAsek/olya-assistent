from scripts.speech_syntes import makeSound
from scripts.vosk_recognise import ResultWord
import config

from fuzzywuzzy import fuzz
import time
import webbrowser
import random

print("Оля: начинаю работу!")
makeSound("начинаю работу!")


def assistent_call(mes: str):
    for i in config.AS_CALL:
        if mes.startswith(i) or fuzz.ratio(mes, i) > 75:
            return True
       
            
        
def find_command(mes: str):
    for i in mes.strip().split():
        for j in config.AS_COMS:
            if fuzz.ratio(i, j) > 75:
                return True

def filtered_commands(mes: str):
    filtered_com = ""
    if find_command(mes):
        for i in mes.split():
            for j in config.commands.keys():
                if i not in config.commands[j] or (i in config.AS_CALL) or (i in config.AS_COMS):
                    continue
                filtered_com += i+" "
          
    return filtered_com.strip()

def execute_commands(mes):

    def call(mes):
        for i in config.AS_CALL:
            if fuzz.ratio(mes, i) > 75:
                return True

    def ctime(fmes):
        for i in config.commands["TimeNow"]:
            if fuzz.ratio(fmes, i) > 75:
                return True
            
        
    def open_youtube(fmes):
        for i in config.commands["OpenYoutube"]:
            if fuzz.ratio(fmes, i) > 75:
                return True
            
            
    def open_browser(fmes):
        for i in config.commands["OpenBrowser"]:
            if fuzz.ratio(fmes, i) > 75:
                return True
            

    def compliment(fmes):
        for i in config.commands["Compliment"]:
            if fuzz.ratio(fmes, i) > 75:
                return True

    if call(mes):
        makeSound("Слушаю вас")
        print("Оля: Слушаю")

    if assistent_call(mes):
        fmes = filtered_commands(mes)
        if ctime(fmes):
            makeSound(f"Сейчас {time.strftime("%H %M")}")
            print(f"Оля: Сейчас {time.strftime("%H:%M")}")
            
        elif open_youtube(fmes):
            webbrowser.open("https://www.youtube.com/")
            makeSound("Открываю ютуб")
            print("Оля: Открываю ютуб")

        elif open_browser(fmes):
            webbrowser.open("https://www.google.com/")
            makeSound("Открываю браузер")
            print("Оля: Открываю")

        elif compliment(fmes):
            choice = random.choice(config.compliments)
            makeSound(choice)
            print(f"Оля: {choice}")
            
        
        
def main():
    try:
        while True:
            mes = ResultWord()
            if assistent_call(mes):
                print(f"Я: {mes.capitalize()}")
                execute_commands(mes)
            
    except AttributeError:
        print("Конец работы")

if __name__ == "__main__":
    main()
        
    
    

          

