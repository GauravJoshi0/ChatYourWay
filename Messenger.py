from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivy import Config
from kivy.lang import Builder
from kivy.core.text import LabelBase

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

LabelBase.register(name="nav_rail", fn_regular="fonts\\CourierPrime-Regular.ttf")
LabelBase.register(name="nasalization", fn_regular="fonts\\nasalization-rg.otf")
LabelBase.register(name="message", fn_regular="fonts\\Poppins-Regular.ttf")

class Messenger(MDApp):
    def on_textfield_focus(self):
        message_box=self.root.ids.text_field
        if message_box.focus:
            widget_rm=self.root.ids.field_layout.remove_widget
            widget_rm(self.root.ids.mike)
            widget_rm(self.root.ids.attach)

            global send
            send=MDIconButton(
                icon="images\send.png",
                ripple_scale=0,
                pos_hint={"center_y": .65}

            )
            self.root.ids.layout_main1.add_widget(send)
            

        elif not message_box.focus:
            widget_add=self.root.ids.field_layout.add_widget
            widget_add(self.root.ids.mike)
            widget_add(self.root.ids.attach)

            self.root.ids.layout_main1.remove_widget(send)

    def build(self):
        self.icon="images\messenger.png"
        self.title="ChatYourWay"
        return Builder.load_file('design.kv')

Messenger().run()
