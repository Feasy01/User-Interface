from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors import ButtonBehavior
import weakref

class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton,self).__init__(**kwargs)
    # def on_touch_up(self, touch):
    #     # print("mouse down",touch)
    def on_press(self):
        print(self.source)
        img = Image(source = self.source, allow_stretch=True , keep_ratio=False, size_hint=(1,1))
        print(self.parent.parent)
        # self.parent.parent.parent.parent.ids.layout.remove_
        # self.parent.parent.parent.parent.ids.layout.add_widget(img)
        self.parent.parent.parent.parent.ids.layout.ids.photo.source=self.source
        # print(img.source)

        # self.ids.layout.add_widget(photo)
    pass
def on_touch_down(touch):
         print(touch)
class MainWidget(BoxLayout):
    app = App.get_running_app()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def draw(self):
    def selected(self,removeFiles):
        self.add(removeFiles)
    def remove(self):
        self.ids.layout.remove_widget(self.ids.select)
        self.ids.layout.remove_widget(self.ids.filechooser)
        img = Image(source = '' , allow_stretch=True , keep_ratio=False, size_hint=(1,1))
        self.ids.layout.add_widget(img)
        self.ids.layout.ids['photo'] = weakref.ref(img)
        print(self.ids.layout.ids)
        # img = Image(source='')
        # self.ids.layout.add_widget(img)
    # def btn(self):
    #     self.remove(
    #     print("lessgo")
    #     self.remove_widget(self)
    def append(self,source):
        print(source)
        photo = Image(source=source)
        self.ids.layout.add_widget(photo)
    def press(self):
        photo = Image(source=self.source)
        print(photo.source)
        self.ids.layout.add_widget(photo)
    def add(self,list):
        print(list)
        for i,source in enumerate(list):
            try:
                a = ImageButton(source=source , allow_stretch=True , keep_ratio=False, size_hint=(None,None))
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