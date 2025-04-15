 #!/usr/bin/python

import os,sys,random,requests



def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        


try:
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    


banner = r"""


     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⠶⠶⠶⠶⠶⠶⠶⢖⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣆⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠈⠹⣦⡀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⢀⣤⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣦⣀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀
     ⠀⠀⠀⢀⡾⠁⠀⣠⡾⢁⣾⡿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣆⠹⣦⠀⠀⢻⣆⠀⠀⠀⠀
     ⠀⠀⢀⡾⠁⢀⢰⣿⠃⠾⢋⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⠀⢹⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡌⠻⠆⢿⣧⢀⠀⢻⣆⠀⠀⠀
     ⠀⠀⣾⠁⢠⡆⢸⡟⣠⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡸⣿⠀⣆⠀⢿⡄⠀⠀
     ⠀⢸⡇⠀⣽⡇⢸⣿⠟⢡⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠙⢿⣿⠀⣿⡀⠘⣿⠀⠀
     ⡀⣿⠁⠀⣿⡇⠘⣡⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣦⡙⠀⣿⡇⠀⢻⡇⠀
     ⢸⡟⠀⡄⢻⣧⣾⡿⢋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣴⣿⠉⡄⢸⣿⠀
     ⢾⡇⢰⣧⠸⣿⡏⢠⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠓⢶⠶⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠙⣿⡟⢰⡧⠀⣿⠀
     ⣸⡇⠰⣿⡆⠹⣠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣿⡏⠀⠠⢺⠢⠀⠀⣿⣷⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠸⠁⣾⡇⠀⣿⠀
     ⣿⡇⠀⢻⣷⠀⣿⡿⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡅⠀⠀⢸⡄⠀⠀⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡆⣰⣿⠁⠀⣿⠀
     ⢸⣧⠀⡈⢿⣷⣿⠃⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣇⠀⢀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⢿⣧⣿⠃⡀⢸⣿⠀
     ⠀⣿⡀⢷⣄⠹⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⡯⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⡟⢁⣴⠇⣼⡇⠀
     ⠀⢸⡇⠘⣿⣷⡈⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢰⣿⡧⠈⣴⣿⠏⢠⣿⠀⠀
     ⠀⠀⢿⡄⠘⢿⣿⣦⣿⣯⠘⣆⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⡎⢸⣿⣣⣾⡿⠏⠀⣾⠇⠀⠀
     ⠀⠀⠈⢷⡀⢦⣌⠛⠿⣿⡀⢿⣆⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢀⣿⡁⣼⡿⠟⣉⣴⠂⣼⠏⠀⠀⠀
     ⠀⠀⠀⠈⢷⡈⠻⣿⣶⣤⡁⠸⣿⣆⠡⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣾⡟⠀⣡⣴⣾⡿⠁⣴⠏⠀⠀⠀⠀
    ⠀ ⠀⠀⠀⠈⢿⣄⠈⢙⠿⢿⣷⣼⣿⣦⠹⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢡⣾⣿⣶⣿⠿⢛⠉⢀⣾⠏⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠹⣧⡀⠳⣦⣌⣉⣙⠛⠃⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠐⠛⠋⣉⣉⣤⡶⠁⣰⡿⠁⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠙⠛⠿⠿⠿⠿⠟⠛⠛⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠙⠟⠛⠿⠿⠿⠿⠟⠛⠁⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⠙⠶⣦⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⡶⠖⣁⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⡉⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠉⠉⠉⠉⣡⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⢦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣠⣴⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀



           ███████╗███████╗███╗░░██╗██╗████████╗██╗░░██╗
           ╚════██║██╔════╝████╗░██║██║╚══██╔══╝██║░░██║
           ░░███╔═╝█████╗░░██╔██╗██║██║░░░██║░░░███████║
           ██╔══╝░░██╔══╝░░██║╚████║██║░░░██║░░░██╔══██║
           ███████╗███████╗██║░╚███║██║░░░██║░░░██║░░██║
           ╚══════╝╚══════╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝
  
                                                                       
                     𝙲𝙰𝚁 𝙿𝙰𝚁𝙺𝙸𝙽𝙶 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙰𝚈𝙴𝚁 𝟷
                      𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁 𝚃𝙾 𝙲𝙾𝙽𝚃𝙸𝙽𝚄𝙴                                 
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.red_to_yellow, pyColorate.Vertical, enter=True)


pySystem.Clear()



import random
import requests
from time import sleep
import os, signal, sys
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from zenbruh import Zendev

__CHANNEL_USERNAME__ = "ZENXCPM"
__GROUP_USERNAME__   = "ZENXCHAT"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = figlet_format('ZENXCPM', font='bloody')
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋'))
    print(Colorate.Horizontal(Colors.rainbow, '    𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃'))
    print(Colorate.Horizontal(Colors.rainbow, '      𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄 𝐓𝐎 𝐁𝐔𝐘 𝐔𝐍𝐋𝐈𝐌𝐈𝐓𝐄𝐃 𝐁𝐀𝐋𝐀𝐍𝐂𝐄 𝐓𝐆 @senitbruh ')) 
    print(Colorate.Horizontal(Colors.rainbow, f' ‌                𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')

        if all(key in data for key in ['floats', 'localID', 'money', 'coin', "integers"]):
            
            console.print("[bold][red]========[/red][ PLAYER DETAILS ][red]========[/red][/bold]")
            
            console.print(f"[bold white]   >> Name        : {data.get('Name', 'UNDEFINED')}[/bold white]")
            console.print(f"[bold white]   >> LocalID     : {data.get('localID', 'UNDEFINED')}[/bold white]")
            console.print(f"[bold white]   >> Moneys      : {data.get('money', 'UNDEFINED')}[/bold white]")
            console.print(f"[bold white]   >> Coins       : {data.get('coin', 'UNDEFINED')}[/bold white]")
            friends_count = len(data.get("FriendsID", []))
            console.print(f"[bold white]   >> Friends     : {friends_count}[/bold white]")
            # Count Cars (Checking if it's nested)
            car_data = data.get("carIDnStatus", {}).get("carGeneratedIDs", [])
            # Remove duplicates by converting the list to a set
            unique_car_data = set(car_data)
            car_count = len(unique_car_data)
            console.print(f"[bold white]   >> Car Count   : {car_count}[/bold white]")
       
        else:
            console.print("[bold red] '! ERROR: new accounts must be signed-in to the game at least once (✘)[/bold red]")
            exit(1)
    else:
        console.print("[bold red] '! ERROR: seems like your login is not properly set (✘)[/bold red]")
        exit(1)
     

def load_key_data(cpm):

    data = cpm.get_key_data()
    
    console.print("[bold][red]========[/red][ ACCESS KEY DETAILS ][red]========[/red][/bold]")
    
    console.print(f"[bold white]   >> Access Key  [/bold white]: [black]{data.get('access_key')}[/black]")
    
    console.print(f"[bold white]   >> Telegram ID : {data.get('telegram_id')}[/bold white]")
    
    console.print(f"[bold white]   >> Balance     : {data.get('coins') if not data.get('is_unlimited') else 'Unlimited'}[/bold white]")
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            console.print(f"[bold red]{tag} cannot be empty or just spaces. Please try again (✘)[/bold red]")
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    console.print("[bold red] =============[bold white][ LOCATION ][/bold white]=============[/bold red]")
    console.print(f"[bold white]    >> Country    : {data.get('country')} {data.get('zip')}[/bold white]")
    console.print("[bold red] ===============[bold white][ MENU ][/bold white]===========[/bold red]")

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[/bold]", "Access Key", password=False)
        console.print("[bold yellow][%] Trying to Login[/bold yellow]: ", end=None)
        cpm = Zendev(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]ACCOUNT NOT FOUND (✘)[/bold red]")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]WRONG PASSWORD (✘)[/bold red]")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]INVALID ACCESS KEY (✘)[/bold red]")
                sleep(2)
                continue
            else:
                console.print("[bold red]TRY AGAIN[/bold red]")
                console.print("[bold yellow] '! Note: make sure you filled out the fields ![/bold yellow]")
                sleep(2)
                continue
        else:
            console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
            sleep(1)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["00", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",]
            console.print("[bold yellow][bold white](01)[/bold white]: Increase Money           [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](02)[/bold white]: Increase Coins           [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](03)[/bold white]: King Rank                [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](04)[/bold white]: Change ID                [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](05)[/bold white]: Change Name              [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](06)[/bold white]: Change Name (Rainbow)    [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](07)[/bold white]: Number Plates            [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](08)[/bold white]: Account Delete           [bold red]Free[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](09)[/bold white]: Account Register         [bold red]Free[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](10)[/bold white]: Delete Friends           [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](11)[/bold white]: Unlock Paid Cars         [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](12)[/bold white]: Unlock All Cars          [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](13)[/bold white]: Unlock All Cars Siren    [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](14)[/bold white]: Unlock W16 Engine        [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](15)[/bold white]: Unlock All Horns         [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](16)[/bold white]: Unlock Disable Damage    [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](17)[/bold white]: Unlock Unlimited Fuel    [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](18)[/bold white]: Unlock Home 3            [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](19)[/bold white]: Unlock Smoke             [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](20)[/bold white]: Unlock Wheels            [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](21)[/bold white]: Unlock Animations        [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](22)[/bold white]: Unlock Equipaments M     [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](23)[/bold white]: Unlock Equipaments F     [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](24)[/bold white]: Change Race Wins         [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](25)[/bold white]: Change Race Loses        [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](26)[/bold white]: Clone Account            [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](27)[/bold white]: Custom HP                [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](28)[/bold white]: Custom Angle             [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](29)[/bold white]: Custom Tire burner       [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](30)[/bold white]: Custom Car Millage       [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](31)[/bold white]: Custom Car Brake         [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](32)[/bold white]: Remove Rear Bumper       [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](33)[/bold white]: Remove Front Bumper      [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](34)[/bold white]: Change Account Password  [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](35)[/bold white]: Change Account Email     [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](36)[/bold white]: Custom Spoiler           [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](37)[/bold white]: Custom BodyKit           [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](38)[/bold white]: Unlock Premium Wheels    [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](39)[/bold white]: Unlock Toyota Crown      [bold red]1[/bold red][/bold yellow]")
            console.print("[bold yellow][bold white](0) [/bold white]: Exit From Tool [/bold yellow]")
            
            console.print("[bold red]===============[bold white][ SERVICE ][/bold white]===============[/bold red]")
            
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            console.print("[bold red]===============[bold white][ PROCESSING, PLS WAIT! ][/bold white]===============[/bold red]")
            
            if service == 0: # Exit
                console.print("[bold white] Thank You for using my tool[/bold white]")
            elif service == 1: # Increase Money
                console.print("[bold yellow][bold white][?][/bold white] Insert how much money do you want[/bold yellow]")
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("[bold green]======================================[/bold green]")
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold red]please try again later! (✘)[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold red]please use valid values! (✘)[/bold red]")
                    sleep(2)
                    continue
            elif service == 2:  # Increase Coins
                console.print("[bold yellow][bold white][?][/bold white] Insert how much coins do you want[/bold yellow]")
                amount = IntPrompt.ask("[?] Amount")
                print("[ % ] Saving your data: ", end="")
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("[bold green]======================================[/bold green]")
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                        else: continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] 'Please use valid values[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    console.print("[bold yellow] '======================================[/bold yellow]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold yellow] '[?] Enter your new ID[/bold yellow]")
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                        console.print("[bold yellow] '======================================[/bold yellow]")
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                        else: continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] 'Please use valid ID[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold yellow] '[?] Enter your new Name[/bold yellow]")
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                        console.print("[bold yellow] '======================================[/bold yellow]")
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                        else: continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] 'Please use valid values[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print("[bold yellow] '[?] Enter your new Rainbow Name[/bold yellow]")
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                        console.print("[bold yellow] '======================================[/bold yellow]")
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                        else: continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] 'Please use valid values[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Giving you a Number Plates: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                console.print("[bold yellow] '[!] After deleting your account there is no going back !![/bold yellow]")
                answ = Prompt.ask("[?] Do You want to Delete this Account ?!", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    console.print("[bold yellow] '======================================[/bold yellow]")
                    console.print("[bold yellow] f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}[/bold yellow]")
                else: continue
            elif service == 9: # Account Register
                console.print("[bold yellow] '[!] Registring new Account[/bold yellow]")
                acc2_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                acc2_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Creating new Account: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    console.print("[bold yellow] '======================================[/bold yellow]")
                    console.print("[bold yellow] f'INFO: In order to tweak this account with Telmun[/bold yellow]")
                    console.print("[bold yellow] 'you most sign-in to the game using this account[/bold yellow]")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] 'This email is already exists ![/bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Deleting your Friends: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Note: this function takes a while to complete, please don't cancel.", end=None)
                console.print("[%] Unlocking All Paid Cars: ", end=None)
                if cpm.unlock_paid_cars():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Unlocking All Cars: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Unlocking All Cars Siren: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Unlocking w16 Engine: ", end=None)
                if cpm.unlock_w16():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Unlocking All Horns: ", end=None)
                if cpm.unlock_horns():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Unlocking Disable Damage: ", end=None)
                if cpm.disable_engine_damage():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Unlocking Unlimited Fuel: ", end=None)
                if cpm.unlimited_fuel():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Unlocking House 3: ", end=None)
                if cpm.unlock_houses():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Unlocking Smoke: ", end=None)
                if cpm.unlock_smoke():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 20: # Unlock Smoke
                console.print("[%] Unlocking Wheels: ", end=None)
                if cpm.unlock_wheels():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(8)
                    continue
            elif service == 21: # Unlock Smoke
                console.print("[%] Unlocking Animations: ", end=None)
                if cpm.unlock_animations():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 22: # Unlock Smoke
                console.print("[%] Unlocking Equipaments Male: ", end=None)
                if cpm.unlock_equipments_male():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] Unlocking Equipaments Female: ", end=None)
                if cpm.unlock_equipments_female():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                console.print("[bold yellow] '[!] Insert how much races you win[/bold yellow]")
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                        console.print("[bold yellow] '======================================[/bold yellow]")
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                        else: continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] '[!] Please use valid values[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                console.print("[bold yellow] '[!] Insert how much races you lose[/bold yellow]")
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                        console.print("[bold yellow] '======================================[/bold yellow]")
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                        else: continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold yellow] '[!] Please use valid values[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] '[!] Please use valid values[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                console.print("[bold yellow] '[!] Please Enter Account Detalis[/bold yellow]")
                to_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                to_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Cloning your account: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:     
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] '[!] THAT RECIEVER ACCOUNT IS GMAIL PASSWORD IS NOT VALID OR THAT ACCOUNT IS NOT REGISTERED[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 27:
                console.print("[bold yellow][!] Note[/bold yellow]: original speed can not be restored!.")
                console.print("[bold yellow][!] Enter Car Details.[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] Car Id[/bold]")
                new_hp = IntPrompt.ask("[bold][?]Enter New HP[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?]Enter New Inner Hp[/bold]")
                new_nm = IntPrompt.ask("[bold][?]Enter New NM[/bold]")
                new_torque = IntPrompt.ask("[bold][?]Enter New Torque[/bold]")
                console.print("[bold yellow][%] Hacking Car Speed[/bold yellow]:",end=None)
                if cpm.hack_car_speed(car_id, new_hp, new_inner_hp, new_nm, new_torque):
                    console.print("[bold green]SUCCESFUL (✔)[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold yellow] '[!] Please use valid values[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 28: # ANGLE
                console.print("[bold yellow] '[!] ENTER CAR DETALIS[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold yellow] '[!] ENTER STEERING ANGLE[/bold yellow]")
                custom = IntPrompt.ask("[red][?]﻿ENTER THE AMOUNT OF ANGLE YOU WANT[/red]")                
                console.print("[red][%] HACKING CAR ANGLE[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 29: # tire
                console.print("[bold yellow] '[!] ENTER CAR DETALIS[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold yellow] '[!] ENTER PERCENTAGE[/bold yellow]")
                custom = IntPrompt.ask("[pink][?]﻿ENTER PERCENTAGE TIRES U WANT[/pink]")                
                console.print("[red][%] Setting Percentage [/red]: ", end=None)
                if cpm.max_max2(car_id, custom):
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    answ = Prompt.ask("[bold green][?] DO YOU WANT TO EXIT[/bold green] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 30: # Millage
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW MILLAGE![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTER MILLAGE U WANT[/bold blue]")                
                console.print("[bold red][%] Setting Percentage [/bold red]: ", end=None)
                if cpm.millage_car(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 31: # Brake
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW BRAKE![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTER BRAKE U WANT[/bold blue]")                
                console.print("[bold red][%] Setting BRAKE [/bold red]: ", end=None)
                if cpm.brake_car(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 32: # Bumper rear
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")                
                console.print("[bold red][%] Removing Rear Bumper [/bold red]: ", end=None)
                if cpm.rear_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 33: # Bumper front
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")                
                console.print("[bold red][%] Removing Front Bumper [/bold red]: ", end=None)
                if cpm.front_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 75:  # /testin endpoint
                console.print("[bold]ENTER CUSTOM FLOAT DATA[/bold]")
                custom = IntPrompt.ask("[bold][?] VALUE (e.g. 1 or 0)[/bold]")     # This is the value
                console.print(f"[bold red][%] Setting float key... [/bold red]", end=None)
                if cpm.testin(custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold yellow]FAILED[/bold yellow]")
                    console.print("[bold yellow]PLEASE TRY AGAIN[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 34:
                console.print("[bold]Enter New Password![/bold]")
                new_password = prompt_valid_value("[bold][?] Account New Password[/bold]", "Password", password=False)
                console.print("[bold red][%] Changing Password [/bold red]: ", end=None)
                if cpm.change_password(new_password):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white]Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold yellow]FAILED[/bold yellow]")
                    console.print("[bold yellow]PLEASE TRY AGAIN[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 36: # telmunnongodz
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER SPOILER ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]ENTER NEW SPOILER ID[/bold blue]")                
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end=None)
                if cpm.telmunnongodz(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 37: # telmunnongonz
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER BODYKIT ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERT BODYKIT ID[/bold blue]")                
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end=None)
                if cpm.telmunnongonz(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 35:
                console.print("[bold]Enter New Email![/bold]")
                new_email = prompt_valid_value("[bold][?] Account New Email[/bold]", "Email")
                console.print("[bold red][%] Changing Email [/bold red]: ", end=None)
                if cpm.change_email(new_email):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white]Thank You for using my tool[/bold white]")
                    else: break
                else:
                    console.print("[bold red]FAILED[/bold yellow]")
                    console.print("[bold red]EMAIL IS ALREADY REGISTERED [/bold red]")
                    sleep(4)
            elif service == 38: # SHITTIN
                console.print("[%] Unlocking Premium Wheels..: ", end=None)
                if cpm.shittin():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 39: # Unlock toyota crown
                console.print("[!] Note: this function takes a while to complete, please don't cancel.", end=None)
                console.print("[%] Unlocking Toyota Crown: ", end=None)
                if cpm.unlock_crown():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            else:
                continue
            break
        break              
