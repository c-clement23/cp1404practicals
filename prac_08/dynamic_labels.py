from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """App that dynamically creates Labels for a list of names"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.names = ["Alice", "Bob", "Charlie", "Dana"]