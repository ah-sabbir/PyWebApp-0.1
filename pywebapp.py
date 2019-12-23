from template_config import template

def errors(args):
    with open("error.log","a") as er:
        er.write("\n"+str(args))
import sys,os
from os import system
filename = sys.argv
txt = ""
for i in filename[1:]:
    if ".html" in i:
        try:
            os.makedirs("Templates")
        except Exception as e:
            errors(e)
        with open("Templates/"+i,"w+") as writer:
            writer.write(template)
    elif ".css" in i:
        try:
            os.makedirs("static/css")
        except Exception as e:
            errors(e)
        with open("static/css/"+i,"w+") as r:
            r.write('body {font-family: "Lato", sans-serif}')
    elif ".js" in i:
        try:
            os.makedirs("static/js")
        except Exception as e:
            errors(e)
        with open("static/js/"+i,"w+") as r:
            pass
    else:
        print("you have enter wrong keywords :(")
        






