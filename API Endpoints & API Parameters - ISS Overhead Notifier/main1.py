import requests
from datetime import datetime
import smtplib
MY_LAT=12.904863
MY_LNG=77.506489

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response)
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude<=MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
def is_dark():
    para = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted":0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=para)
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
        return True

    


# print(sunrise)
# print(sunset)
# sun = sunrise.split("T")[1].split(":")[0]
# print(sun)
# date = sun[0]
# time = sun[1]
# print(date)
# print(time)
# print(sun)