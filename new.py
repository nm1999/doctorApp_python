import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
# import nutrition
from kivy.core.window import Window
from cmath import inf
from logging.config import listen
from tabnanny import check
import webbrowser
import speech_recognition as sr
import pyttsx3
Window.size = (380, 600)
KV = """
Screen:
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title:'Doctor App'
            left_action_items: [["menu", lambda x:  nav_drawer.set_state("open") ]]            
            spacing:0

        MDLabel:
            text:"Tap the microphone "
            halign:'center'
            font_size:'22sp'

        MDIconButton:
            icon:"microphone"                                
            user_font_size: "120sp"              
            spacing:30
            padding:10
            pos_hint:{'center_x':.5,'center_y':.5}
            on_press:app.begin()
    
        MDLabel:
            text:"speak to me"
            halign:'center'
            font_size:'14sp'
                     
        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["map-marker", lambda x: app.location() ]]
                icon:'comment'
                user_font_size: "20sp"
                mode:'free-end'
                type:'bottom'
        
    

    MDNavigationDrawer:
        id: nav_drawer
        orientation:'vertical'

        Image:
            source:'l.jpg'
            size_hint:.5,.5
            pos_hint:{'center_x':.5,'center_y':.5}

        ScrollView:
            MDList:
                OneLineAvatarIconListItem:
                    text:"Profile"
                    IconLeftWidget:
                        icon: "account"

                OneLineAvatarIconListItem:
                    text:"settings"
                    IconLeftWidget:
                        icon: "account-settings-outline"

                OneLineAvatarIconListItem:
                    text:"Rate us"
                    IconLeftWidget:
                        icon: "star"

                OneLineAvatarIconListItem:
                    text:"signout"
                    IconLeftWidget:
                        icon: "logout"
                
"""
class DoctorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        # global screen_manager
        # screen_manager = ScreenManager()
        # screen_manager.add_widget(Builder.load_file('splash.kv'))
        # screen_manager.add_widget(Builder.load_file('home.kv'))
        lg = Builder.load_string(KV)
        return lg

    def begin(self):
        print("begin clicked")
        r = sr.Recognizer()

        engine = pyttsx3.init()

        def speech2():
            with sr.Microphone() as source2:
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                try:
                    r.adjust_for_ambient_noise(source2)
                    # print("Listening...")
                    # listens for the user's input
                
                    audio2 = r.listen(source2)
                    # Using ggogle to recognize audio
                    # print("Recognizing...")
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    print(MyText)
                    return MyText
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                except sr.UnknownValueError:
                    print("unknown error occured")

        def speak(text):
            engine.setProperty('rate',120)
            voices = engine.getProperty('voices')
            engine.setProperty('voice' ,voices[1].id)
            engine.say(text)
            engine.runAndWait()

        def check(info):
            if 'hello' in info or 'hi' in info:
                return speak("hey , how can i help you")
            elif 'headache' in info or 'dizzy' in info or 'stress' in info or 'stressed' in info:
                return speak('take plenty of non alcoholic fluids like water and passion fruits. Have enough sleep this will help your mind to refresh , if conditions persist contact the hosiptal from the link below ,thank you')
            elif 'stomachache' in info or 'stomach pain' in info:
                return speak('take warm water , reduce on the fatty foods you eat like chapati , donnuts and many more. Always ensure that you wash your hands after visiting the latrines. thank you ')
            elif ('posho' in info or 'cassava' in info or 'sweet potatoes' in info or 'matooke' in info) and ( 'food value' in info or 'gain' in info or 'get' in info):
                return speak("it is a source of energy for your body. ")
            elif ('beans' in info or 'eggs' in info  or 'irish ' in info or 'cawo peas' in info or 'soya' in info) and ( 'food value' in info or 'gain' in info or 'get' in info ):
                return speak("it is a good food for body building ")
            elif ("odi" in info ) and ( 'food value' in info or 'gain' in info or 'get' in info):
                return speak("Oddi is source of energy to the body") 
            elif "constipation" in info:
                return speak("Always include greens in your daily meal , this will make it easy for stomach enzymes to work more efficiently during food break down. thank u")
            elif "pregnant" in info or 'baby' in info:
                return speak("Go for regular medical check ups , so that you get extra attention for the forming baby in your womb. I wish you a safe baby delivery. thank u ")
            elif 'joint pain' in info :
                return speak("if your from making exercises , get enough rest. If you have not done any exercises , try strectching alittle, this will enable blood flow very well. If conditions persist visit the nearest government hospital")
            elif 'use condoms' in info or 'condom' in info:
                return speak("i am still being lectured about how to use condoms. Master Nyanzi Mathias is working hard to see that i get to know such information. thank you  ")
            else:
                return speak("I cannot answer your question because am still under development and training , very soon , i will be updated , ask any other question.  thank u")

        dic = {
            'welcome':'Hi , am  the beacon doctor robot. I am programmed to give advise on health challenges, Am still under development. how can i help you '
        }



        def conserve():
            speak(dic['welcome'])
            while True:
                text  =""
                listening =str(speech2())
                # print("t hass gottent the word" + str(listening))

                if listening in 'goodbye' or listening == 'stop':
                    speak('it has been good speaking to u , have a nice day')
                    break
                check(listening)
        # check(' gkiio')
        conserve()



    def navbar(self):
        print('Still in progress')

    def location(self):
        print("Go to hospital")
        webbrowser.open('https://www.google.com/maps/@2.2572733,32.8216376,1161m/data=!3m1!1e3')
    
DoctorApp().run()
