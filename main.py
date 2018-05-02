from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import matplotlib.pyplot as plt
import numpy as np


class Button(Widget):
    pass


class GraphSession(Widget):
    def __init__(self):
        super(GraphSession, self).__init__()

    graph_now =  ObjectProperty(None)

    def create_graph(self):
        x = np.linspace(0, 2, 100)

        plt.plot(x, x, label = 'linear')
        plt.plot(x, x**2, label = 'quadratic')
        plt.plot(x, x**3, label = 'cubic')

        plt.xlabel('position (m)')
        plt.ylabel('height (m)')

        plt.title("This is My Plot")

        plt.legend()

        plt.show()

class GraphAttemptApp(App):
    def build(self):
        session = GraphSession()
        return session


if __name__ == "__main__":
    GraphAttemptApp().run()


