import requests

url = "http://123.206.87.240:8002/web12/"

def do_it():
    while True:
        res = requests.get(url)
        if res.text.find("flag{") !=-1:
            print(res.text)
            exit(1)

if __name__ == "__main__":
    do_it()