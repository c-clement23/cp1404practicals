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


MilesConverterApp().run()
