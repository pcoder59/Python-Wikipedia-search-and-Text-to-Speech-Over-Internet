import requests
import bs4
import playsound
import pyttsx3

search = input("Search Anything: ")

def speech(msg):
    msgobj = pyttsx3.init()
    msgobj.say(msg)
    msgobj.runAndWait()

def fetchData(search):
    res = requests.get("https://en.wikipedia.org/wiki/"+search)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    data = soup.select("p")
    print(data[1].text)
    speech(data[1].text)
    
fetchData(search)