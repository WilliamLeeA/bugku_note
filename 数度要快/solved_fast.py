import requests_html
import base64

s = requests_html.HTMLSession()

url = "http://123.206.87.240:8002/web6/"

def doIt():
    return_info = s.get(url)
    prototype_flag = return_info.headers.get("flag").encode()
    margin = base64.b64decode(prototype_flag).decode()
    margin = margin.split(":")[1]
    res = s.post(url, data={'margin': base64.b64decode(margin)})
    print(res.headers)
    print(res.text)



if __name__ == "__main__":
    doIt()