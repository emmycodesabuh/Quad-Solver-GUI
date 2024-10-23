from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
import math as m

# Set window background color
Window.clearcolor = get_color_from_hex('#1c1c1c')



class UI(BoxLayout):
	
    txt = ""
    def preview(self):
    	a = self.ids.a.text
    	b = self.ids.b.text
    	c = self.ids.c.text
    	
    	# check if data is provided
    	if a == "" and b == "" and c == "":
    		self.show_popup("Enter Values a, b and c to preview and calculate")
    	else:
    	
    		# Display equation
    		B, C = "", ""
    		
    		if int(b) > 0:
    			B = "+"
    		else:
    			B = "-"
    		if int(c) > 0:
    			C = "+"
    		else:
    			C = "-"
    	
    		#print the eqn using the absolute values of variables to eliminate unwanted -ve data forms
    		if int(a) == 1:
    			#using the format ax²+bx+c = 0
    			txt1 = f"x² {B} {int(m.fabs(int(b)))}x {C} {int(m.fabs(int(c)))} = 0"
    		elif int(a) > 1:
    			txt1 = f"{int(a)}x² {B} {int(m.fabs(int(b)))}x {C} {int(m.fabs(int(c)))} = 0"
    		elif int(a) < 1:
    			txt1 = f"{int(a)}x² {B} {int(m.fabs(int(b)))}x {C} {int(m.fabs(int(c)))} = 0"
    		txt = txt1
    		print(txt)
    	
    		self.ids.preview.text = txt
    
    def calculate(self):
    	a = self.ids.a.text
    	b = self.ids.b.text
    	c = self.ids.c.text
    	
    	# Let D = (b²-4ac)
    	# x = (-b ± √b²-4ac)/2a
    	D = (m.pow(int(b), 2) - (4*int(a)*int(c)))
    	# if D > 0, roots are real (valid)
    	if D > 0:
    		x1 = ((-int(b) + m.sqrt(D)) / (2*int(a)))
    		x2 = ((-int(b) - m.sqrt(D)) / (2*int(a)))
    		
    		self.show_popup(f"\n roots are {int(x1)} or {int(x2)}")
    	# if D = 0, roots are real (valid)
    	# x = -b/2a
    	elif D == 0:
    		x = (-int(b) / (2*int(a)))
    		self.show_popup(f"\n root is {int(x)}")
    	# if D < 0, roots are unreal (invalid)
    	else:
    		self.show_popup("\nInvalid Expression\nCannot compute unreal roots")

    
    def show_popup(self, message):
        popup = Popup(
            title='Login Result',
            content=Label(text=message),
            size_hint=(None, None),
            size=(500, 250)
        )
        popup.open()


class QuadSolverApp(App):
    def build(self):
        return UI()

if __name__ == '__main__':
    QuadSolverApp().run()
