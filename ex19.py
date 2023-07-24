import PySimpleGUI as sg
from convert17 import convert

label1 = sg.Text("Enter Feet:  ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inch")

convert_btn = sg.Button("Convert", key="convert")
exit_btn = sg.Button("Exit", key="exit")
convert_label = sg.Text(key="output", text_color="green")

col1 = sg.Column([[label1], [label2], [convert_btn]])
col2 = sg.Column([[input1], [input2], [exit_btn, convert_label]])
col3 = sg.Column([[convert_label]])

window = sg.Window("File Compressor",
                   layout=[[col1, col2]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'convert':
            meter = convert(float(values["feet"]), float(values["inch"]))
            window["output"].update(value=meter)
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()