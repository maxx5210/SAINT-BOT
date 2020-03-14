from time import sleep
from datetime import date
import threading


boucle = 1

def boucle():
    today = date.today()
    print("Today's date:", today)
    threading.Timer(60, boucle())

boucle()