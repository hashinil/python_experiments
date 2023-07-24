import PySimpleGUI as sg
from convert17 import convert

sg.theme("Black")
label1 = sg.Text("Enter Feet:  ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inch")

convert_btn = sg.Button(size=4, image_source='images/add.png', mouseover_colors="LightBlue2")
convert_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_btn, convert_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    #feet = float(values["feet"])
    #inch = float(values["inch"])
    meter = convert(float(values["feet"]), float(values["inch"]))
    window["output"].update(value=meter)
window.close()