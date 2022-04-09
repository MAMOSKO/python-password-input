# -*- coding: utf-8 -*-
from pynput.keyboard import Key, Listener
from threading import Thread


characters="abcçdefgğhıijklmnoçprsştuüvyzwxq1234567890.,_-!+%"

password=""
passwordText=""

def changeTexta(text,i,a):
    "FUNCTION FOR passwordInput"
    returnText=""
    while i<len(text):
        returnText=returnText+a
        i+=1
    return returnText


def passwordInput(passtext=""):
    global password
    print(str(passtext),end="\r")
    def on_press(key):
        global password
        if key==Key.backspace and password != "":
            l=len(password)
            password=password[:l-1]
        elif key==Key.enter:
            print("")
            global passwordText
            passwordText=password
            return False
        else:
            if str(key).replace("'","") in characters or key==Key.space:
                if key==Key.space:
                    password=password+" "
                else:
                    password=password+str(key).replace("'","")
        print(changeTexta(password,-20," "),end="\r")
        print(str(passtext)+changeTexta(password,0,"*"),end="\r")
    with Listener(on_press=on_press) as listener:
        listener.join()
        if listener=="":
            return ""
    return passwordText


passwordInput.__doc__="""
Kullanimi "input" fonksiyonu ile aynidir.
Its usage is the same as the "input" function.

Ornek/Example:
from passwordInput import passwordInput
password=passwordInput.passwordInput("Enter Password: ")
print("Password is "+password)

https://mamosko.ml
https://github/MAMOSKO
"""
