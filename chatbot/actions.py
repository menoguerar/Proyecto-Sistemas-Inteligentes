from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot("location")
        response = "El clima es una mierdaaaaaa en "+mylocation(loc)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]

def mylocation(location):
    return location+"xD"