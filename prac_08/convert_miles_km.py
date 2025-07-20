from kivy.lang import Builder
from kivy.app import App


class MilesConverterApp(App):
    def build(self):
        self.title = "convert miles km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesConverterApp().run()
