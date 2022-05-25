import kivy
from kivy.app import App


kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)

kivy.require('1.9.0')

from kivy.config import Config
Config.set('graphics', 'width', '441')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)

from where import run
from sort import start
from pypltmonths import plotGraphTotalSpentPerMonth
from pypltdates import plotGraphTotalSpentPerDay

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.text import LabelBase
import time

from kivy.core.window import Window
Window.clearcolor = (0.3, 0.5, 0.2, 0.8)

class CameraClick(BoxLayout):
    def capture(self):
            camera = self.ids['camera']
            camera.export_to_png("icons/capture.png")
            print("Captured")
            analysis()


'''
"Schoolfed is an easy to use shopping and budgeting app for students.\n Many students, including our team, struggle with budgeting.
And especially in this modern age, where you just swipe a card and go,
money may seem to disappear out of wallets like some sort of black magic.
Money management truly is a difficult skill to learn for many,
which is why we created Schoolfed. \n
Directions: Take or upload an image of a reciept in the camera's tab
by pressing play and capture. Then analyze the receipt with 3
different graphs that clearly show your spending. Furthermore,
the sort tab shows how much you spent at each store in small to large order!"
'''

Builder.load_string("""
<ScreenOne>:

    FloatLayout:
        Image:
            source: 'icons/Schoolfed.png'
            keep_ratio: False
            allow_stretch: True
            opacity: 0.8
            size_hint: 0.55, 0.4
            pos_hint: {'center_x': 0.5, 'center_y': 0.75}

        Label:
			id: name_label
			text: "By Jeffrey Lam, Linden Zheng, and Linda Xue"
            font_name: "Squad"
            pos: 0, 0
			font_size: 16
            keep_ratio: False
            allow_stretch: True

    BoxLayout:


        Button:
            background_normal: 'icons/cameraicon.png'
            size: 147, 50
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
        Button:
            background_normal: 'icons/graphicon.png'
            #text: "Graphs"
            background_color: 0, 1, 0, 0.8
            size: 147, 50
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_three'
        Button:
            background_normal: 'icons/listicon.png'
            background_color: 0, 1, 0, 1
            size: 147, 50
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_four'

<ScreenTwo>:
    FloatLayout:
        Button:
            background_normal: 'icons/backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None

            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'
        Camera:
            id: camera
            resolution: (640, 480)
            play: False
            size: 640, 480
    BoxLayout:

        ToggleButton:
            text: 'Play'
            on_press: camera.play = not camera.play
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Capture'
            size_hint_y: None
            height: '48dp'
            on_press: root.capture()
        Button:
            text: 'Select Image'
            size_hint_y: None
            height: '48dp'
            on_press: root.imageselect()

<ScreenThree>:
    FloatLayout:
        Button:

            background_normal: 'icons/backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'
        Button:
            text: "Graph by Store"
            font_name: "Squad"
            pos: 75, 100
            size: 291, 75
            size_hint: None, None
            background_color: 0, 1, 0, 1
            on_press:
                root.runGraph()
        Button:
            #height: 30
            font_name: "Squad"
            pos: 75, 350
            size: 291, 75
            size_hint: None, None
            background_color: 0, 1, 0, 0.8
            text: "Graph by Month"
            on_press:
                root.runMonth()

        Button:
        #    height: 30
            font_name: "Squad"
            pos: 75, 600
            size: 291, 75
            size_hint: None, None
            background_color: 0, 1, 0, 0.5
            text: "Graph by Day"
            on_press:
                root.runDay()


<ScreenFour>:
    FloatLayout:
        Button:
            background_normal: 'icons/backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'
        Button:
            id: sort_but
            text: "Sort"
            font_name: "Squad"
            pos: 100, 100
            size: 241, 50
            background_color: 0, 1, 0, 1
            size_hint: None, None
            on_press:
                root.runSort()



		Label:
			id: name_label
			text: "Least to Most Spent at Stores"
            font_name: "Squad"
            pos: 5, 100
			font_size: 22



""")

LabelBase.register(name='Squad',
                   fn_regular='fonts/Squad.ttf')
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):

    pass
       # Replace the given image source value:


class ScreenTwo(Screen):
    def runCamera(self):
        print("hi")
    def capture(self):

        camera = self.ids['camera']
        camera.export_to_png("icons/capture.png")
        print("Captured")
        analysis()


    def imageselect(self):
        from selectionanalysis import selectImageandAnalyze
        selectImageandAnalyze()


class ScreenThree(Screen):
    def runGraph(self):
        run()
    def runMonth(self):
        plotGraphTotalSpentPerMonth(1)
    def runDay(self):
        plotGraphTotalSpentPerDay()

string = ""
class ScreenFour(Screen):
    def runSort(self):
        x,y,total = start()
        print(len(x))
        global string
        for i in range(len(x)):

            string = string + x[i] +" : " + str(y[i]) + "\n"
        string = string + "Total: " + str(total)
        self.ids.name_label.text = string
        self.ids.sort_but.disabled = True






screen_manager = ScreenManager()


screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))

#screen_manager.current = "School Fed"

class ScreenApp(App):
    icon = "icons/Schoolfed.png"
    title = 'School Fed'
    def build(self):
        '''self.window = GridLayout()

        self.window.add_widget()'''

        return screen_manager



# run the app
sample_app = ScreenApp()
sample_app.run()
