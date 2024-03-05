from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (200, 200)

Builder.load_string('''
<MenuPage>:
    size: 200, 200
    canvas.before:
        Color:
            rgba: 0.9, 0.8, 0.9, 1 
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'horizontal'
        padding: 5
        spacing: 5
        size_hint_y: None
        width: 150
        height: 80
        pos_hint: {'down': 1}

        Button:
            background_normal: 'prev.png'
            on_release: root.prev_song()

        Button:
            background_normal: 'play.png'
            on_release: root.plays()

        Button:
            background_normal: 'next.png'
            on_release: root.next_song()
''')



class MenuPage(Screen):
    Mlist = ['Wii.mp3', 'Dababy.mp3', 'Borat.mp3', 'Pewds.mp3']

    def __init__(self, **kwargs):
        super(MenuPage, self).__init__(**kwargs)
        self.Im = 0
        self.Cmusic = SoundLoader.load(self.Mlist[self.Im])

    def plays(self):
        if self.Cmusic:
            if self.Cmusic.state == 'stop':
                self.Cmusic.play()
            else:
                self.Cmusic.stop()

    def next_song(self):
        self.Im = (self.Im + 1) % len(self.Mlist)
        if self.Cmusic:
            self.Cmusic.unload()
        self.Cmusic = SoundLoader.load(self.Mlist[self.Im])
        self.plays()
    
    def prev_song(self):
        self.Im = (self.Im - 1) % len(self.Mlist)
        if self.Cmusic:
            self.Cmusic.unload()
        self.Cmusic = SoundLoader.load(self.Mlist[self.Im])
        self.plays()


sm = ScreenManager()
menu = MenuPage(name='menu')
sm.add_widget(menu)


class MpplayerApp(App):
    def build(self):
        return sm


MpplayerApp().run()
