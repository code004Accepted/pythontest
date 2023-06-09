import requests
import time
import webbrowser
from ics import Calendar

url = "webcal://p203-caldav.icloud.com.cn/published/2/MjAxMjcyMTk2NTEyMDEyN8GBwm1FlgKQX286ky2MJ-uEC_7MKsK7VyDrT3PvH58fioQWPcWeTrDOzzAl3u7aRBDVjYfABltR4_kJ28513Hw"
response = requests.get(url)
calendar = Calendar(response.text)
html = calendar.render()

while True:
    with open("calendar.html", "w") as file:
        file.write(html)
    webbrowser.open("calendar.html")
    time.sleep(300);
