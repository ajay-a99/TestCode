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

def calculate_weight_on_planets(weight_on_earth):
    gravity_factors = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19,
        "Pluto": 0.06
    }
    weights_on_planets = {planet: int(weight_on_earth) * factor for planet, factor in gravity_factors.items()}
    print(weights_on_planets,'***********************')
    return weights_on_planets

# Example usage
# weight_on_earth = 70  # weight in kg
# weights = calculate_weight_on_planets(weight_on_earth)

# for planet, weight in weights.items():
#     print(f"Weight on {planet}: {weight:.2f} kg")
