#!/usr/bin/python3

import getopt,sys,os
sys.path.append('__init__')
from art import *
import get_ip as ad
import file_mg as file 
import config_Backup as config
from termcolor import colored 
import json 


print(colored(text2art ("Agis1"),'cyan'))
print(colored('Created by Nicolas MENUT \n\n'.center(60),'red'))
url = None 
port = None 
# Lecture du fichier json si il y a des informations pré-enregistrés
with open('__init__/target.json') as json_backup :
    data = json.load(json_backup)
    for p in data['data']:
        url = p["url"]
        port = p["port"]

def help():
    f = open('__init__/help.txt','r')
    fcontent = f.read()
    print(fcontent)
    f.close()

def nmap1():
    global url 
    global port
    url, port = config.config_attk(url, port)
    # config.save_changes(url,port)
    path_dir ="reports/" + url
    file.create_dir(path_dir)
    ip = ad.get(url)
    print('The IP Address is :',ip)
    os.system('gnome-terminal -- bash -c "nmap -A '+ip+' -o '+path_dir+'/nmap.txt && bash"') 
    os.system('gnome-terminal -- bash -c "nikto +h '+url+' -p '+port+' -output '+path_dir+'/nikto.txt && bash"')
    os.system('gnome-terminal -- bash -c "python3 __init__/dirsearch/dirsearch.py -u '+url+":"+port+ ' -e * --simple-report='+path_dir+'/dirsearch.txt && bash"')

	
def nmap2():
    global url 
    global port
    url, port = config.config_attk(url, port)
    config.save_changes(url,port)
    path_dir ="reports/" + url
    file.create_dir(path_dir)
    ip = ad.get(url)
    print('The IP Address is :',ip)
    os.system('gnome-terminal -- bash -c "nmap -sV --script=vuln '+ip+' -o '+path_dir+'/nmap_vuln.txt && bash"') 


def main():
    full_cm_arg = sys.argv 
    arg_list = full_cm_arg[1:]
    short_options = "ho:nu"
    long_options = ["help","nmap1","nmap2", 'output=','verbose']

    try:
        args , values, = getopt.getopt(arg_list , short_options,long_options)
        for current_arg , current_val in args :
            if current_arg in ("-n","--nmap1"):
                nmap1()  
            if current_arg in ("-u","--nmap2"):
                nmap2()   
            if current_arg in ("-h","--help"):
                help()
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

if __name__ == '__main__':
    main()