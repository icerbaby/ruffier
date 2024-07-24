from kivy.clock import Clock
from kivy.uix.label import Label

from kivy.properties import BooleanProperty

class Timer(Label):
    finished = BooleanProperty(False)
    
    def __init__(self, total_seconds, start_text="Залишилося секунд: ", rest_text="Відпочивайте: ",color = (1, 0, 0.5, 1), **kwargs):
        
        self.total_seconds = total_seconds
        self.current_seconds = total_seconds
        self.start_text = start_text
        self.rest_text = rest_text
        self.finished = False
        self.color = color
        
        super().__init__(text=self.start_text + str(self.current_seconds), **kwargs)
        
    def start(self):
        Clock.schedule_interval(self.change, 1)
        
    def restart(self, total_seconds=None):
        if total_seconds is not None:
            self.total_seconds = total_seconds
        self.current_seconds = 0
        self.text = self.start_text + str(self.current_seconds)
        self.finished = False
        self.start()
    

    
    def change(self, *args):
        self.current_seconds -= 1
        self.text = self.start_text + str(self.current_seconds)
        if self.current_seconds == 0:
            self.finished = True
            return False
        
