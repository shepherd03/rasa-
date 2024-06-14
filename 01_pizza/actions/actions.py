from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

ALLOWED_PIZZA_SIZES = ["small", "medium", "large", "extra-large", "extra large", "s", "m", "l", "xl"]
ALLOWED_PIZZA_FLAVORS = ["mozzarella", "fungi", "veggie", "pepperoni", "hawaii"]

class ActionOrderPizza(Action):
    def name(self) -> Text:
        return "action_order_pizza"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[EventType]:
        pizza_size = tracker.get_slot("pizza_size")
        pizza_flavor = tracker.get_slot("pizza_flavor")

        if pizza_size not in ALLOWED_PIZZA_SIZES:
            if pizza_size is None:
                dispatcher.utter_message("What size would you like your pizza to be?。")
                return []
            else:
                dispatcher.utter_message(f"Sorry,we don't offer {pizza_flavor} pizza.We only accept pizza sizes: {'/'.join(ALLOWED_PIZZA_SIZES)}")
                return [SlotSet("pizza_size", None)]

        if pizza_flavor not in ALLOWED_PIZZA_FLAVORS:
            if pizza_flavor is None:
                dispatcher.utter_message("What flavor of pizza would you like to buy?")
                return []
            else:
                dispatcher.utter_message(f"Sorry,we don't offer {pizza_flavor} pizza.We only accept pizza flavors: {'/'.join(ALLOWED_PIZZA_FLAVORS)}")
                return [SlotSet("pizza_flavor", None)]

        dispatcher.utter_message(f'OK.Your order is confirmed:{pizza_size} {pizza_flavor} pizza.')
        return []