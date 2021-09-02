from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics.vertex_instructions import (Line, Rectangle)
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import InstructionGroup
from kivy.clock import Clock
from datetime import datetime
import itertools


import weakref
from kivy.core.window import Window
def convert(touch,pos,size):
    pass
class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton,self).__init__(**kwargs)
    # def on_touch_up(self, touch):
    #     # print("mouse down",touch)
    def on_press(self):
        print(self.source)
        img = Image(source = self.source, allow_stretch=True , keep_ratio=False, size_hint=(1,1))
        # self.parent.parent.parent.parent.ids.layout.remove_widget()
        # self.parent.parent.parent.parent.ids.layout.add_widget(img)
        self.parent.parent.parent.ids.layout.ids.photo.source=self.source
        # print(img.source)

        # self.ids.layout.add_widget(photo)
    pass
def on_touch_down(touch):
         return(touch)




class butt(Button):
    def __init__(self,numbers, coords, **kwargs):
        super(butt, self).__init__(**kwargs)
        self.numbers = numbers
        self.coords = coords
    def find_index(self):
        for i , button in enumerate(self.parent.parent.parent.parent.ids.layout.ids.photo.buttons):
            if button.numbers == self.numbers:
                return i


    def on_press(self):
        print(self.numbers)
        line = Line(points = self.coords, width=3)
        # self.parent.parent.parent.parent.ids.layout.ids.photo.canvas.clear()
        self.parent.parent.parent.parent.ids.layout.ids.photo.canvas.remove(self.parent.parent.parent.parent.ids.layout.ids.photo.instructions[self.find_index()])
        # print(self.parent.ids)
        #     # (self.parent.parent.parent.parent.ids.photo.instructions[self.find_index()])
        self.parent.parent.parent.parent.ids.layout.ids.photo.table.pop(self.find_index())
        self.parent.parent.parent.parent.ids.layout.ids.photo.instructions.pop(self.find_index())
        print(self.parent.parent.parent.parent.ids.layout.ids.photo.table)
        print(self.parent.parent.parent.parent.ids.layout.ids.photo.buttons)
        print(self.parent.parent.parent.parent.ids.layout.ids.photo.instructions)
        self.parent.parent.parent.parent.ids.layout.ids.photo.buttons.pop(self.find_index())
        self.parent.parent.parent.parent.ids.objects.remove_widget(self)
        # self.parent.remove_widget()


class Frame():
    id_iter = itertools.count()
    def __init__(self,coords,name):
        self.coords = coords
        self.name = name
        self.id = next(self.id_iter)


class Draw(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line = [0,0,0,0,0,0,0,0,0,0]
        self.table=[]
        self.instructions = []
        self.buttons = []


    def remove(self,number):
        item = Line(points=self.table[number].coords)
        print(self.canvas.get_group(Line))
        del self.table[number]


    def on_touch_down(self,touch):
        # if touch.x
        if (touch.x > self.pos[0] and touch.x< self.pos[0]+self.size[0]):
            self.line[0] = touch.x
            self.line[1] = touch.y
            self.table.append(Frame(self.line,"name"))
            self.buttons.append(butt(text=str(self.table[-1].id),size_hint=(1,None),width=300, numbers = self.table[-1].id, coords = self.table[-1].coords))
            self.parent.parent.ids.objects.add_widget(self.buttons[-1])
            with self.canvas:
                Color(0,0,1,1)
                # touch.ud["line"]=Line(points=(touch.x,touch.y,touch.x,touch.y,touch.x,touch.y,touch.x,touch.y), closed =True)


    def on_touch_move(self, touch):
        if (touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]):
            self.line[2] = self.line[0]
            self.line[3] = touch.y
            self.line[4] = touch.x
            self.line[5] = touch.y
            self.line[6] = touch.x
            self.line[7] = self.line[1]
            self.line[8] = self.line[0]
            self.line[9] = self.line[1]
            # with self.canvas:
            #     Line(points = self.line, closed=True)


    def on_touch_up(self, touch):
        if (touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]):
            if self.table:
                self.instructions.append(Line(points=self.table[-1].coords))
                self.canvas.add(self.instructions[-1])
            print(self.table)
        #dodajemy wspolrzedne do tablicy jakiejs ta se tak o
                # touch.ud["line"].points[2] = touch.x
                # touch.ud["line"].points[3] = touch.ud["line"].points[1]
                # touch.ud["line"].points[4] = touch.ud["line"].points[0]
                # touch.ud["line"].points[5] = touch.y
                # print(touch.ud["line"].points)
                # touch.ud["line"].points[6] = touch.x
                # touch.ud["line"].points[7] = touch.y


class MainWidget(BoxLayout):
    app = App.get_running_app()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.names = []
        self.current_calss = ""
    def selected(self,removeFiles):
        self.add(removeFiles)
    def getClass(self,text):
        self.names.append(text)
        self.ids.list3.values.append(text)
    def spinner_clicked(self,text):
        self.current_calss = text
        print(self.current_calss)


    def getPoints(self):
        pass
    def remove(self):
        self.ids.layout.remove_widget(self.ids.select)
        self.ids.layout.remove_widget(self.ids.filechooser)
        # img = Image(source = '' , allow_stretch=True , keep_ratio=False, size_hint=(1,1))
        # self.ids.layout.add_widget(img)
        # self.ids.layout.ids['photo'] = weakref.ref(img)
        picture = Draw(source='',allow_stretch=True , keep_ratio=False, size_hint=(1,1))
        self.ids.layout.add_widget(picture)
        self.ids.layout.ids['photo'] = weakref.ref(picture)
        # self.draw()
        # img = Image(source='')
        # self.ids.layout.add_widget(img)
    # def btn(self):
    #     self.remove(
    #     print("lessgo")
    #     self.remove_widget(self)
    def append(self,source):
        photo = Image(source=source)
        self.ids.layout.add_widget(photo)
    def press(self):
        photo = Image(source=self.source)
        print(photo.source)
        self.ids.layout.add_widget(photo)
    def add(self,list):
        for i,source in enumerate(list):
            try:
                a = ImageButton(source=source , allow_stretch=True , keep_ratio=False, size_hint=(0.25,None))
                self.ids.images.add_widget(a)
                print("added " +str(source))

            except:
                pass
class TheApp(App):
    def build(self):
        root = MainWidget()
        return root

# def addImg(target,list):
#     for i, source in enumerate(list):
#         img = Image(source=source)
#         print(target)
#         print(img)
#         target.add_widget(img)


if __name__== "__main__":
    TheApp().run()