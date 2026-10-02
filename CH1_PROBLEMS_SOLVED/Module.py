import pyjokes
import pyttsx3

# fetch a random joke 
joke = pyjokes.get_jokes()
print("joke:",joke)

# text to speech
engine = pyttsx3.init()

# finishing
engine.say(joke)
engine.RunandWait()
