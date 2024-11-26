# Made by - Manan Garg 

#this program caters 3 things 
#GUI - It is a simple graphical user interface to interact with the user.It also integrates all the other functions of the program.
#PASSWORD AND OTP GENERATOR - it generates passwords and otp of given length by a user and choses a random character from the given list of characters,number and symbol as per user request , then it transform list to a string and shuffle the string's content before displaying it
#MORSE TO TEXT TRANSLATOR AND VICE VERSA - it converts morse code to text and text to morse code , it map user given code or text to morse code or text respectively, then it display the result .
#SIMPLE AI CHATBOT- it takes user input and display the response of the chatbot according to our code, it uses if-else condition to check the response .due to our lack of knowledge it is a very basic ai chatbot tbh it is not even ai but a simple if-else chatbot.

#all the comments except for dated comments are added on 13 nov

#importing random , appopener, webbrowser and kivy library to make our code work
import random
import webbrowser

from AppOpener import open#opens app

#importing diffrent GUI function to make an interactive GUI 
from kivy.app import App#makes app
from kivy.uix.boxlayout import BoxLayout#window layout
from kivy.uix.label import Label#makes labels
from kivy.uix.button import Button#makes button
from kivy.uix.textinput import TextInput#takes input box
from kivy.uix.popup import Popup#defines popup

# Morse code dictionary for text to morse conversion
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

#reversing the dictionary for morse to text conversion
reverse_dict = {value: key for key, value in morse_dict.items()}

# creating mainapp class for app creation
class MainApp(App):
    #it builds gui of our program ,self creates a diffrent class for easy acess 
    def build(self):
        #makes title of our app
        self.title = "PYTITAN Application"
        #defines body style and spacing for our app 
        layout = BoxLayout(orientation='vertical', padding=50, spacing=15) # edited on 14 nov
        layout.size = (400, 1000) # edited on 14 nov
        #adds title to our window 
        layout.add_widget(Label(text="Python project submitted by PYTITAN", font_size=50))#edited on 14 nov

        # PASSWORD GENERATION SECTION ( APP LOOK )
        #adds widget(displayed text) , input box(box in which input is made) , button(pressed for code execution) for password generator part display on app
        layout.add_widget(Label(text="Password Generator", font_size=40))
        self.password_letters = TextInput(hint_text="Number of letters", multiline=False)
        self.password_numbers = TextInput(hint_text="Number of numbers", multiline=False)
        self.password_symbols = TextInput(hint_text="Number of symbols", multiline=False)
        layout.add_widget(self.password_letters)
        layout.add_widget(self.password_numbers)
        layout.add_widget(self.password_symbols)
        password_button = Button(text="Generate Password", on_press=self.generate_password)
        layout.add_widget(password_button)

        # OTP GENERATION SECTION
        #adds widget(displayed text) , input box(box in which input is made) , button(pressed for code execution) for OTP generator part display on app
        layout.add_widget(Label(text="OTP Generator", font_size=40))
        self.OTP_numbers = TextInput(hint_text="Number of digits in OTP", multiline=False)
        layout.add_widget(self.OTP_numbers)
        OTP_button = Button(text="Generate OTP", on_press=self.generate_OTP)
        layout.add_widget(OTP_button)

        # Morse Code Translator Section
        #adds widget(displayed text) , input box(box in which input is made) , button(pressed for code execution) for morse translator part display on app
       
        layout.add_widget(Label(text="Morse Code Translator", font_size=40))
        self.morse_input = TextInput(hint_text="Enter text or Morse code", multiline=True)
        layout.add_widget(self.morse_input)
        morse_button = Button(text="Convert to Morse Code", on_press=self.text_to_morse)
        layout.add_widget(morse_button)
        morse_button_reverse = Button(text="Convert Morse Code to Text", on_press=self.morse_to_text)
        layout.add_widget(morse_button_reverse)

        # AI Model Section
        #adds widget(displayed text) , input box(box in which input is made) , button(pressed for code execution) for ai model part display on app
       
        layout.add_widget(Label(text="Simple AI Model", font_size=40))
        self.command_input = TextInput(hint_text="Enter your command", multiline=False)
        layout.add_widget(self.command_input)
        ai_button = Button(text="Execute Command", on_press=self.execute_command)
        layout.add_widget(ai_button)

        return layout

#before this was made on 9/11/2024

    #defining function for password generation
    
    def generate_password(self, instance):
        try:
            nr_letters = int(self.password_letters.text)
            nr_numbers = int(self.password_numbers.text)
            nr_symbols = int(self.password_symbols.text)

            letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'
            symbols = '!#$%&()*+@~`'

            password_list = (
                random.choices(letters, k=nr_letters) +
                random.choices(numbers, k=nr_numbers) +
                random.choices(symbols, k=nr_symbols)
            )
            random.shuffle(password_list)
            random.shuffle(password_list)#added 2 lines on 14 nov
            random.shuffle(password_list)

            password = ''.join(password_list)

            self.show_popup("Generated Password", f"Your password is: {password}")
        
        except ValueError:
            self.show_popup("Error", "Please enter valid numbers.") #made on 13 nov

    #defining function for OTP generation
    
    def generate_OTP(self, instance):
        try:
            nr_numbers1 = int(self.OTP_numbers.text)
            
            if nr_numbers1 < 0:
                raise ValueError("Please enter non-negative numbers.") #made on 13 nov

            numbers = '0123456789'
            OTP_list = random.choices(numbers, k=nr_numbers1) 
            
            random.shuffle(OTP_list)
            random.shuffle(OTP_list)#added 2 line on 14 nov
            random.shuffle(OTP_list)

            OTP = ''.join(OTP_list)

            self.show_popup("Generated OTP", f"Your OTP is: {OTP}")
        
        except ValueError:
            self.show_popup("Error", "Please enter valid numbers.") #made on 13 nov
   
    #defining function for text to morse translator
    
    def text_to_morse(self, instance):
        text = self.morse_input.text.upper()
        morse_code = ' '.join(morse_dict.get(char, '') for char in text)
        self.show_popup("Morse Code", f"Morse code: {morse_code}")

    #defining function for morse to text translator
    
    def morse_to_text(self, instance):
        morse = self.morse_input.text
        text = ''.join(reverse_dict.get(code, ' ') for code in morse.split())
        self.show_popup("Text", f"Text: {text}")

#before this was made in 10/11/2024

    #defining function for AI model
   
    def execute_command(self, instance):
        # AI model functionality 
        # Made on 22 oct
        
        command = self.command_input.text.lower()
        
        #simple if-else statements for chatbot
        if command == "open my instagram" or command == "open insta":
            webbrowser.open("https://www.instagram.com")
        
        elif command == "open my linkedin" or command == "open linkedin":
            webbrowser.open("https://www.linkedin.com")
        
        elif command == "open my calendar" or command == "whats my schedule":
            open("Calendar")
        
        elif command == "open spotify" or command == "play some music":
            open("Spotify")
        
        elif command == "add a task" or command == "open to do":
            open("Microsoft To Do")
        
        elif command == "order some food" or command == "open zomato":
            open("Zomato,Swiggy")
        
        elif command == "order grocery" or command == "open groceries" or command == "open blinkit":
            open("Blinkit")
        
        elif command == "open my files" or command == "open file manager":
            open("File Explorer")
        
        elif command == "open mails" or command == "check my mail":
            open("Outlook(new),Gmail")
        
        elif command == "whatsapp" or command == "check my whatsapp":
            open("WhatsApp")
        
        elif command == "open calculator" or command == "calculator":
            open("Calculator")
        
        elif command == "open my browser" or command == "search on web":
            open("Brave")
        
        elif command == "open word":
            open("Word")
        
        elif command == "open powerpoint":
            open("PowerPoint")
        
        elif command == "open excel":
            open("Excel")
        
        elif command == "open microsoft 365" or command == "open office":
            open("Microsoft 365 (Office)")
        
        elif command == "good morning":
            self.show_popup("Response", "Good Morning! How can I help you today?")
        
        elif command == "how are you" or command == "hru":
            self.show_popup("Response", "I am good! How are you feeling today?")
        
        elif command == "how many marks do pytitan expect?":
            self.show_popup("Response", "10 marks")
        
        elif command == "how did pytitan make this code" :
            self.show_popup("Response", "The project idea was given by Saurabh sir , and with the help of\n his previous teaching we made a rough version of this project \nwhich we further refined using help from Youtube(kivy and tkinter),\nchatgpt and blackbox(code refining and error assesment)")
        
        #above 2 elif added on 14 nov
        else:
            self.show_popup("Error", "Sorry, I'm unable to understand! Please try again with lateral versions.")

    #defining popup window
    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text="Close", size_hint=(0.6, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.7, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

#running the app
if __name__ == '__main__':
    MainApp().run()

#before this was made on 12/11/2024

#credit - Saurabh Sir (project idea and teaching), Ankit Sir (Ai code idea and teaching) , Matador software(GUI,Youtube).
#credit - chatgpt(code refining), blackbox(error assesment) and youtube (Project vsulisation and integration).

#If you have reached this far of code and read all of it then we appreciate your time and effort. Thank you.
#Also if you have any suggestions , ideas or flaws of our code then please do let us know. We will be happy to hear from you. Thank you.
#Point of contact - Manan Garg Gargmanan7289@gmail.com
