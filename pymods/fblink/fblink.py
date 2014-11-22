#!/usr/bin/python

import os

    # Open main facebook url.
def openurl():
    os.system('clear')
    os.system('sensible-browser --new-window="https://www.facebook.com"')
    os.system('clear')

    # Open main mobile facebook url.
def openmob():
    os.system('clear')
    os.system('sensible-browser --new-window="https://m.facebook.com"')
    os.system('clear')

    # Open Apollon Data Metrics facebook url.
def apollon():
    os.system('clear')
    os.system('sensible-browser --new-window="https://www.facebook.com/apollondma"')
    os.system('clear')

    # Open Ubuntu Linux facebook url.
def ubuntu():
    os.system('clear')
    os.system('sensible-browser --new-window="https://www.facebook.com/ubuntulinux"')
    os.system('clear')

    # Open custom prompted facebook url.
def custom():
    os.system('clear')
    os.system('CUST=$(zenity --entry --title="Facebook.." --text="Open (username/page)") && sensible-browser --new-window="https://www.facebook.com/$CUST"')
    os.system('clear')


