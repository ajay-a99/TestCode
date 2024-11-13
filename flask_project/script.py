import pyjokes
import qrcode
import pytz 
from datetime import datetime 

def joke():
   my_joke = pyjokes.get_joke(language="en", category="neutral")
   return my_joke

def qr_generator(text):
    img = qrcode.make(text)
    img.save("qr_code.png")

def time(value1):
    UTC = pytz.utc 
    entered_time = datetime.now(UTC).strftime('%Y-%m-%d %H:%M')
    IST = pytz.timezone(value1)
    current_time = datetime.now(IST).strftime('%Y-%m-%d %H:%M')
    return entered_time, current_time