from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivymd.uix.button import MDIconButton
from kivy import Config
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
LabelBase.register(name="nav_rail", fn_regular="fonts\\CourierPrime-Regular.ttf")
LabelBase.register(name="message", fn_regular="fonts\\Poppins-Regular.ttf")
LabelBase.register(name="test", fn_regular="fonts\\Poppins-Black.ttf")

class Messenger(MDApp):
    def build(self):
        self.icon="images\messenger.png"
        self.title="Messenger"
        return Builder.load_file('design.kv')

Messenger().run()
