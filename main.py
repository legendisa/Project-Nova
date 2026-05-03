from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
import random

KV = """
BoxLayout:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos; size: self.size
    Widget:
        size_hint_y: None
        height: dp(200)
        canvas:
            Color:
                rgba: 0, 1, 0, 1
            Line:
                ellipse: (self.center_x - 80, self.center_y - 50, 160, 100)
                width: 2
            Color:
                rgba: 0, 1, 1, 1
            Ellipse:
                pos: self.center_x - 25, self.center_y - 25
                size: 50, 50
    Label:
        text: 'PROJECT NOVA'
        font_size: '36sp'
        color: 0, 1, 0, 1
    Label:
        text: app.status_text
        font_size: '20sp'
        color: 0, 1, 1, 1
    Label:
        text: 'DEVELOPER: ISA YORUK'
        font_size: '14sp'
        color: 0.5, 0.5, 0.5, 1
"""

class NovaApp(App):
    status_text = StringProperty("SYSTEM ONLINE")
    def build(self):
        Clock.schedule_interval(self.update, 1)
        return Builder.load_string(KV)
    def update(self, dt):
        cpu = random.randint(10, 99)
        self.status_text = f"CPU: {cpu}% | SECURE"

if __name__ == "__main__":
    NovaApp().run()
