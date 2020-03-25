from io import BytesIO
from requests import get
from glob import glob
from os import getcwd,remove
from zipfile import ZipFile


def bootstrapLoading():
    print("Front End components Loading...")
    components_url = "https://github.com/twbs/bootstrap/archive/v4.3.1.zip"
    parse_zip = get(components_url)
    file_name = parse_zip.headers['content-disposition'].split("filename=")[1]
    with open(file_name,"wb") as writer:
        writer.write(parse_zip.content)
        ZipFile(file_name,"r").extractall(getcwd())

    remove(str(getcwd())+'\\'+file_name)
    print("Front End Components Loaded")



