import PySimpleGUI as sg
from discord_webhook import DiscordWebhook

layout = [  [sg.Text("Insert webhook url")],
            [sg.Input()],
            [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window('Discord Webhook Tool by Tems', layout)     

event, url = window.read()
window.close()
if event == 'Quit':
    window.close()
    quit()

def send():
    second = [  [sg.Text("Message")],     
            [sg.Input()],
            [sg.Button('Ok'), sg.Button('Quit')]]


    tt = sg.Window('Discord Webhook Tool by Tems', second)

    event, mess = tt.read()
    if event == 'Quit':
        tt.close()
        quit()
    print(mess)
    webhook = DiscordWebhook(url=url[0], content = mess[0] )
    response = webhook.execute()
    tt.close()
while True:
    send()
