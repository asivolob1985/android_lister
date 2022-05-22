import kivy

kivy.require('2.1.0') # replace with your current kivy version !

from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout

class check_box(GridLayout):
    def __init__(self, **kwargs):
        # super function can be used to gain access
        # to inherited methods from a parent or sibling class
        # that has been overwritten in a class object.
        super(check_box, self).__init__(**kwargs)

        # 2 columns in grid layout
        self.cols = 2

        self.count_labels = 10
        for i in range(self.count_labels):
            self.add_widget(TextInput(text='', multiline=False))
           # self.add_widget(Label(text='Текст'))
            self.active = CheckBox(active=False)
            self.add_widget(self.active)

        # Add checkbox, Label and Widget
        # Adding label to screen
        #self.lbl_active = Label(text='Checkbox is on')
        #self.add_widget(self.lbl_active)

        # Attach a callback
        self.active.bind(active=self.on_checkbox_Active)

    # Callback for the checkbox
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active.text = "Checkbox is ON"
            print("Checkbox Checked")
        else:
            self.lbl_active.text = "Checkbox is OFF"
            print("Checkbox unchecked")


# App derived from App class
class CheckBoxApp(App):
    def build(self):
        # build is a method of Kivy's App class used
        # to place widgets onto the GUI.
        return check_box()


# Run the app
if __name__ == '__main__':
    CheckBoxApp().run()
