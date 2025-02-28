# import library yang diperlukan
#
from datetime import datetime # untuk set tanggal dan waktu
# from playsound import playsound # untuk memainkan lagu

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "invalid time format! please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Coba lagi..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Coba lagi..."
        else:
            return "OK"

while True:
    alarm_time = input("Masukkan waktu dalam format 'HH:MM:SS AM/PM' format: ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Set alarm untuk {alarm_time}...")
        break

    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    alarm_period = alarm_time[9:].upper()

    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        current_period = now.strftime("%p")

        if alarm_period == current_period:
            if alarm_hour == curren_hour:
                if alarm_min == current_min:
                    if alarm_sec == current_sec:
                        print("Bangung Woi")
                        # playsound('/home/ai/Downloads/Telegram Desktop/Final Fantasy VII Advent Children Soundtrack – Calling.mp3')
                        break
