# This is a simple AI GUI Interface program
# Written by Robert Miller in Python 3.8

import wolframalpha
import wikipedia
client = wolframalpha.Client("WL78H2-UW5A2L3PRT")
import PySimpleGUI as sg

sg.theme('DarkBlue')  # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout =   [ [sg.Text('Enter your Command'), sg.InputText()],
           [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Welcome to Dyslexa', layout)
# Event Loop to process "events"

import pyttsx3
engine = pyttsx3.init()


while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).textengine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

window.close()
