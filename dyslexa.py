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
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    try:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        sg.Popup(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        sg.Popup(wiki_res)

window.close()
