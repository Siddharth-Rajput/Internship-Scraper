import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def Banner():
    print('''
  _____       _                      _     _         _____                                
 |_   _|     | |                    | |   (_)       / ____|                               
   | |  _ __ | |_ ___ _ __ _ __  ___| |__  _ _ __  | (___   ___ _ __ __ _ _ __   ___ _ __ 
   | | | '_ \| __/ _ \ '__| '_ \/ __| '_ \| | '_ \  \___ \ / __| '__/ _` | '_ \ / _ \ '__|
  _| |_| | | | ||  __/ |  | | | \__ \ | | | | |_) | ____) | (__| | | (_| | |_) |  __/ |   
 |_____|_| |_|\__\___|_|  |_| |_|___/_| |_|_| .__/ |_____/ \___|_|  \__,_| .__/ \___|_|   
                                            | |______                    | |              
                                            |_|______|                   |_|              
Made By :
Siddharth Rajput 
The keywords feature is still under development so till then 
you have to manually edit the code to set your keywords 🙂 
                                   ''')

Banner()
cookies = open('cookies.txt', 'r')
nono = cookies.read().split(":")
head = {nono[0]:nono[1]}

with requests.Session() as s:
    def fetch(url,head):
		r = s.get(url, headers=head)
		soup = BeautifulSoup(r.content, 'lxml')
		for article in soup.find_all('div', class_='internship_meta'):
			name = article.find('div', class_='heading_4_5 profile').text.strip()
			company = article.find('div', class_='heading_6 company_name').text.strip()
			stipend = article.find('span', class_='stipend').text.strip()    		
			
			def want(name, company, stipend):
				name = Style.BRIGHT + Fore.RED + name
				company = Style.BRIGHT + Fore.RED + company
				stipend = Style.BRIGHT + Fore.YELLOW + stipend
				return name, company, stipend
			def leave(name, company, stipend):
				name = Style.BRIGHT + Fore.WHITE + name
				company = Style.BRIGHT + Fore.WHITE + company
				stipend = Style.BRIGHT + Fore.WHITE + stipend
				return name, company, stipend
			
			if "devops".lower() in name.lower(): edited = want(name, company, stipend)
			elif "testing".lower() in name.lower(): edited = want(name, company, stipend)
			elif "development".lower() in name.lower(): edited = want(name, company, stipend)
			elif "automation".lower() in name.lower(): edited = want(name, company, stipend)				
			else: edited = leave(name, company, stipend)
			
			print (Style.BRIGHT + Fore.GREEN + 'Name-> ' + edited[0] + Style.BRIGHT + Fore.GREEN + ' Company-> ' + edited[1] + Style.BRIGHT + Fore.GREEN + ' Stipend-> ' + edited[2] + Style.BRIGHT + Fore.WHITE)
			#print ''
		print (Style.BRIGHT + Fore.MAGENTA + "The list of page 2......." + Style.BRIGHT + Fore.WHITE)
fetch('https://internshala.com/internships/matching-preferences',head)
fetch('https://internshala.com/internships/matching-preferences/page-2',head)

k=input("press close to exit") 
