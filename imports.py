import datetime
import os
import smtplib
import webbrowser as wbr

import psutil
import pyautogui
import pyttsx3  # text to speech
import requests
import speech_recognition as spr
import wikipedia
from flask import Flask, Response
from flask_restful import Api, Resource

import config as cfg
