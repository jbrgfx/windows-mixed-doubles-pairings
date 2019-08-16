import PySimpleGUI as sg
import subprocess


# Please check Demo programs for better examples of launchers
def ExecuteCommandSubprocess(command, *args):
    try:
        sp = subprocess.Popen([command, *args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        pass


layout = [
    [sg.Text('Players:\r\tEdit female and/or male participants. \r\tUnmatched females and males will be waitlisted. \r\tWaitlists will not change until the participant lists change. \r\tParticipants are listed in the order they signed up to play. \r\nAssign Courts: \r\tWhen you assign Mixed Doubles courts, Notepad will open: \r\tpaste [Ctrl-V] to see results and then save and print. \r\nYou may assign courts again for another round of mixed doubles.', size=(54, 12))],
    # [sg.Output(size=(88, 20))],
    [sg.Button('Females'), sg.Button('Males'), sg.Button('Assign Courts'), sg.Button('EXIT')],
]

window = sg.Window('Mixed Doubles Rosters').Layout(layout)

# ---===--- Loop taking in user input and using it to call scripts --- #

while True:
    (event, value) = window.Read()
    if event == 'EXIT' or event is None:
        break  # exit button clicked
    if event == 'Females':
        ExecuteCommandSubprocess('notepad', '%USERPROFILE%\\Desktop\\demo\\data\\females.csv')
    elif event == 'Males':
        ExecuteCommandSubprocess('notepad', '%USERPROFILE%\\Desktop\\demo\\data\\males.csv')
    elif event == 'Assign Courts':
            ExecuteCommandSubprocess('%USERPROFILE%\\Desktop\\demo\\run.bat')