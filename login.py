from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (350, 600)

kv = """
MDFloatLayout:
   md_bg_color: 1,1,1,1
   Image:
      source: 'logo.png'
      pos_hint: {"y": .25}
   MDLabel:
      text: "S I G N    I N"
      pos_hint:{"center_x": .5, "center_y": .5}
      halign: "center"
      font_name: "Poppins-SemiBold.ttf"
      font_size: "30sp"
      theme_text_color: "Custom"
      text_color: 60/225, 43/255, 117/255, 1
   MDFloatLayout:
      size_hint: .85, .08
      pos_hint: {"center_x": .5, "center_y": .38}
      canvas:
         Color:
            rgb: (238/255, 238/255, 238/255, 1)
         RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [25]
      TextInput:
         hint_text: "Email"
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
   MDFloatLayout:
      size_hint: .85, .08
      pos_hint: {"center_x": .5, "center_y": .28}
      canvas:
         Color:
            rgb: (238/255, 238/255, 238/255, 1)
         RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [25]
      TextInput:
         hint_text: "Password"
         password : True
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
   MDTextButton:
      text: "Forget your password?"
      font_name: "Poppins-Light.ttf"
      font_size: "13sp"
      theme_text_color: "Custom"
      text_color: 255,255,255, 1
      pos_hint: {"center_x": .5, "center_y": .21}
   MDLabel:
      text: "Don't have an account?"
      font_name: "Poppins-Light.ttf"
      font_size: "12sp"
      text_color: 255,255,255, 1
      pos_hint: {"center_x": .68, "center_y": .04} 
   MDTextButton:
      text: "Sign up here"
      font_name: "Poppins-Light.ttf"
      font_size: "12sp"
      color: rgba(60, 43, 117, 700)
      pos_hint: {"center_x": .70, "center_y": .04}
   Button:
      text: "Login"
      font_name: "Poppins-Light.ttf"
      font_size: "20sp"
      size_hint: .5, .08
      pos_hint: {"center_x": .5, "center_y": .12}
      background_color: 0,0,0,0
      canvas.before:
         Color:
            rgb: 246/255, 135/255, 177/255, 1
         RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [23]
"""

class LoginPage(MDApp):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    LoginPage().run()



