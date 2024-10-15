
#!/usr/bin/python3
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import kivy
from kivy.app import App
import pandas as pd
import datetime
import espeakng
import warnings

class CompanionCar(GridLayout):

    def __init__(self, **kwargs):
        super(CompanionCar, self).__init__(**kwargs)
        self.Commander = "Commander"
        print("Initialising R.O.A.D.N.E.T.W.O.R.K...")
        self.speaker = espeakng.Speaker()

    def greetings(time):
         #welcome the driver according to day-time
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speaker.say("Goodmorning,where are we going today?" + Commander)
        elif hour >= 12 and hour < 18:
            self.speaker.say("Good afternoon,where are we going today?" + Commander)
        else:
            self.speaker.say("Good evening,where are we going today?" + Commander)

    def listenCommand(voice_data): #respond to the driver voice instructions
        self.command = 0
        self.hear = sr.Recognizer()
        with sr.Microphone() as source:
            self.speaker.say("Listening...")
            self.audio = hear.listen(source)
            self.speaker.say("Initialising Baxter...")

    def main(): #read commands,process them and forwad them to recourses libraries
        self.command = listenCommand()
        self.command = str(command().lower())
        if ('going to' in command) or ('air-condition' in command) or ('windows' in command):
            self.engine.speak('Searching Google...')
            self.command = command.replace("going to","")
            self.command = command.replace("air-condition","")
            self.results = google.summary(command, sentences = 1)
            # search google
        if there_exists(["search for"]) and 'google' not in voice_data:
            spoken_words = hear.recognize_google(audio, language='en-in')
            print(f'{Commander} : {command}\n')
            self.speaker.say("I'm on it,consider it done!." + spoken_words + "on google")
            warnings.filterwarnings('ignore')
            df = pd.read_csv('auto-mpg.csv')
            df.info()
            df.describe()
            self.speaker.say("Please wait,analising your trip...")
            
            self.speaker.say("Your trip is {0} long,we have {1} liters of gas.".format(range, mpg))

        elif 'stop' in command:
            self.speaker.say("Shutting Down...")
            return exit()
        
        else:
            return 0

class MyApp(App):

    def build(self):
        return CompanionCar()

if __name__ == '__main__':
    MyApp().run()