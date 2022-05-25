from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''

<Screen>:
    canvas.before:
        Color:
            rgba: (0.8, 0.5, 1, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    background_normal: ''
    orientation: 'vertical'
    padding: 50

    CustomPanel:
        CustomPanelItem:
            Label:
                text: 'Hello there'


<CustomPanel@TabbedPanel+CustomStrip>:
    do_default_tab: False
    tab_width: self.width
    padding: 0, 0, 0, 0


<CustomPanelHeader@TabbedPanelHeader>:
    text: 'Long Text for a Tab'
    padding: 0, 0


<CustomPanelItem@TabbedPanelItem+CustomPanelHeader>:
    text: 'Hello World Hello World Hello World'
    padding: 0, 0


<CustomStrip@TabbedPanelStrip>:
    canvas:
        Color:
            rgba: (0, 1, 0, 1) # green
        Rectangle:
            size: self.size
            pos: self.pos

''')


class Screen(BoxLayout):
    pass


class TestApp(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    TestApp().run()


#https://stackoverflow.com/questions/56501118/position-tabbed-panel-header-in-kivy
