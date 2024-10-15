import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(350,300)

weight = tkinter.Label(text="Enter Your Weight (Kg)")
weight.pack()

entry_weight = tkinter.Entry(width=20)
entry_weight.pack()

height = tkinter.Label(text="Enter Your Height (Cm)")
height.pack()

entry_height = tkinter.Entry(width=20)
entry_height.pack()
def calculate_bmi():
    height = entry_height.get()
    weight = entry_weight.get()
    bmi_result=tkinter.Label(text="")
    if weight == "" or height == "":
        bmi_result.config(text="Enter both weight and height!")
    else:
        try:
            weight_kg = float(entry_weight.get())
            height_m = float(entry_height.get()) / 100
            bmi = weight_kg / pow(height_m, 2)
            if (bmi <= 16):
                bmi_result.config(text=f"Your BMI {round(bmi),2}. Sevelery Underweight.")

            elif (bmi <= 18.4):
                bmi_result.config(text=f"Your BMI {round(bmi),2}. Underweight.")

            elif (bmi < 25):
                bmi_result.config(text=f"Your BMI {round(bmi),2}. Normal.")
            elif (bmi < 30):
                bmi_result.config(text=f"Your BMI {round(bmi),2}. Overweight.")
            elif (bmi < 35):
                bmi_result.config(text=f"Your BMI {round(bmi),2}. Moderately Obese.")
            elif (bmi < 40):
                bmi_result.config(text=f"Your BMI {round(bmi),2}. Severely Obese.")
            else:
                bmi_result.config(text=f"Your BMI {round(bmi),2}. Morbidly Obese.")
        except:
            bmi_result.config(text="Enter valid value!")
    bmi_result.pack()




calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()




window.mainloop()
