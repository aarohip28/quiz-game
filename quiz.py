from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

mixer.init()

mixer.music.load('images/kbc.mp3')
# mixer.music.play()

def select(event):
    callButton.place_forget()

    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()



    b=event.widget
    value=b['text']
    for i in range(15):
        if value==correct_answers[i]:
            if value==third_option[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    lifeLine50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    phoneLifeLineButton.config(state=NORMAL, image=phoneImage)

                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])

                    amountLabel.config(image=amountImage)


                root2 = Toplevel()
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('You won 0 pounds!!')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=30)

                winLabel = Label(root2, text='You Won!!', font=('arial', 35, 'bold'),
                                 bg='black', fg='white')
                winLabel.pack()

                playButton = Button(root2, text='Play again', font=('arial', 20, 'bold'),
                                    bg='black', fg='white',command=playagain)
                playButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'),
                                     bg='black', fg='white',command=close)
                closeButton.pack()

                happyImage = PhotoImage(file='images/happy.png')
                happyLabel = Label(root2, image=happyImage)
                happyLabel.place(x=30, y=280)

                happyLabel1 = Label(root2, image=happyImage)
                happyLabel1.place(x=400, y=280)

                root2.mainloop()
                break

            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])

            amountLabel.config(image=amountImages[i])

        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                lifeLine50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audiencePole)
                phoneLifeLineButton.config(state=NORMAL,image=phoneImage)

                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountLabel.config(image=amountImage)


            root1=Toplevel()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 pounds!!')
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loseLabel=Label(root1,text='You Lose!!',font=('arial',35,'bold'),bg='black',fg='white')
            loseLabel.pack()

            tryAgainButton=Button(root1,text='Try again',font=('arial',20,'bold'),
                                  bg='black',fg='white',command=tryagain)
            tryAgainButton.pack()

            closeButton=Button(root1,text='Close',font=('arial',20,'bold'),
                               bg='black',fg='white',command=close)
            closeButton.pack()

            sadImage = PhotoImage(file='images/sad.png')
            sadLabel = Label(root1,image=sadImage)
            sadLabel.place(x=30,y=280)

            sadLabel1 = Label(root1, image=sadImage)
            sadLabel1.place(x=400, y=280)

            root1.mainloop()
            break




root=Tk()
root.geometry('1270x652+0+0')
root.title('Quiz App')
root.config(bg='black')


questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

def lifeLine50():
    lifeLine50Button.config(image=image50x,state=DISABLED)
    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton1.config(text='')
        optionButton2.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton4.config(text='')
        optionButton1.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')


def audiencePoleLifeLine():
    audiencePoleButton.config(image=audiencePoleX,state=DISABLED)
    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620,y=190)
    progressbarC.place(x=660,y=190)
    progressbarD.place(x=700,y=190)

    progressbarLabelA.place(x=580,y=320)
    progressbarLabelB.place(x=620,y=320)
    progressbarLabelC.place(x=660,y=320)
    progressbarLabelD.place(x=700,y=320)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0,'end-1c')==questions[2]:
        progressbarA.config(value=80)
        progressbarB.config(value=60)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if questionArea.get(1.0,'end-1c')==questions[3]:
        progressbarA.config(value=30)
        progressbarB.config(value=70)
        progressbarC.config(value=90)
        progressbarD.config(value=50)

    if questionArea.get(1.0,'end-1c')==questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)
        progressbarB.config(value=10)
        progressbarC.config(value=60)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=20)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)
        progressbarB.config(value=70)
        progressbarC.config(value=50)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)
        progressbarB.config(value=80)
        progressbarC.config(value=70)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)
        progressbarB.config(value=20)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=90)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)
        progressbarB.config(value=60)
        progressbarC.config(value=50)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)
        progressbarB.config(value=30)
        progressbarC.config(value=40)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)
        progressbarB.config(value=60)
        progressbarC.config(value=90)
        progressbarD.config(value=80)

def phoneLifeLine():
    mixer.music.load('images/calling.mp3')
    mixer.music.play()
    callButton.place(x=70,y=260)
    phoneLifeLineButton.config(image=phoneImageX,state=DISABLED)

def phoneClick():
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f"The correct ans is {correct_answers[i]}")
            engine.runAndWait()



correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "7:23PM", "MI", "Jupiter", "7",
                   "1000 years", "Apple","Bill Gates"]


leftFrame=Frame(root,bg='black',padx=90)
leftFrame.grid(row=0,column=0)

topFrame=Frame(leftFrame,bg='black',pady=15)
topFrame.grid()
centerFrame=Frame(leftFrame,bg='black',pady=15)
centerFrame.grid(row=1,column=0)
bottomFrame=Frame(leftFrame)
bottomFrame.grid(row=2,column=0)

rightFrame=Frame(root,pady=25,padx=50,bg='black')
rightFrame.grid(row=0,column=1)

image50=PhotoImage(file='images/50-50.png')
image50x=PhotoImage(file='images/50-50-X.png')
lifeLine50Button=Button(topFrame,image=image50,bg='black',bd=0,
                        activebackground='black',width=180,height=80,command=lifeLine50)
lifeLine50Button.grid(row=0,column=0)

audiencePole=PhotoImage(file='images/audiencePole.png')
audiencePoleX=PhotoImage(file='images/audiencePoleX.png')
audiencePoleButton=Button(topFrame,image=audiencePole,bg='black',bd=0,
                          activebackground='black',width=180,height=80,command=audiencePoleLifeLine)
audiencePoleButton.grid(row=0,column=1)

phoneImage=PhotoImage(file='images/phoneAFriend.png')
phoneImageX=PhotoImage(file='images/phoneAFriendX.png')
phoneLifeLineButton=Button(topFrame,image=phoneImage,bg='black',bd=0,
                           activebackground='black',width=180,height=80,command=phoneLifeLine)
phoneLifeLineButton.grid(row=0,column=2)

callImage=PhotoImage(file='images/phone.png')
callButton=Button(root,image=callImage,bd=0,bg='black',activebackground='black',
                  cursor='hand2',command=phoneClick)


centerImage=PhotoImage(file='images/center.png')
logoLabel=Label(centerFrame,image=centerImage,bg='black',width=300,height=200)
logoLabel.grid(row=0,column=0)

amountImage=PhotoImage(file='images/Picture0.png')
amountImage1=PhotoImage(file='images/Picture1.png')
amountImage2=PhotoImage(file='images/Picture2.png')
amountImage3=PhotoImage(file='images/Picture3.png')
amountImage4=PhotoImage(file='images/Picture4.png')
amountImage5=PhotoImage(file='images/Picture5.png')
amountImage6=PhotoImage(file='images/Picture6.png')
amountImage7=PhotoImage(file='images/Picture7.png')
amountImage8=PhotoImage(file='images/Picture8.png')
amountImage9=PhotoImage(file='images/Picture9.png')
amountImage10=PhotoImage(file='images/Picture10.png')
amountImage11=PhotoImage(file='images/Picture11.png')
amountImage12=PhotoImage(file='images/Picture12.png')
amountImage13=PhotoImage(file='images/Picture13.png')
amountImage14=PhotoImage(file='images/Picture14.png')

amountImages=[amountImage1,amountImage2,amountImage3,amountImage4,amountImage5,
              amountImage6,amountImage7,amountImage8,amountImage9,amountImage10,
              amountImage11,amountImage12,amountImage13,amountImage14]

amountLabel=Label(rightFrame,image=amountImage,bg='black')
amountLabel.grid(row=0,column=0)


layOutImage=PhotoImage(file='images/lay.png')
layOutLabel=Label(bottomFrame,image=layOutImage,bg='black')
layOutLabel.grid(row=0,column=0)

questionArea=Text(bottomFrame,font=('arial',18,'bold'),width=34,
                  height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,questions[0])

labelA=Label(bottomFrame,text='A: ',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=60,y=110)
optionButton1=Button(bottomFrame,text=first_option[0],font=('arial',18,'bold'),
                     bd=0,bg='black',activebackground='black',fg='white',
                     activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=100)

labelB=Label(bottomFrame,text='B: ',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=330,y=110)
optionButton2=Button(bottomFrame,text=second_option[0],font=('arial',18,'bold'),
                     bd=0,bg='black',activebackground='black',fg='white',
                     activeforeground='white',cursor='hand2')
optionButton2.place(x=370,y=100)

labelC=Label(bottomFrame,text='C: ',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=60,y=180)
optionButton3=Button(bottomFrame,text=third_option[0],font=('arial',18,'bold'),
                     bd=0,bg='black',activebackground='black',fg='white',
                     activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=180)

labelD=Label(bottomFrame,text='D: ',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=330,y=190)
optionButton4=Button(bottomFrame,text=fourth_option[0],font=('arial',18,'bold'),
                     bd=0,bg='black',activebackground='black',fg='white',
                     activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

progressbarA=Progressbar(root,orient=VERTICAL,length=120)
progressbarB=Progressbar(root,orient=VERTICAL,length=120)
progressbarC=Progressbar(root,orient=VERTICAL,length=120)
progressbarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarLabelA=Label(root,text='A',font=('arial',20,'bold'),
                        bg='black',fg='white')
progressbarLabelB=Label(root,text='B',font=('arial',20,'bold'),
                        bg='black',fg='white')
progressbarLabelC=Label(root,text='C',font=('arial',20,'bold'),
                        bg='black',fg='white')
progressbarLabelD=Label(root,text='D',font=('arial',20,'bold'),
                        bg='black',fg='white')



optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)

root.mainloop()

