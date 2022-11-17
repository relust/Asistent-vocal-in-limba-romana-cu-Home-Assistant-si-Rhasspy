ASISTENT VOCAL ÎN LIMBA ROMÂNĂ
În Home Assistant se instalează addon-ul Rhasspy
Am făcut tutorial pe forumul https://smarthome360.ro/forums/forum/home-assistant/
Acestea sunt automatizările și setările pe care le-am folosit în acest proiect. 
Fișierul waw se copie în /share/rhasspy/profiles 
Directorul slots și fișierele kaldi_custom_words.txt, sentences.ini se copie în /share/rhasspy/profiles/en 
Fișierul weather.py se copie în directorul /config/phython_scripts 
Pentru wikipedia trebuie instalt addon-ul Appdaemon. Fișierul rhasspywikipedia.py se copie în /config/appdaemon/apps iar în apps.yaml din directorul appdaemon se scrie:
rhasspywikipedia:
  module: rhasspywikipedia 
  class: RhasspyWikipedia
