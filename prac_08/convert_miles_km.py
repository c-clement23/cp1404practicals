from kivy.lang import Builder
from kivy.app import App
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.60934


class MilesConverterApp(App):
    result_text = StringProperty("0.0")

    def build(self):
        self.title = "convert miles km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self):
        """Convert miles to km using the input"""
        miles_str = self.root.ids.input_miles.text
        try:
            miles = float(miles_str)
        except ValueError:
            miles = 0.0
        km = miles * MILES_TO_KILOMETERS
        self.result_text = f"{km:.5f}"

    def handle_increment(self, change):
        """Increase or decrease the miles value and update result."""
        miles_str =self.root.ids.input_miles.text
        try:
            miles = float(miles_str)
        except ValueError:
            miles = 0.0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.convert()


MilesConverterApp().run()
