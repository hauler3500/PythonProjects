import PySimpleGUI as sg
from random import randint
import win32com.client
from time import sleep





def determineWinner(p,c):
    winner = ''
    
    if p == 'Rock':
        if c == 'Scissors':
            winner = 'Player'
        elif c == 'Paper':
            winner = 'Computer'
        else:
            winner = 'Tie!'

    if p == 'Paper':
        if c == 'Scissors':
            winner = 'Computer'
        elif c == 'Rock':
            winner = 'Player'
        else:
            winner = 'Tie!'

    if p == 'Scissors':
        if c == 'Rock':
            winner = "Computer"
        elif c == 'Paper':
            winner = "Player"
        else:
            winner = "Tie!"
    print(c)
    print(winner)
    return [c,winner]
    
        
    

    


def getCompChoice(p):
    r = randint(1,3)
    comp = ''
    if r == 1:
        comp = 'Rock'
    elif r == 2:
        comp = 'Paper'
    else:
        comp = 'Scissors'
    
    results = determineWinner(p,comp)    
    return results



gamesPlayed = 0
gamesWon = 0
sg.theme('GreenTan') # give our window a spiffy set of colors

layout = [[sg.Text('Your Choice: '),sg.Text(key='-USER-', size=(40, 1))],
          [sg.Text('Computer Choice: '), sg.Text(key='-COMP-', size=(40, 1))],
          [sg.Text('Winner is: '), sg.Text(key='-WINNER-', size=(40, 1))],
          [sg.Button('Rock',size=(15,5)), sg.Button('Paper',size=(15,5)), sg.Button('Scissors',size=(15,5))],
          [sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0])),sg.Text(' | '),sg.Text('Games Played: '),sg.Text('0',key='-GP-'),sg.Text('Games Won: '),sg.Text('0',key='-GW-')]]

window = sg.Window('Rock Paper Scissors', layout, icon=r'rock.ico', font=('Helvetica', ' 13'), size=(450,250),default_button_element_size=(8,2))


speaker = win32com.client.Dispatch("SAPI.SpVoice")



while True:     # The Event Loop
    
    compChoice = ''
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
        break
    if event == 'Rock':
        window['-USER-'].update('Rock')
        speaker.Speak('You Chose Rock')
        sleep(0.5)
        compChoice = getCompChoice('Rock')
        window['-COMP-'].update(compChoice[0])
        window['-WINNER-'].update(compChoice[1])
        speaker.Speak('Computer chose' + compChoice[0])
        speaker.Speak('Winner is' + compChoice[1])
        gamesPlayed +=1
        window['-GP-'].update(gamesPlayed)
        if compChoice[1] =='Player':
            gamesWon +=1
            window['-GW-'].update(gamesWon)
    if event == 'Paper':
        window['-USER-'].update('Paper')
        speaker.Speak('You Chose Paper')
        sleep(0.5)
        compChoice = getCompChoice('Paper')
        window['-COMP-'].update(compChoice[0])
        window['-WINNER-'].update(compChoice[1])
        speaker.Speak('Computer chose' + compChoice[0])
        speaker.Speak('Winner is' + compChoice[1])
        gamesPlayed +=1
        window['-GP-'].update(gamesPlayed)
        if compChoice[1] =='Player':
            gamesWon +=1
            window['-GW-'].update(gamesWon)
        
    if event == 'Scissors':
        window['-USER-'].update('Scissors')
        speaker.Speak('You Chose Scissors')
        sleep(0.5)
        compChoice = getCompChoice('Scissors')
        window['-COMP-'].update(compChoice[0])
        window['-WINNER-'].update(compChoice[1])
        speaker.Speak('Computer chose' + compChoice[0])
        speaker.Speak('Winner is' + compChoice[1])
        gamesPlayed +=1
        window['-GP-'].update(gamesPlayed)
        if compChoice[1] =='Player':
            gamesWon +=1
            window['-GW-'].update(gamesWon)
        
    

window.close()
