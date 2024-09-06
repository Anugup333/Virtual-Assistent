import text_to_speech as tts
import speech_to_text as stt
import datetime 
import webbrowser as web
import weather



def action(data):
    
    user_data = (str)(data).lower()

    if "what is your name" in user_data:
        tts.text_to_speech("My name is Virtual Assistent")
        return "My name is Virtual Assistent"
    
    elif "hello" in user_data or "hye" in user_data:
        tts.text_to_speech("hey, Sir How I can help you ")
        return "hey, Sir How I can help you "

    elif "good morning" in user_data:
        tts.text_to_speech("Good Morning Sir")
        return "Good Morning Sir"
    
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour)+ "Hour : ", (str)(current_time.minute)+ "Minute"
        tts.text_to_speech(Time)
        return Time

    elif "play music" in user_data:
        web.open("https://open.spotify.com/")
        tts.text_to_speech("spotify is now ready for music")
        return "spotify is now ready for music"

    elif "youtube" in user_data:
        web.open("https://youtube.com")
        tts.text_to_speech("youtube is now ready for you")
        return "youtube is now ready for you"

    elif "open google" in user_data:
        web.open("https://google.com/")
        tts.text_to_speech("google is now ready for you")
        return "google is now ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        tts.text_to_speech(ans)
        return ans
    
    elif "shutdown" in user_data:
        tts.text_to_speech("ok , Sir")
        return "ok , Sir"

    else:
        tts.text_to_speech("I am able to Understand ")
        return "I am not able to Understand "
 