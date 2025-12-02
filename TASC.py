# Save as main.py in Pydroid 3
# Install required package first in Pydroid 3 terminal:
# pip install kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import time

# Fake password
CORRECT_PASSWORD = "192919"

class TASCApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)  # Black background
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=15)

        # Optional background (put tasc_bg.jpg in same folder)
        try:
            bg = Image(source='tasc_bg.jpg', allow_stretch=True, keep_ratio=False)
            self.layout.add_widget(bg)
            content = BoxLayout(orientation='vertical', size_hint=(1, 1), padding=40, spacing=20)
            bg.add_widget(content)
        except:
            content = self.layout
            with self.layout.canvas.before:
                Color(0, 0.05, 0, 1)
                self.rect = Rectangle(size=Window.size, pos=(0, 0))

        # Title
        title = Label(
            text="[color=00ff41]T.A.S.C[/color]",
            font_size='60sp',
            markup=True,
            font_name='Roboto'  # You can download Orbitron.ttf and use it
        )
        content.add_widget(title)

        subtitle = Label(
            text="[color=00ff00]Tactical Advanced Strategic Command[/color]",
            font_size='18sp',
            markup=True
        )
        content.add_widget(subtitle)

        welcome = Label(
            text="[color=39ff14]» WELCOME TO T.A.S.C «[/color]",
            font_size='24sp',
            markup=True
        )
        content.add_widget(welcome)

        # Username
        content.add_widget(Label(text="[color=00ff00]AGENT ID[/color]", markup=True, font_size='18sp'))
        self.username = TextInput(
            hint_text="Enter username...",
            multiline=False,
            size_hint_y=None,
            height=50,
            background_color=(0, 0.3, 0, 1),
            foreground_color=(0, 1, 0, 1),
            cursor_color=(0, 1, 0, 1)
        )
        content.add_widget(self.username)

        # Password
        content.add_widget(Label(text="[color=00ff00]PASSCODE[/color]", markup=True, font_size='18sp'))
        self.password = TextInput(
            hint_text="      ",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50,
            background_color=(0, 0.3, 0, 1),
            foreground_color=(0, 1, 0, 1),
            cursor_color=(0, 1, 0, 1)
        )
        content.add_widget(self.password)

        # Status
        self.status = Label(text="", font_size='18sp', color=(1, 0, 0, 1))
        content.add_widget(self.status)

        # Login Button
        login_btn = Button(
            text=">> EXECUTE LOGIN <<",
            size_hint_y=None,
            height=60,
            background_normal='',
            background_color=(0, 0.4, 0, 1),
            color=(0, 1, 0, 1),
            font_size='20sp'
        )
        login_btn.bind(on_press=self.login)
        content.add_widget(login_btn)

        # Startup animation
        Clock.schedule_once(self.startup, 1)

        return self.layout

    def startup(self, dt):
        msgs = [
            "Initializing quantum core...",
            "Bypassing NSA backdoor...",
            "Engaging stealth mode...",
            "Ready."
        ]
        def show_msg(i):
            if i < len(msgs):
                self.status.text = "[color=00ff41]" + msgs[i] + "[/color]"
                self.status.markup = True
                Clock.schedule_once(lambda dt: show_msg(i+1), 1.5)
            else:
                self.status.text = "[color=00ff41]Enter credentials.[/color]"
        show_msg(0)

    def shake(self, widget):
        anim = Animation(x=widget.x + 20, duration=0.1) + Animation(x=widget.x - 20, duration=0.1)
        anim += Animation(x=widget.x + 15, duration=0.1) + Animation(x=widget.x - 15, duration=0.1)
        anim += Animation(x=widget.x + 10, duration=0.1) + Animation(x=widget.x - 10, duration=0.1)
        anim += Animation(x=widget.x, duration=0.1)
        anim.start(widget)

    def login(self, instance):
        if self.password.text == CORRECT_PASSWORD:
            self.status.text = "[color=00ff00]ACCESS GRANTED[/color]"
            self.status.markup = True
            Clock.schedule_once(self.show_granted, 1.5)
        else:
            self.status.text = "[color=ff0000]ACCESS DENIED[/color]"
            self.status.markup = True
            self.shake(self.layout)

    def show_granted(self, dt):
        self.layout.clear_widgets()
        granted = BoxLayout(orientation='vertical', padding=40, spacing=20)

        granted.add_widget(Label(text="[color=00ff00]ACCESS GRANTED[/color]", font_size='50sp', markup=True))
        granted.add_widget(Label(text="[color=00ff41]CLASSIFIED LEVEL: OMEGA[/color]", font_size='24sp', markup=True))
        granted.add_widget(Label(text="[color=39ff14]Agent authenticated.[/color]", font_size='20sp', markup=True))

        terminal = Label(
            text="",
            font_size='16sp',
            color=(0, 1, 0.3, 1),
            halign='left',
            valign='top',
            text_size=(Window.width - 100, None),
            markup=True
        )
        granted.add_widget(terminal)

        self.layout.add_widget(granted)

        lines = [
            "> Neural interface: ONLINE",
            "> Satellite uplink: SECURE",
            "> Ghost protocol: ACTIVATED",
            "> Loading mission briefing...",
            "> Target acquired.",
            "\n[color=39ff14][ SYSTEM READY ][/color]"
        ]

        def type_line(i):
            if i < len(lines):
                terminal.text += lines[i] + "\n"
                Clock.schedule_once(lambda dt: type_line(i+1), 0.8)

        type_line(0)

TASCApp().run()
