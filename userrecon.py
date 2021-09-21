#!/usr/bin/python
import random
import pyfiglet
import resources.socialLinks
from colorama import init, Fore
import requests
import os
from resources.headers import headers
import datetime

init()
print(Fore.RED + pyfiglet.figlet_format("User ReCon"))
created_by = '''Vijay Sahu''' 
banner = pyfiglet.figlet_format(created_by, font='small')
print (Fore.GREEN + "Created By:\n", created_by + '\nhttps://www.github.com/vijaysahuofficial')
failed = Fore.RED +' [-] Not Found : '
found = Fore.GREEN + '[+] Found : '
outputFolder = 'output'
x = datetime.datetime.now()
username = str(input('Enter username >>> '))

ifexist = os.path.exists(outputFolder)
if ifexist is False:
    os.mkdir(outputFolder)
elif ifexist is True:
    pass
file = open(f'{outputFolder}/{username}.txt', 'a')
file.write(f'\n\n\t\t#Generated By UserReCon\n#https://github.com/vijaysahuofficial/UserReCon\nResult Generated at {x.strftime("%X %x")}\n\nAccounts Found\n\n')
file.close()
print('\n')
print(Fore.GREEN + "Finding Accounts")


class ReCon:
    def __init__(self,site_name, social_url, username, output, headers):
        self.site_name = site_name
        self.social_url = social_url
        self.name = username
        self.output = output
        self.headers = {'User-Agent': f'{random.choice(headers)}'}
    def find_account(self):
        try:
            try:
                response = requests.get(self.social_url.format(self.name),headers = self.headers, timeout=5) 
                if response.status_code == 200:
                    print(found + self.site_name, self.social_url.format(self.name))
                    ifexist = os.path.exists(self.output)
                    if ifexist is False:
                        os.mkdir(self.output)
                        file = open(f'{self.output}/{self.name}.txt','a')
                        file.write(f'{self.social_url.format(self.name)}\n')
                    elif ifexist is True:
                        file = open(f'{self.output}/{self.name}.txt','a')
                        file.write(f'{self.social_url.format(self.name)}\n')
                    else:
                        print(Fore.RED + "Something Went Wrong")
                else:
                    print(failed + self.site_name)
            except:
                print(failed + self.site_name + ' : Connection Failed')
        except requests.exceptions.ReadTimeout:
                print(failed + self.site_name + ' : Request timed out')

try:
    for i in resources.socialLinks.links:
        ReCon(i, resources.socialLinks.links[i], username, outputFolder, headers).find_account()
except KeyboardInterrupt:
    print(Fore.RED + "Pressed CTRL + C\nBYE")
print(Fore.LIGHTCYAN_EX + '\n\n\nThanks for using UserReCon')
