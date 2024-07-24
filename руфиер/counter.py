from kivy.uix.label import Label

class Counter(Label):
    def __init__(self, total, text, **kwargs):
        
        self.total = total
        self.current = 1  # !!!!!!!
        self.idk = 30
        self.counter_text = text
        if self.current == 1:
            super().__init__(text=self.counter_text + ": " + str(self.idk), **kwargs)
        else:
            super().__init__(text=self.counter_text + ": " + str(self.current) - str(self.idk), **kwargs)
        
    def next(self, *args):
        self.current -= 1 # !!!!!!!
        self.text = self.counter_text + ": " + str(max(0, self.total + self.current))
        
        