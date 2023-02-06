from gtts import gTTS
from playsound import playsound
import datetime


def alarm_ring():
    # It is a text value that we want to convert to audio
    text_val = 'Good Morning.Have a nice day'
    # Here are converting in English Language
    language = 'en'

    # Passing the text and language to the engine,speed can also be set
    obj = gTTS(text=text_val, lang=language, slow=False)

    # save the voice in mp3 format
    obj.save("alarm.mp3")

    # Play the exam.mp3 file
    playsound("alarm.mp3")


now = datetime.datetime.now()
current_time = now.strftime("%H:%M")
# print(current_time)
alarm_time = input("alarm time(H:M): ")
if alarm_time == current_time:
    alarm_ring()
