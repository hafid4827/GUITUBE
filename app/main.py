from PySimpleGUI import (
    Window,
    Text,
    Input,
    Button,
    WINDOW_CLOSED
)
from pytube import YouTube

from os.path import abspath
from threading import Thread


UPPS = ''


def YTDonwloader(url: str, name: str = ''):
    """ yt = YouTube(url).streams.filter(file_extension='mp4').first() """
    global UPPS
    try:
        yt = YouTube(url).streams.filter(
            progressive=True,
            file_extension='mp4'
        ).first()
        if name != '':
            yt.download(output_path=abspath('./videos'), filename=name)
        else:
            yt.download(output_path=abspath('./videos'))
    except:
        UPPS = 'ups error'


def Layout():
    return [
        [Text(text='Welcome')],
        [Text(text='URL:'), Input(key='-url-')],
        [Text(text='msg:', key='-msg-')],
        [Button(button_text='Donwloader', key='-btnd-')]
    ]


def Exe():
    global UPPS
    layout = Layout()
    window = Window('GUITUBE', layout)
    while True:
        event, value = window.read()

        if event == '-btnd-':
            url = value['-url-']
            if url != '':
                Thread(target=YTDonwloader, args=(url,)).start()
                window['-msg-'].update('')
            else:
                if UPPS != '':
                    window['-msg-'].update(UPPS)
                else:
                    window['-msg-'].update('el campo esta vacio')
            window['-url-'].update('')

        if event == WINDOW_CLOSED:
            break


if __name__ == '__main__':
    Exe()
