# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# AUTHOR : MrTechX | ToolsX | UlisesCamacho
# PROJECT : URL Spoofer with Python
# VERSION : 1.6.0
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
import gdshortener                                                                              
import os                                                                                       
import time                                                                                     
from colorama import Fore,Back,Style
def ascii():                                                                                        
    print(Fore.LIGHTRED_EX+'''                                                                                   
         ____ ___ ____ ____   ____
	   / ___|_ _/ ___|  _ \ / ___|            
      | |    | | |   | |_) | |                  
	  | |___ | | |___|  __/| |___               
  	   \____|___\____|_|    \____|              
           
           Creador de Enlace			      

''')

def clear():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux
    else:
        os.system("clear")

def load():
    print(Fore.LIGHTGREEN_EX+"Generando tu nuevo url💀...")
    
def get_url_shortened():
    request_gdshortener = gdshortener.ISGDShortener()
    url = input(Fore.LIGHTGREEN_EX+"💀 Ingresa tu link >>> "+Fore.LIGHTRED_EX)
    custom_url_part = input(Fore.LIGHTGREEN_EX+"Ingresa palabras clave💀 >>> "+Fore.LIGHTRED_EX)
    true_custom_url_part = "https://" + custom_url_part + "@"
    load()
    time.sleep(1)
    shortened_url = request_gdshortener.shorten(url)
    newurl = shortened_url[0]
    final_url = newurl.replace("https://", true_custom_url_part)
    print(Fore.LIGHTGREEN_EX+"Toma tu nuevo link💀 >>> "+Fore.LIGHTRED_EX + final_url+Fore.LIGHTBLUE_EX)

clear()
ascii()
get_url_shortened()
