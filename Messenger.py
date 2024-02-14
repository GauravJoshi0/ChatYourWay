from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy import Config
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen, ScreenManager

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

LabelBase.register(name="nav_rail", fn_regular="fonts\\CourierPrime-Regular.ttf")
LabelBase.register(name="nasalization", fn_regular="fonts\\nasalization-rg.otf")
LabelBase.register(name="message", fn_regular="fonts\\Poppins-Regular.ttf")

class User(MDLabel):
    ...

class Response(MDLabel):
    ...

class SettingWindow(Screen):
    ...

class ChatWindow(Screen):
    def send(self, object):
        message=self.manager.get_screen("chatwindow").ids.text_field.text
        layout=self.manager.get_screen("chatwindow").ids.layout
        if (len(message))<=5:
            lblsize=0.1
        elif (len(message))<=14:
            lblsize=0.19
        elif (len(message))<=20:
            lblsize=0.27
        else:
            lblsize=0.4
        layout.add_widget(User(text=message, valign="center", size_hint_x=lblsize))
        # self.manager.get_screen("chatwindow").ids.text_field.text=""
        
    def on_textfield_focus(self):
        message_box=self.manager.get_screen("chatwindow").ids.text_field
        if message_box.focus:
            widget_rm=self.manager.get_screen("chatwindow").ids.field_layout.remove_widget
            widget_rm(self.manager.get_screen("chatwindow").ids.mike)
            widget_rm(self.manager.get_screen("chatwindow").ids.attach)

            global send
            send=MDIconButton(
                icon="images\send.png",
                ripple_scale=0,
                pos_hint={"center_y": .5, "right": 1},
                on_press=self.send

            )
            self.manager.get_screen("chatwindow").ids.field_layout.add_widget(send)
            

        elif not message_box.focus:
            widget_add=self.manager.get_screen("chatwindow").ids.field_layout.add_widget
            widget_add(self.manager.get_screen("chatwindow").ids.mike)
            widget_add(self.manager.get_screen("chatwindow").ids.attach)

            self.manager.get_screen("chatwindow").ids.field_layout.remove_widget(send)

class WindowManager(ScreenManager):
    ...

class Messenger(MDApp):


    def build(self):
        self.icon="images\messenger.png"
        self.title="ChatYourWay"
        return Builder.load_file('design.kv')

Messenger().run()
