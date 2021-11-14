from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (350, 600)

kv = """
MDFloatLayout:
      md_bg_color: rgba(246, 250, 255, 255)
      MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .91}
            user_font_size: "20sp"
            theme_text_color: "Custom"
            text_color: rgba(71, 92, 119, 225)
      MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"center_x": .93, "center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(71, 92, 119, 225)    
      MDLabel:
            text: "Conversation"
            pos_hint:{"center_x": .56, "center_y": .85}
            font_name: "Poppins-SemiBold.ttf"
            font_size: "22sp"
            color: rgba(71, 92, 119, 225)
      MDFloatLayout:
            size_hint: .85, .08
            pos_hint: {"center_x": .5, "center_y": .76}
            canvas:
                  Color:
                        rgb: (238/255, 238/255, 238/255, 1)
                  RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [25]
            TextInput:
                  hint_text: "Search for friend"
                  size_hint: 1, None
                  pos_hint: {"center_x": .5, "center_y": .5}
                  height: self.minimum_height
                  multiline: False
                  cursor_colour: 96/255, 74/255, 215/255, 1
                  cursor_width: "2sp"
                  foreground_color: 96/255, 74/255, 215/255, 1
                  background_color: 0,0,0,0
                  padding:15
                  font_name: "Poppins-LightItalic.ttf"
                  font_size: "18sp"
      GridLayout:
            size_hint_y: None
            row_default_height:60
            height: self.minimum_height
            cols:1
            spacing: 15, 10
            padding: 30, 90
            MDFloatLayout:
                  MDIconButton:
                        icon: "arrow-right"
                        pos_hint: {"center_x": .09, "center_y": .51}
                        user_font_size: "40sp"
                        theme_text_color: "Custom"
                        text_color: rgba(71, 92, 119, 225)
                  MDLabel:
                        text: "Love Quinn"
                        font_size: "16sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .63}               
                        color: rgba(71, 92, 119, 255)
                  MDLabel:
                        text: "Hey Love, is the bakery class still"
                        font_size: "14sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .32}               
                        color: rgba(188, 202, 228, 255)
            MDFloatLayout:
                  MDIconButton:
                        icon: "arrow-right"
                        pos_hint: {"center_x": .09, "center_y": .51}
                        user_font_size: "40sp"
                        theme_text_color: "Custom"
                        text_color: rgba(71, 92, 119, 225)
                  MDLabel:
                        text: "Theo James"
                        font_size: "16sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .63}               
                        color: rgba(71, 92, 119, 255)
                  MDLabel:
                        text: "Sure, the kids will love a chance"
                        font_size: "14sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .32}               
                        color: rgba(188, 202, 228, 255)
            MDFloatLayout:
                  MDIconButton:
                        icon: "arrow-right"
                        pos_hint: {"center_x": .09, "center_y": .51}
                        user_font_size: "40sp"
                        theme_text_color: "Custom"
                        text_color: rgba(71, 92, 119, 225)
                  MDLabel:
                        text: "Annalise Keating"
                        font_size: "16sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .63}               
                        color: rgba(71, 92, 119, 255)
                  MDLabel:
                        text: "Are you able to tutor Hannah this"
                        font_size: "14sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .32}               
                        color: rgba(188, 202, 228, 255)
            MDFloatLayout:
                  MDIconButton:
                        icon: "arrow-right"
                        pos_hint: {"center_x": .09, "center_y": .51}
                        user_font_size: "40sp"
                        theme_text_color: "Custom"
                        text_color: rgba(71, 92, 119, 225)
                  MDLabel:
                        text: "Sharpay Evans"
                        font_size: "16sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .63}               
                        color: rgba(71, 92, 119, 255)
                  MDLabel:
                        text: "The kids loved it! Saved me a lot"
                        font_size: "14sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .32}               
                        color: rgba(188, 202, 228, 255)
            MDFloatLayout:
                  MDIconButton:
                        icon: "arrow-right"
                        pos_hint: {"center_x": .09, "center_y": .51}
                        user_font_size: "40sp"
                        theme_text_color: "Custom"
                        text_color: rgba(71, 92, 119, 225)
                  MDLabel:
                        text: "Mindy Lahiri"
                        font_size: "16sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .63}               
                        color: rgba(71, 92, 119, 255)
                  MDLabel:
                        text: "Hey Anette, I'm available today"
                        font_size: "14sp"
                        font_name: "Poppins-SemiBold.ttf"
                        pos_hint: {"center_x": .73, "center_y": .32}               
                        color: rgba(188, 202, 228, 255)
      MDTextButton:
            text: "Delete chat history"
            font_name: "Poppins-Medium.ttf"
            font_size: "13sp"
            theme_text_color: "Custom"
            text_color: rgba(71, 92, 119, 225)
            pos_hint: {"center_x": .47, "center_y": .08}
"""
class ConversationPage(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
   ConversationPage().run()

