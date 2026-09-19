import pyttsx3 
import speech_recognition as sr 
import math 
from tkinter import *
from tkinter import ttk
import threading 

engine=pyttsx3.init()
recognizer=sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    global stop_listening
    stop_listening=False

    with sr.Microphone() as source:
        while not stop_listening:

            try:
                #ui code  
                root.after(0,status_label.config,{'text':'lsitening'})
                audio=recognizer.listen(source)
                command=recognizer.recognize_google(audio)
                result=calculate()
                #ui code 

                if result is not None:
                     display_text.insert(END,f'You said:{command}\n)

            except sr.UnknownValueError:
                print('Sorry , I dint understand')

            except sr.RequestError:
                print('Bad Error')
                #ui code 
                      

def calculate(command):
    command=command.lower()

    try: 
        if 'add' in command or '+' in command or 'sum' in command or 'plus' in command:
            numbers=[ float(n) for n in command.spilt() if n.replace('.','').isdigt()]

        elif 'subtract'in command or '-' in command or 'minus' in command or 'difference' in command:
               numbers=[ float(n) for n in command.spilt() if n.replace('.','').isdigt()]
               result=numbers[0]-numbers[1]

        elif 'multiplication'in command  or ' *' in command or 'multipy' in command:
             numbers=[ float(n) for n in command.spilt() if n.replace('.','').isdigt()]
             result=numbers[0]*numbers[1]
        elif 'Divide' in command or '/' in command or 'Divison' in command:
            numbers=[ float(n) for n in command.spilt() if n.replace('.','').isdigt()]
            result=numbers[0]/numbers[1]
        elif 'power'in command:
            numbers=[ float(n) for n in command.spilt() if n.replace('.','').isdigt()]
            result=math.pow(numbers[0],numbers[1])
        elif 'square'in command:
                    numbers=[ float(n) for n in command.spilt() if n.replace('.','').isdigt()]
                    result=numbers[0]**2
        else:
             print('operation not supported')
    except Exception:
         print('Error')
         result='Error'
    return result

def start_listening():
     threading.Thread(target=listen).start()

def stop_listen():
    global stop_listening
    stop_listening=True 
    

def clear_conversation():
    #ui code 
    display_text.delete(1,END)
    status_label.config(text='Converstion ')
root=Tk()

root.title('Voice Calculator')
root.geometry(700 * 500 )
root.resizable(False,False)
root.configure(bg="#D66F3362")        
## > concept of threading : if we need to do parallel execution we use threading .

style=ttk.Style()
style.theme_use('clam')

style.configure('TButton',font=('Arial','10','bold'),background='#0AD80A',foreground='BLACK',padding=10)

style.configure('TLabel',font=('Arial','10','bold'),background='#DACC08',foreground='BLACK',padding='10')
style.configure('Status_label',font=('Arial','10','bold'),background='#DACC08',foreground='BLACK',padding='10')
button_frame=ttk.frame(root)

button_frame.pack()

start_button=ttk.Button(button_frame,text='start listening',command=start_listening)
start_button.pack(side=LEFT,padx)