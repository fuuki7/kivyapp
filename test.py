from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (1280, 720)


class MyWidget(Widget):
    pass


class MyApp(App):
    title = "My Application"

    def build(self):
        return Label(text="Hello World!")


if __name__ == "__main__":
    MyApp().run()
