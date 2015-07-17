from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout

class GuiController(Widget):
    def __init__(self):
        super(GuiController, self).__init__()


class NumberTextInput(TextInput):
    def __init__(self, **kwargs):
        super(NumberTextInput, self).__init__(**kwargs)
    def some_Act(self):
        pass

    def insert_text(self, substring, from_undo=False):
        if substring.isdigit() and len(self.text) < 2:
            return super(NumberTextInput, self).insert_text(substring, from_undo = from_undo)
        else:
            pass

    def do_backspace(self, from_undo=False, mode='bkspc'):
        pass

    def do_undo(self):
        pass
    # def on_text_validate(self): #fires when user hits enter in single line textinput
    #     t_input = NumberTextInput()
    #     t_input_up = t_input.ids.input_up
    #     t_input_down = t_input.ids.input_down
    #     if t_input_up.focus == True:
    #         t_input_up.focus = BooleanProperty(False)
    #         t_input_down.focus = BooleanProperty(True)






class GuiApp(App):

    def build(self):
        return GuiController()

if __name__ == '__main__':
    GuiApp().run()