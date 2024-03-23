import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDRectangleFlatButton
from math import floor


class MyLayout(MDBoxLayout):
    mgr=ObjectProperty(None)
    def start_call(self):
        self.Min=1
        self.Max=1000
        self.N=(self.Max-self.Min)+1
        self.Numbers=[x for x in range(self.N+1)]
        self.guess=floor(self.Min+self.Max)/2
        self.No=1
        self.mgr.current='screen1'
        self.mgr.transition.direction='left'
        self.ids.mgr.screen1.l1.text='Is your number Greater, Equal or Less than'
        self.ids.mgr.screen1.la.text=str(int(self.guess))

    def less(self):
        self.ids.mgr.screen1.l2.text='Is your number Greater, Equal or Less than'
        self.Max=self.guess
        self.guess=floor(self.Min+self.Max)/2
        self.ids.mgr.screen1.lb.text=str(int(self.guess))
        self.No +=1

    def greater(self):
        self.ids.mgr.screen1.l2.text='Is your number Greater, Equal or Less than'
        self.Min=self.guess
        self.guess=floor(self.Min+self.Max)/2
        self.ids.mgr.screen1.lb.text=str(int(self.guess))
        self.No +=1

    def equal(self):
        self.ids.mgr.screen2.number.text=str(int(self.guess))
        self.ids.mgr.screen2.guess_number.text=str(int(self.No))
        self.mgr.current='screen2'
        self.mgr.transition.direction='left'

    def again(self):
        self.Min=1
        self.Max=1000
        self.N=(self.Max-self.Min)+1
        self.Numbers=[x for x in range(self.N+1)]
        self.guess=floor(self.Min+self.Max)/2
        self.No=1
        self.ids.mgr.screen1.l2.text=''
        self.ids.mgr.screen1.lb.text=''
        self.mgr.current='screen1'
        self.mgr.transition.direction='right'
        
        
        

kv='''
MyLayout:
    orientation:'vertical'
    mgr:mgr
    ScreenManager:
        id:mgr
        wellcover:wellcover
        screen1:screen1
        screen2:screen2
##################################
        Screen:
            id:wellcover
            name:'wellcover'
            MDBoxLayout:
                orientation:'vertical'
                spacing: dp(10)
                padding:dp(10)
                AnchorLayout:
                    size_hint_y:None
                    height:cover.height
                    Image:
                        id:cover
                        source:'wellcome.jpg'
                        size_hint:None,None
                        size:'500dp','500dp'
                MDFillRoundFlatButton:
                    text:'start'
                    pos_hint:{'center_x': 0.5,'center_y': 0.5}
                    on_press:root.start_call()
######### SC1 #########################################
        Screen:
            id:screen1
            name:'screen1'
            l1:l1
            l2:l2
            la:la
            lb:lb
            MDBoxLayout:
                orientation:'vertical'
                spacing: dp(10)
                padding:dp(10)
                AnchorLayout:
                    size_hint_y:None
                    height:gg.height
                    Image:
                        id:gg
                        source:'gg.PNG'
                        size_hint:None,None
                        size:'350dp','350dp'
                MDBoxLayout:
                    orientation:'horizontal'
                    spacing: dp(10)
                    padding:dp(10)
                    MDLabel:
                        text:''
                        id:l1
                        bold:True
                    MDLabel:
                        text:''
                        theme_text_color: "Custom"
                        text_color: 0, 0.8, 0.2, 1
                        id:la
                        bold:True
                MDBoxLayout:
                    orientation:'horizontal'
                    spacing: dp(10)
                    padding:dp(10)
                    MDLabel:
                        text:''
                        id:l2
                    MDLabel:
                        text:''
                        id:lb
                        theme_text_color: "Custom"
                        text_color: 1, 0, 0, 1
                        bold:True
               
                
                MDBoxLayout:
                    orientation:'horizontal'
                    spacing: dp(10)
                    padding:dp(10)
                    MDFillRoundFlatButton:
                        text:'Less'
                        on_press:
                            root.less()
                            root.mgr.screen1.l2.theme_text_color="Custom"
                            root.mgr.screen1.l2.text_color=1,0,0,1
                            root.mgr.screen1.lb.text_color=1,0,0,1
                            root.mgr.screen1.l2.bold=True
                    MDRoundFlatButton:
                        text:'Equal!'
                        on_press:root.equal()
                    MDFillRoundFlatButton:
                        text:'Greater'
                        on_press:
                            root.greater()
                            root.mgr.screen1.l2.bold=True
                            root.mgr.screen1.l2.theme_text_color="Custom"
                            root.mgr.screen1.l2.text_color=0,0,1,1
                            root.mgr.screen1.lb.text_color=0,0,1,1
######### SC 2 ###################################################
        Screen:
            id:screen2
            name:'screen2'
            guess_number:guess_number
            number:number
            MDBoxLayout:
                orientation:'vertical'
                spacing: dp(15)
                padding:dp(15)
                MDLabel:
                    text:'Congratulations!'
                    font_size:'45sp'
                    halign:'center'
                AnchorLayout:
                    size_hint_y:None
                    height:ff.height
                    Image:
                        id:ff
                        source:'ff.jpg'
                        size_hint:None,None
                        size:'250dp','250dp'
                MDBoxLayout:
                    orientation:'horizontal'
                    spacing: dp(10)
                    padding:dp(10)
                    MDLabel:
                        text:'Your number is '
                        italic:True
                      
                        
                    MDLabel:
                        text:''
                        theme_text_color: "Custom"
                        text_color: 1, 0, 0, 1
                        bold:True
                        id:number
                    MDLabel:
                        text:''
                    MDLabel:
                        text:''
                MDBoxLayout:
                    orientation:'horizontal'
                    spacing: dp(5)
                    padding:dp(5)
                    MDLabel:
                        text:'I found it in '
                        italic:True
                    MDLabel:
                        text:''
                        id:guess_number
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        bold:True
                    MDLabel:
                        text:'guess'
                        italic:True
                    MDLabel:
                        text:''
                    MDLabel:
                        text:''
                    MDLabel:
                        text:''
                    MDLabel:
                        text:''
                    MDLabel:
                        text:''
                MDBoxLayout:
                    orientation:'horizontal'
                    spacing: dp(10)
                    padding:dp(10)
                    MDRoundFlatButton:
                        text:'Play again!'
                        on_press:root.again()
                    MDFillRoundFlatButton:
                        text:'Exit'
                        on_release:app.get_running_app().stop()
                    MDLabel:
                        text:''
                    MDLabel:
                        text:'Designed by M.J.Shadfar'
                        font_size: "10sp"
                        italic:True
                    
                    
'''






#def Guess(Min,Max,guess,No):
    #if Min==Max:
       # return
    #else:
      #  op=input('IS your number (G)reater, (E)qual or (L)ess than %i: ' % guess)
      #  if (op=='E' or op=='e'):
        ##    print('I found your number in %i guess and it is %i' % (No,guess))
        #    Min=Max
         #   Guess(Min,Max,guess,No)
      #  elif (op=='G' or op=='g'):
         #   Min=guess
         #   guess=floor(Min+Max)/2
         #   No +=1
          #  Guess(Min,Max,guess,No)
       # elif (op=='L' or op=='l'):
         #   Max=guess
         ##   guess=floor(Min+Max)/2
          #  No +=1
          #  Guess(Min,Max,guess,No)
       # else:
         #   print('Error in data')



#Guess(Min,Max,guess,No)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Blue'
        
        return Builder.load_string(kv)


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
MainApp().run()


