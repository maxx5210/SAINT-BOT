from time import sleep
from datetime import date
import threading



def boucle():
    today = date.today()
    print("Today's date:", today)
    threading.Timer(1, lambda : boucle()).start()

boucle()