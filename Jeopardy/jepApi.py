import requests
import json
#import win32com.client
import random

def triviaSet(i):
    parameters = {"id":i}
    
    questionList =[]
    questionSet = []
    
    response = requests.get("http://jservice.io/api/category",params=parameters)
    
    data = response.json()
    cat = data['title'] 
    clues = data['clues']

    while len(questionList) <= 10:
        questions = []
        rand = random.randint(0,len(clues)-1)
        q = clues[rand]
        if q not in questionList:
            questionList.append(q)

    for i in range(0,len(questionList) -1):
        temp = []
        temp2 = questionList[i]
        tId = temp2.get("id")
        tQ = temp2.get("question")
        tA = temp2.get("answer")
        temp.append(tId)
        temp.append(tQ)
        temp.append(tA)
        questionSet.append(temp)
    
    return [cat,questionSet]
    
