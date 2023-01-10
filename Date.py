import PySimpleGUI as sg
import datetime

layout = [
    [sg.Text("enter the date lol (YY/MM/DD):", font=("Arial", 16, "bold"))],
    [sg.Input()],
    [sg.Button("Submit"), sg.Exit()]
]


window = sg.Window("What's the day????", layout)

while True:
    event, values = window.Read()

    if event in (None, "Exit"):
        break

    date_str = values[0]

    year, day, month = map(int, date_str.split("/"))

    date = datetime.datetime(year, day, month)

    day_of_week = date.weekday()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    message = f"The day of the week is: {days[day_of_week]}"

    sg.popup(message)

window.Close()
