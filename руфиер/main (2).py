from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window

from kivy.uix.image import Image



from ruffier import *
from texts import *
from timer import *
from animationupdown import AnimationUpDown
from counter import Counter

Window.clearcolor = (0.75, 0.7, 0, 0.4)

name = "Illia"
age = 14

p1, p2, p3 = 0, 0, 0

def is_integers(*args):
    for arg in args:
        try:
            arg = int(arg)
        except:
            return False
    return True

class Registration(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=8
        )
        
        self.input_name_layout = BoxLayout(
            orientation="horizontal"
        )
        
        self.input_age_layout = BoxLayout(
            orientation="horizontal"
        )
        
        self.instruction_label = Label(
            text=txt_instruction,
            color = (0, 0, 1, 1)
        )
        
        self.name_label = Label(
            text=txt_input_name
        )
        
        self.name_input = TextInput()
        
        self.age_label = Label(
            text=txt_input_age
        )
        
        self.age_input = TextInput()
        
        self.go_next_button = Button(
            text=txt_go_next,
            color = [0, 0, 0, 1],
            background_color = [0.4, 1, 0.5, 1]
        )

        
        



        self.go_next_button.on_press = self.next_screen
        
        self.main_layout.add_widget(self.instruction_label)
        
        self.input_name_layout.add_widget(self.name_label)
        self.input_name_layout.add_widget(self.name_input)
        self.main_layout.add_widget(self.input_name_layout)
        
        self.input_age_layout.add_widget(self.age_label)
        self.input_age_layout.add_widget(self.age_input)
        self.main_layout.add_widget(self.input_age_layout)
        
        self.main_layout.add_widget(self.go_next_button)
        
        self.add_widget(self.main_layout)
        
    def next_screen(self):
        global name, age
        
        name = self.name_input.text
        age = self.age_input.text
        
        if is_integers(age):
            age = int(age)
            self.manager.current = "2"
    
class FirstPulse(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.can_go_next_screen = False # !!!!!!!!!!!!
        
        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=8
        )
        
        self.input_p1_layout = BoxLayout(
            orientation="horizontal"
        )
        
        self.instruction_label = Label(
            text=txt_test1,
            color = (0, 0, 1, 1)
        )
        
        self.timer = Timer(total_seconds=1) # !!!!!!!!!
        self.timer.bind(finished=self.on_timer_finished) # !!!!!!!!
        
        self.p1_label = Label(
            text=txt_input_p1
        )
        
        self.p1_input = TextInput()
        self.p1_input.set_disabled(True) # !!!!!!!!!!
        
        self.go_next_button = Button(
            text=txt_go_next,
            color = [0, 0, 0, 1],
            background_color = [0.4, 1, 0.5, 1]
        )
        self.go_next_button.on_press = self.next_screen
        
        self.main_layout.add_widget(self.instruction_label)
        self.main_layout.add_widget(self.timer) # !!!!!!!!!!!!!!!!!!!!
        
        self.input_p1_layout.add_widget(self.p1_label)
        self.input_p1_layout.add_widget(self.p1_input)
        self.main_layout.add_widget(self.input_p1_layout)
        
        self.main_layout.add_widget(self.go_next_button)
        
        self.add_widget(self.main_layout)
        
    def on_timer_finished(self, *args):
        self.can_go_next_screen = True
        self.p1_input.set_disabled(False)
        self.go_next_button.set_disabled(False)
        
    def next_screen(self):
        global p1
        
        if self.can_go_next_screen:
            p1 = self.p1_input.text
            if is_integers(p1):
                p1 = int(p1)
                self.manager.current = "3"
        else:
            self.go_next_button.set_disabled(True)
            self.timer.start()

class PhysicWork(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.can_go_next_screen = False # !!!!
        
        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=8
        )
        
        self.top_layout = BoxLayout(
            orientation="horizontal"
        ) # !!!!
        
        self.instruction_label = Label(
            text=txt_sits,
            color = (0, 0, 1, 1)
        )
        
        self.animationupdown = AnimationUpDown(
            total=30,
            duration=1.25,
            animation_text="Присідайте!",
            animation_color=(0.54510, 0.00000, 1.00000),
            animation_text_color=(1, 1, 1),
            auto_repeat=True
        ) # !!!!
        
        self.counter = Counter(
            total=30,
            text="Залишилося присідань"
        ) # !!!!
        

        self.animationupdown.bind(finished=self.on_animation_finish)
        self.animationupdown.bind(current=self.counter.next)
        
        self.go_next_button = Button(
            text=txt_go_next,
            color = [0, 0, 0, 1],
            background_color = [0.4, 1, 0.5, 1]
        )
        self.go_next_button.on_press = self.next_screen
        
        self.top_layout.add_widget(self.instruction_label)
        self.top_layout.add_widget(self.counter)
        self.top_layout.add_widget(self.animationupdown)
        
        self.main_layout.add_widget(self.top_layout)
        self.main_layout.add_widget(self.go_next_button)
        
        self.add_widget(self.main_layout)
        
    def on_animation_finish(self, *args):
        self.can_go_next_screen = True
        self.go_next_button.set_disabled(False)
        
    def next_screen(self):
        if not self.can_go_next_screen:
            self.go_next_button.set_disabled(True)
            self.animationupdown.start()
        else:
            self.manager.current = "4"

class PulseSecondThird(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.can_go_next_screen = False
        self.stage = 1
        
        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=8
        )
        
        self.input_p2_layout = BoxLayout(
            orientation="horizontal"
        )
        
        self.input_p3_layout = BoxLayout(
            orientation="horizontal"
        )
        
        self.instruction_label = Label(
            text=txt_test3,
            color = [0, 0, 1, 1],
        )
        
        self.timer = Timer(total_seconds=5)
        self.timer.bind(finished=self.on_timer_finished)
        
        self.p2_label = Label(
            text=txt_input_p2
        )
        
        self.p2_input = TextInput()
        self.p2_input.set_disabled(True)
        
        self.p3_label = Label(
            text=txt_input_p3
        )
        
        self.p3_input = TextInput()
        self.p3_input.set_disabled(True)
        
        self.go_next_button = Button(
            text=txt_go_next,
            color = [0, 0, 0, 1],
            background_color = [0.4, 1, 0.5, 1]
        )
        self.go_next_button.on_press = self.next_screen
        
        self.main_layout.add_widget(self.instruction_label)
        self.main_layout.add_widget(self.timer)
        
        self.input_p2_layout.add_widget(self.p2_label)
        self.input_p2_layout.add_widget(self.p2_input)
        self.main_layout.add_widget(self.input_p2_layout)
        
        self.input_p3_layout.add_widget(self.p3_label)
        self.input_p3_layout.add_widget(self.p3_input)
        self.main_layout.add_widget(self.input_p3_layout)
        
        self.main_layout.add_widget(self.go_next_button)
        
        self.add_widget(self.main_layout)
        
    def on_timer_finished(self, *args):
        if self.timer.finished:
            if self.stage == 1:
                self.stage = 2
                self.timer.restart(total_seconds=5)
                self.p2_input.set_disabled(False)
            elif self.stage == 2:
                self.stage = 3
                self.timer.restart(total_seconds=5)
            elif self.stage == 3:
                self.stage = 4
                self.timer.restart(total_seconds=5)
            elif self.stage == 4:
                self.p3_input.set_disabled(False)
                self.go_next_button.set_disabled(False)
                self.can_go_next_screen = True
        
    def next_screen(self):
        global p2, p3
        
        if self.can_go_next_screen:
            p2 = self.p2_input.text
            p3 = self.p3_input.text
            
            if is_integers(p2, p3):
                p2 = int(p2)
                p3 = int(p3)
                self.manager.current = "5"
        else:
            self.go_next_button.set_disabled(True)
            self.timer.start()

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.result_label = Label(text="",color = [0, 0, 1, 1])
        
        self.on_enter = self.on_screen_enter
        
        self.add_widget(self.result_label)
        
    def on_screen_enter(self):
        self.result_label.text = name + "\n" + test(p1, p2, p3, age)

class RuffierApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Registration(name="1"))
        sm.add_widget(FirstPulse(name="2"))
        sm.add_widget(PhysicWork(name="3"))
        sm.add_widget(PulseSecondThird(name="4"))
        sm.add_widget(Result(name="5"))
        return sm
    
RuffierApp().run()