import PySimpleGUI as sg
from jepApi import *




def correctAnswer():
    sg.popup('Correct')
    #print('Correct')




def incAnswer(i):
    sg.popup('Sorry the correct answer was ' + i)
    #print('Sorry the correct answer was ' +i)




def displayEndScreen(c):
    
    layout = [
        [sg.Text("RESULTS")],
        [sg.Text("Category: " )],
        [sg.Text("Number Answered Correctly: " + str(c))],
        [sg.Text("Play Again?    "), sg.Button("YES"), sg.Button("NO")]
        ]
    window = sg.Window("GAME OVER",layout, size=(250,150))
    event, value = window.read()
    if event == 'YES':
        correct = 0
        window.CloseNonBlocking()
        displayMenu()
    if event == 'NO':
        window.CloseNonBlocking()




def displayMenu():
    layout = [[sg.Text('Welcome To Jeopardy!')],
              [sg.Text('Please Choose a Category Below')],
              [sg.Rad("Baseball",'CAT', key =2)],
              [sg.Rad("Movies",'CAT', key = 4)],
              [sg.Rad("Odd Jobs",'CAT', key = 3)],
              [sg.Rad("Trivia",'CAT', key = 11)],
              [sg.Rad("Hollywood Legends",'CAT', key = 15)],
              [sg.Rad("Cars",'CAT', key = 16)],
              [sg.Rad("Animals",'CAT', key = 21)],
              [sg.Rad("Movie Trivia",'CAT', key = 24)],
              [sg.Rad("Science",'CAT', key = 25)],
              [sg.Rad("Toys & Games",'CAT', key = 32)],
              [sg.Button("Submit"), sg.Button("Quit")]]
    
    window = sg.Window('Jeopardy - Main Menu',layout)
    button, values = window.read()
    selected = values
    choice = ''
    cat = ''
    for key in selected:
        if selected[key] == True:
            choice = key
            

    qList = triviaSet(choice)
    cat = qList[0]
    questions = qList[1]
    
    q = []
    a = []
    for i in questions:
        q.append(i[1])
        a.append(i[2])

        
    window.close()
    
    displayQuestions(cat,q,a)




def displayQuestions(c,q,a):
    correct = 0
    #cat = c
    
    for i in range(len(q)):
        #createWindow(i)
        layout = [
            [sg.Text('Category: ' + c)], 
            [sg.Text('Question')],
            [sg.Text(q[i])],
            [sg.Text('enter answer below')],
            [sg.InputText(key = '-QUERY-')],
            [sg.Text('Question No: ' + str(i +1)), sg.Text('       Number Correct ' + str(correct))],
            #[sg.Output(size=(50,2))],
            [sg.Button("Submit")]
            ]

        window = sg.Window('Jeopardy',layout)
        event,value = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event =='Submit':
            query = value['-QUERY-'].rstrip()
            if query == a[i]:
                correctAnswer()
                correct +=1
            else:
                incAnswer(a[i])
        
        window.CloseNonBlocking()
        

    displayEndScreen(correct)


