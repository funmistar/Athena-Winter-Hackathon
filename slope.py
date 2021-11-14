from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager
from to_do_list import MainApp
from kivymd.toast import toast

# Attempt to add a custom font

Window.size = (350,600)

class Slope(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("slope.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("dashboard.kv"))
        screen_manager.add_widget(Builder.load_file("conversation.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("community.kv"))
        screen_manager.add_widget(Builder.load_file("my_kid.kv"))
        screen_manager.add_widget(Builder.load_file("profile.kv"))
        return screen_manager

    def callback(self, instance, value):
        toast(value)

if __name__ == "__main__":
    Slope().run()


# #Hot reloader configuration
# KV = '''
# #:import KivyLexer kivy.extras.highlight.KivyLexer
# #:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer
#
# BoxLayout:
#     HotReloadViewer:
#         path: app.path_to_kv_file
#         errors: True
#         errors_text_colour: 1, 1, 0, 1
#         errors_background_colour: app.theme_cls.bg_dark
# '''
#
# class SplashScreen(MDApp):
#     path_to_kv_file = "slope.kv"
#     #build function
#     def build(self):
#         return Builder.load_string(KV)
#
#
# SplashScreen().run()