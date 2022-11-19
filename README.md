ASISTENT VOCAL ÎN LIMBA ROMÂNĂ
Demo: https://youtu.be/_TUVXTEl2JQ

TUTORIAL https://smarthome360.ro/forums/topic/asistent-vocal-in-limba-romana-cu-home-assistant-si-rhasspy/

În Home Assistant se instalează addon-ul Rhasspy

Acestea sunt automatizările și setările pe care le-am folosit în acest proiect. 

Fișierul waw se copie în /share/rhasspy/profiles 

Directorul slots și fișierele kaldi_custom_words.txt, sentences.ini se copie în /share/rhasspy/profiles/en

Fișierul weather.py se copie în directorul /config/python_scripts 

Pentru wikipedia trebuie instalt addon-ul Appdaemon pentru că integrarea python_scripts nu suportă funcția import. Fișierul rhasspywikipedia.py se copie în /config/appdaemon/apps iar în apps.yaml din directorul appdaemon se scrie:

rhasspywikipedia:
  module: rhasspywikipedia 
  class: RhasspyWikipedia
