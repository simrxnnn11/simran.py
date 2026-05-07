#mysraper.py

import requests
from bs4 import Beautifulsoup

print("testing.....please wait")
# This fetches a simple website
response =requests.get("https://google.com")
soup =Beautifulsoup(response.text, 'html.parser')

# This prints the title of website
print("website Title is:", soup.title.string)
 


C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe