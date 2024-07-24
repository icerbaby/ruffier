from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.image import Image


class AnimationUpDown(BoxLayout):
    finished = BooleanProperty(False) #!!!!
    current = NumericProperty(0) #!!!!
    
    def __init__(self, total, duration, animation_text="Присідайте",animation_color=(0.1, 0.1, 0.1),animation_text_color=(0.54510, 0.00000, 1.00000),auto_repeat=False, **kwargs):
        super().__init__(**kwargs)
        
        self.finished = False #!!!!
        self.current = 0 #!!!!
        
        self.total = total
        self.duration = duration
        self.animation_text = animation_text
        self.animation_color = animation_color
        self.animation_text_color = animation_text_color
        self.auto_repeat = auto_repeat
        


        self.animation = (
            Animation(pos_hint={"top": 0.1}, duration=duration)
            +
            Animation(pos_hint={"top": 1.0}, duration=duration)
        )
        self.animation.on_progress = self.next #!!!!
        
        self.animated_button = Button(
            text=self.animation_text,
            background_color=self.animation_color,
            color=self.animation_text_color,
            size_hint=(1, 0.2),
            pos_hint={"top": 1.0},
            
        )
        

        self.add_widget(self.animated_button)
        
    def start(self):
        self.current = 30
        self.finished = False
        self.animation.repeat = self.auto_repeat
        self.animation.start(self.animated_button)
        
    def next(self, widget, step):
        if step == 1.0:
            self.current -= 1
            if self.current == 0:
                self.finished = True
                self.animation.repeat = False
            
        