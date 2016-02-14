from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout  

class myApp(App):
	def build(self):
		f=FloatLayout()
		s=Scatter()
		l=Label(text=u"Hello World!",font_size=150)
		f.add_widget(s)
		s.add_widget(l)
		return f
if __name__=="__main__":
	myApp().run()