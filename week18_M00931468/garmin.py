import tkinter as tk
from tkinter import ttk
from settings import *
import customtkinter as ctk



class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        #Main app configuration
        super().__init__(fg_color=GUNMETAL)
        self.title('GARMIN Calorie Calculator')
        window_width = 700
        window_height = 600
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()

        left = int((display_width - window_width) / 2)
        top = int((display_height - window_height) / 2)

        self.bind("<Escape>", lambda event: self.quit())

        self.geometry(f"{window_width}x{window_height}+{left}+{top}")
        self.resizable(False,False)
        
        #Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform= 'a')

        self.result = ctk.StringVar(value= "0")
        font = ctk.CTkFont(family=FONT,size=TITLE_MAIN_SIZE, weight= 'bold')
        result_label = ctk.CTkLabel(self, text= self.result, text_color= CERISE, font=font, textvariable = self.result)
        result_label.grid(column = 0, row = 0 , sticky = "nsew")
        font2 = ctk.CTkFont(family=FONT,size=NORMAL_FONT_SIZE, weight= 'bold')
        result_label = ctk.CTkLabel(self, text= "calories", text_color= CERISE, font=font2)
        result_label.grid(column = 0, row = 1 )

        self.age = ctk.IntVar(value = 65) 
        self.sex = ctk.StringVar(value = "")
        self.weight_unit = ctk.StringVar(value="Kg")
        self.weight = ctk.IntVar(value = 0)
        self.goal = ctk.StringVar(value="Fat Loss")
        self.activity = ctk.StringVar(value="Lightly active")
        AgeFrame(self, self.age)
        GenderFrame(self, self.sex)
        WeightFrame(self,self.weight_unit, self.weight)
        GoalFrame(self, self.goal)
        ActivityFrame(self, self.activity)

       

        submit = ctk.CTkButton(self, text= "Calculate", fg_color=GREEN, text_color= GUNMETAL, hover_color=BEIGE, command= self.calculate)
        submit.grid(column = 0, row = 7 , sticky= "nsew", pady = 5, padx = 5)

       
        self.mainloop()

    def calculate(self, *args):
        weight = self.weight.get()
        activity = self.activity.get()
        gender = self.sex.get()
        if self.weight_unit.get() == "Lb":
            weight = weight * 0.453592

        BMR = weight * 20
        TEF = BMR * 0.1
        # choices = ["Lightly active","Moderately active", "Very active", "Extra active"]
        if activity == "Lightly active":
            EEE = 250
        elif activity == "Moderately active":
            EEE = 325
        elif activity == "Very active":
            EEE = 425
        elif activity == "Extra active":
            EEE = 500

        if activity == "Lightly active":
            NEAT = 250
        elif activity == "Moderately active":
            NEAT = 325
        elif activity == "Very active":
            NEAT = 425
        elif activity == "Extra active":
            NEAT = 500

        TDEE = BMR + TEF + EEE + NEAT

        if gender == "F":
            self.result.set(str(int(TDEE - 100)))

        else: 
            self.result.set(str(int(TDEE + 100)))

        
        
        

class AgeFrame(ctk.CTkFrame):
    def __init__(self, parent, age):
        super().__init__(master=parent, fg_color=GUNMETAL)
        self.grid(column = 0, row = 2, sticky = 'nsew',  padx = 5, pady = 5)
        self.age = age
        #layout
        self.rowconfigure(0, weight=1, uniform= 'b')
        self.columnconfigure(0, weight= 1, uniform= 'b')
        self.columnconfigure(1, weight= 1, uniform= 'b')
        self.columnconfigure(2, weight= 1, uniform= 'b')
        self.columnconfigure(3, weight= 1, uniform= 'b')
        

        #Widget
        #Text
        font = ctk.CTkFont(family=FONT,size=NORMAL_FONT_SIZE, weight= 'bold')
        label = ctk.CTkLabel(self,text="Age:", text_color=ORANGE, font=font)
        label.grid( row = 0, column = 0, sticky = "w")

        #Result
        # age = ctk.IntVar(value = 10)
        age_label =  ctk.CTkLabel(self, text= self.age, text_color=ORANGE, font=font, textvariable = self.age)   
        age_label.grid( row = 0, column = 2)

        #Button
        plus_button = ctk.CTkButton(self,text="+",font=font, text_color=GUNMETAL, fg_color=GREEN, hover_color=BEIGE, corner_radius= 6,
                                    command= lambda: self.update_age("plus") )
        plus_button.grid( row = 0, column = 1, pady = 10, padx = 10, sticky = 'nsew')

        minus_button = ctk.CTkButton(self,text="-",font=font, text_color=GUNMETAL, fg_color=GREEN, hover_color=BEIGE, corner_radius= 6,
                                     command= lambda: self.update_age("minus")  )
        minus_button.grid( row = 0, column = 3, pady = 10, padx = 10, sticky = 'nsew')

    def update_age(self, info):
        if info == "plus":
            self.age.set(self.age.get() + 1)
        else:
            self.age.set(self.age.get() - 1)

class GenderFrame(ctk.CTkFrame):
    def __init__(self, parent, gender):
        super().__init__(master=parent, fg_color=GUNMETAL)
        self.grid(column = 0, row = 3, sticky = 'nsew',  padx = 5, pady = 5)
        self.gender = gender
        #layout
        self.rowconfigure(0, weight=1, uniform= 'b')
        self.columnconfigure(0, weight= 1, uniform= 'b')
        self.columnconfigure(1, weight= 1, uniform= 'b')
        self.columnconfigure(2, weight= 1, uniform= 'b')
        self.columnconfigure(3, weight= 1, uniform= 'b')


        #widget
        #text
        font = ctk.CTkFont(family=FONT,size=NORMAL_FONT_SIZE, weight= 'bold')
        label = ctk.CTkLabel(self,text="Sex:", text_color=ORANGE, font=font)
        label.grid( row = 0, column = 0, sticky = "w")

        

        radiobutton_1 = ctk.CTkRadioButton(self, text="Male",
                                                      variable= self.gender, value="M",fg_color=GREEN, 
                                                      font=font, hover_color= BEIGE,text_color=ORANGE)
        radiobutton_1.grid(row = 0, column = 1)
        radiobutton_2 = ctk.CTkRadioButton(self, text="Female",
                                                      variable= self.gender, value="F",
                                                        fg_color=GREEN, font=font, hover_color= BEIGE, text_color=ORANGE)
        radiobutton_2.grid(row = 0, column = 2, columnspan = 2) 


    def radiobutton_event(self, var):
            print("radiobutton toggled, current value:", var.get())
    
class WeightFrame(ctk.CTkFrame):
    def __init__(self, parent, unit, weight):
        super().__init__(master=parent, fg_color=GUNMETAL, )
        self.grid(column = 0, row = 4 , sticky = 'nsew',  padx = 5, pady = 5)
        self.weight = weight
        self.unit = unit
        #layout
        self.rowconfigure(0, weight=1, uniform= 'b')
        self.columnconfigure(0, weight= 1, uniform= 'b')
        self.columnconfigure(1, weight= 1, uniform= 'b')
        self.columnconfigure(2, weight= 1, uniform= 'b')
        self.columnconfigure(3, weight= 1, uniform= 'b')

        #widget
        #text
        font = ctk.CTkFont(family=FONT,size=NORMAL_FONT_SIZE, weight= 'bold')
        label = ctk.CTkLabel(self,text="Weight:", text_color=ORANGE, font=font)
        label.grid( row = 0, column = 0, sticky = "w")

        #Entry
        weight_entry = ctk.CTkEntry(self, placeholder_text= 0,height=40, border_color=GREEN, textvariable= self.weight)
        weight_entry.grid(row = 0, column = 1, columnspan = 2, sticky = "we")

        #Combobox
        choices = ["Kg","Lb"]
        weight_unit_box = ctk.CTkComboBox(self, values = choices,height=40 , variable= self.unit, text_color='#000000', button_color=GREEN, border_color=GREEN )
        weight_unit_box.grid(row = 0, column = 3, sticky = "ew")

class GoalFrame(ctk.CTkFrame):
    def __init__(self, parent, goal):
        super().__init__(master=parent, fg_color=GUNMETAL)
        self.grid(column = 0, row = 5 , sticky = 'nsew',  padx = 5, pady = 5)
        self.goal = goal

        #layout
        self.rowconfigure(0, weight=1, uniform= 'b')
        self.columnconfigure(0, weight= 1, uniform= 'b')
        self.columnconfigure(1, weight= 1, uniform= 'b')
        self.columnconfigure(2, weight= 1, uniform= 'b')
        self.columnconfigure(3, weight= 1, uniform= 'b')

        #widget
        #text
        font = ctk.CTkFont(family=FONT,size=NORMAL_FONT_SIZE, weight= 'bold')
        label = ctk.CTkLabel(self,text="Goals:", text_color=ORANGE, font=font)
        label.grid( row = 0, column = 0, sticky = "w")

        #entry
        choices = ["Fat Loss","Maintenance", "Muscle Gain"]
        goal_unit_box = ctk.CTkComboBox(self, values = choices,height=40 , variable= goal, text_color='#000000', button_color=GREEN, border_color=GREEN )
        goal_unit_box.grid(row = 0, column = 1, sticky = "ew", columnspan = 3)

class ActivityFrame(ctk.CTkFrame):
    def __init__(self, parent, activity):
        super().__init__(master=parent, fg_color=GUNMETAL)
        self.grid(column = 0, row = 6 , sticky = 'nsew',  padx = 5, pady = 5)

        self.activity  = activity
        #layout
        self.rowconfigure(0, weight=1, uniform= 'b')
        self.columnconfigure(0, weight= 1, uniform= 'b')
        self.columnconfigure(1, weight= 1, uniform= 'b')
        self.columnconfigure(2, weight= 1, uniform= 'b')
        self.columnconfigure(3, weight= 1, uniform= 'b')

        #widget
        #text
        font = ctk.CTkFont(family=FONT,size=NORMAL_FONT_SIZE, weight= 'bold')
        label = ctk.CTkLabel(self,text="Activity Level:", text_color=ORANGE, font=font)
        label.grid( row = 0, column = 0, sticky = "w")

        #entry
        choices = ["Lightly active","Moderately active", "Very active", "Extra active"]
        activity_unit_box = ctk.CTkComboBox(self, values = choices,height=40 , variable= self.activity, text_color='#000000', button_color=GREEN, border_color=GREEN )
        activity_unit_box.grid(row = 0, column = 1, sticky = "ew", columnspan = 3)

if __name__ == "__main__":
    App()