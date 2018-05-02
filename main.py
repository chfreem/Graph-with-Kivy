from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
import matplotlib.pyplot as plt
import numpy as np
#from kivy.clock import Clock
#from kivy.uix.behaviors import ButtonBehavior


#class HorizontalButton(ButtonBehavior, Widget):
#    def __init__(self, **kwargs):
#        super(HorizontalButton, self).__init__(**kwargs)
#
#
#class VerticalButton(ButtonBehavior, Widget):
#    def __init__(self, **kwargs):
#        super(VerticalButton, self).__init__(**kwargs)
#    pass
#
#
class Button(Widget):
    pass


class GraphSession(Widget):
    def __init__(self):
        super(GraphSession, self).__init__()

    graph_now =  ObjectProperty(None)
#    gas_pedal =  ObjectProperty(None)
#    brake_pedal =  ObjectProperty(None)

#    speed = NumericProperty(0)

    def create_graph(self):
        pass

#    def accelerate(self):
#        self.speed = self.speed * 1.1 + 1.0


class GraphAttemptApp(App):
    def build(self):
        session = GraphSession()
        return session


if __name__ == "__main__":
    GraphAttemptApp().run()


