#!/usr/bin/python3
import json 


def save_changes(url,port):
    data = {}
    data["data"]=[]
    data["data"].append(
        {
            'url': url,
            'port': port
        }
    )
    with open("__init__/target.json", "w+") as target:
        js_str = json.dumps(data)
        target.write(js_str)
        target.close()


def config_attk(url , port):
    print("## TARGET ## ==>  url: %s , port: %s"%  (url , port) )
    if(url != None and port != None):
        loop = True
        while(loop):
            check = input("do you want to change the previous url and port ? (Y/N) ")
            if(check == "Y"):
                url =input("Please enter the URL : ")
                port = input("Port : ")
                loop = False 
            elif(check == "N"):
                loop = False 
            else :
                print("Bad response")
    else:
        url =input("Please enter the URL : ")
        port = input("Port : ")
    
    save_changes(url,port)
    return url , port
