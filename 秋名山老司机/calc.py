import requests
import requests_html

url = "http://123.206.87.240:8002/qiumingshan/"

s = requests_html.HTMLSession()

info = s.get(url)

calc = info.html.find("div", first=True).text

express = calc[0:len(calc)-3]

result = eval(express)

result = str(result)


return_info = s.post(url, data={'value':  result})

print(return_info.text)