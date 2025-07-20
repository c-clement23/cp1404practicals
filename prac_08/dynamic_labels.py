from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """App that dynamically creates Labels for a list of names"""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)

        self.names = ["Alice", "Bob", "Charlie", "Dana"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root