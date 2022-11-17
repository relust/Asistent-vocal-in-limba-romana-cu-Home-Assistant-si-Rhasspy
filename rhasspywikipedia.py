import appdaemon.plugins.hass.hassapi as hass
import wikipedia as wikipedia

class RhasspyWikipedia(hass.Hass):
    
    def initialize(self):
        self.listen_event(self.first_event, "RHASSPYWIKIPEDIA_EVENT")

    def first_event(self, event_name, data, kwargs):
        wikipedia.set_lang("ro") 
        sessionId = data.get("sessionId")
        question = data.get("question")
        object = data.get("object")
        result = wikipedia.summary(object, sentences = 2)
        self.call_service("mqtt/publish", topic = "hermes/dialogueManager/continueSession", payload_template = '{"sessionId": "' + str(sessionId) + '", "text": " conform wikipedia ' + result + ' "}')
        
        self.log(object)
        #self.call_service("tts/google_translate_say", entity_id = "media_player.ha_display", message = result)

