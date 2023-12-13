from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
LabelBase.register(name="nav_rail", fn_regular="fonts\\Nasalization-rg.ttf")

class Messenger(MDApp):
    def build(self):
        self.icon="images\messenger.png"
        self.title="Messenger"
        return Builder.load_file('design.kv')

Messenger().run()
