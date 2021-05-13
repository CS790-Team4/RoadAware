from keras.models import load_model
import PIL
import numpy as np
#Loading the ml model for GUI - Snigdha
#
#
#
model = load_model('RoadAware_ML_model.h5')
#dictionary to label all traffic signs class.
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing vehicles over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Vehicle > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing vehincle > 3.5 tons' }
#
#
#
#

from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial
from kivy.clock import Clock


class WelcomePage(GridLayout):
    def __init__(self,**kwargs):
        super(WelcomePage,self).__init__(**kwargs)
        
        self.cols = 1
        self.top_grid = GridLayout()
        self.add_widget(Label(text = 'RoadAware',
                              font_size = 40))
        self.top_grid.cols = 1
        
        self.upload = Button(text = "Upload a picture",
                                 background_normal = '',
                               background_color = (0.14,0.63,0.93,1),
                               size_hint = (0.6,0.6), width=900,
                               font_size = 30)
        self.upload.bind(on_press = self.upload_button)
        self.top_grid.add_widget(self.upload)
        
        self.top_grid.add_widget(Label(size_hint_y = None, height = 30))
        
        self.takepic = Button(text = "Take a picture",
                                 background_normal = '',
                               background_color = (0.14,0.63,0.93,1),
                               size_hint = (0.6,0.6), width=900,
                               font_size = 30)
        self.takepic.bind(on_press = self.takepic_button)
        self.top_grid.add_widget(self.takepic)
        
        self.add_widget(self.top_grid)
    
    def upload_button(self,instance):
        ra_app.screen_manager.current = 'Upload'
        
    def takepic_button(self,instance):
        ra_app.screen_manager.current = 'Take_pic'


class UploadPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        
        self.top_grid = GridLayout()
        self.top_grid.cols = 1

        self.img = Image(source = "")
        self.add_widget(self.img)
        self.pred_label = Label(text = '',size_hint_y = None, height = 30, font_size = 30)
        self.add_widget(self.pred_label)
        
        self.filechoo = FileChooserIconView(rootpath = "/Users")
        
        self.add_widget(self.filechoo)
        
        #self.add_widget(Label(text = 'Upload a picture',
                             # font_size = 40))
        self.clas = Button(text = "Classify          ",
                                 background_normal = '',
                               background_color = (0.14,0.63,0.93,1),
                               size_hint = (0.6,0.6), width=900,
                               font_size = 30)
        self.clas.bind(on_press = self.on_classify)
        self.top_grid.add_widget(self.clas)
        self.top_grid.add_widget(Label(size_hint_y = None, height = 30))
        
        self.filechoo.bind(selection = self.on_mouse_select)
        self.back = Button(text = "Back          ",
                                 background_normal = '',
                               background_color = (0.14,0.63,0.93,1),
                               size_hint = (0.6,0.6), width=900,
                               font_size = 30)
        self.back.bind(on_press = self.back_button)
        self.top_grid.add_widget(self.back)
        
        self.add_widget(self.top_grid)
        
    def back_button(self,instance):
        ra_app.screen_manager.current = 'Welcome'
    
    def on_mouse_select(self, obj, val):
        #print(obj)
        #print(self.filechoo.selection[0])
        self.pred_label.text = ''
        if self.filechoo.selection:
            self.img.source = str(self.filechoo.selection[0])
        else:
            self.img.source = ''
        return
    
    def on_touch_up(self,touch):
        if self.filechoo.selection:
            self.img.source = str(self.filechoo.selection[0])
        return super().on_touch_up(touch)
    
    def on_classify(self,instance):
        try:
            file_path = self.img.source
            image = PIL.Image.open(file_path)
            image = image.resize((30,30))
            image = np.expand_dims(image, axis=0)
            image = np.array(image)
        #index = np.argmax(model.predict(image), axis=-1)
            predic = model.predict([image])
            pred = int(np.argmax(predic, axis=-1))
            if(predic[0][pred]<1):
                sign = 'This is not a road sign or the picture is too distorted'
            else:
                sign = classes[pred+1]
            print(sign)
            
        except:
            sign = "Please choose .jpg file"
        self.pred_label.text = sign


class TakepicPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #app= App.get_running_app()
        self.cols = 1
        #self.add_widget(Label(text = 'Take a picture',
                              #font_size = 40))
        self.cameraObject = Camera(play = False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (600,600)
        self.cameraClick = Button(text = "Take Photo")
        self.cameraClick.size_hint = (0.5,0.2)
        self.cameraClick.pos_hint = {'x':0.25,'y':0.75}
        self.cameraClick.bind(on_press= self.onCamClick)
        self.add_widget(self.cameraObject)
        self.add_widget(self.cameraClick)
        
        
    
    def onCamClick(self, instance):
        print("Taking picture")
        Clock.schedule_once(partial(self.cameraObject.export_to_png,"/selfie.png"),0.5 )
        im1 = PIL.Image.open("/selfie.png")
        im1 = im1.convert('RGB')
        im1.save("/selfie.jpg")
        #self.cameraObject.export_to_png("/selfie.png")
        
        ra_app.screen_manager.current = 'Upload'
    

class RoadAwareApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Initial, welcome screen (we use passed in name to activate screen)
        # First create a page, then a new screen, add page to screen and screen to screen manager
        self.welcome_page = WelcomePage()
        screen = Screen(name='Welcome')
        screen.add_widget(self.welcome_page)
        self.screen_manager.add_widget(screen)

        # Upload page
        self.up_page = UploadPage()
        screen = Screen(name='Upload')
        screen.add_widget(self.up_page)
        self.screen_manager.add_widget(screen)
        
        # Take picture page
        self.takepic_page = TakepicPage()
        screen = Screen(name='Take_pic')
        screen.add_widget(self.takepic_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == '__main__':
    ra_app = RoadAwareApp()
    ra_app.run()
