from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.card import MDCard
import to_do_list
from to_do_list import MainApp
from kivymd.uix.chip import MDChip

Window.size = (350,600)

class Dashboard(MDApp):
    def build(self):
        self.theme_cls.theme_style =  "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        self.todolist = MainApp()
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("dashboard.kv"))
        screen_manager.add_widget(Builder.load_file("conversation.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("parent_profile_screen1.kv"))
        screen_manager.add_widget(Builder.load_file("parent_profile_screen3.kv"))
        return screen_manager



if __name__ == "__main__":
    LabelBase.register(name="MPoppins",
                       fn_regular=r"C:\Users\feyi1\PycharmProjects\Game Project\Athena Winter Hackathon\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins",
                       fn_regular=r"C:\Users\feyi1\PycharmProjects\Game Project\Athena Winter Hackathon\Poppins-SemiBold.ttf")
    Dashboard().run()