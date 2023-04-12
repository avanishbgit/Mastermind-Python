from tkinter import *
import time
import random

cols=('Red','Blue','Green','Yellow','Orange','Pink')

i=0
tries=0
count=0
ypad=0
correctCol=[]



def Submit():
    global root
    fh=open('Scores.txt',mode='a+')
    fh.write(str(ent_high.get()+','+str(tries)+'\n'))
    fh.close()
    winscreen.destroy()
    root.destroy()
    mainScreen()

def highScore():
    ln=[]
    hs_win=Tk()
    fh=open('Scores.txt',mode='r')
    te=fh.readlines()
    hs_win.geometry('200x{}'.format(25*len(te)))
    hs_win.title('Scoreboard')
    for i in te:
        i=i.strip()
        ln.append(i)
    for i in ln:
        i=i.split(',')
        nl=Label(hs_win,text='{}: {}'.format(i[0],i[1]))
        nl.pack()
        
def mainScreen():
    global root
    global main_title
    global rules
    global bt_enter
    global bt_hs
    global ans 

    ans=[random.choice(cols) for i in range(4)]
    print("Debug:",ans)

    root=Tk()
    root.geometry('400x350')
    root.title('Mastermind')
    main_title=Label(root,text='Welcome' , font=('Consolas' ,20))
    main_title.pack()

    rules=Label(root,text='Key for results:\nBlack - correct colour in the\n correct position\nWhite - correct colour in the\nincorrect position' , font=('Consolas' ,12))
    rules.pack()

    bt_enter=Button(root,text='Play',width=10,command=enter, bg='green',fg='white')
    bt_enter.place(x='160',y='290')
    bt_hs=Button(root,text='Scores',width=10,command=highScore,bg='light blue')
    bt_hs.place(x='160',y='320')
    root.mainloop()

def win():
    global ent_high
    global winscreen
    winscreen=Tk()
    winscreen.geometry('250x200')
    winscreen.title('Submit Score')
    lb_win=Label(winscreen,text='You won in {} tries'.format(tries),font=('Consolas',13))
    ent_high=Entry(winscreen,text='Name',justify='center')
    bt_submit=Button(winscreen,text='Submit',command=Submit)
    lb_win.pack()
    ent_high.pack()
    bt_submit.pack()
    winscreen.mainloop()

def lost():
    losescreen=Tk()
    losescreen.geometry('250x200')
    lb_lose = Label(losescreen,text='You lost :(',font=('Consolas',15))
    lb_lose.pack()
    losescreen.mainloop()

def kill():
    root.destroy()
    killscreen=Tk()
    killscreen.geometry('300x50')
    lb_kill=Label(killscreen,text='Thanks for playing',font=('Consolas',15))
    lb_kill.pack()
    killscreen.after(3000, lambda: killscreen.destroy())
    killscreen.mainloop()
    

def check():
    global tries
    global count
    global ypad
    global correctCol
    inp=[]
    inp.append(c1.get())
    inp.append(c2.get())
    inp.append(c3.get())
    inp.append(c4.get())
    if tries<=8:
        if (ans == inp):
            tries+=1
            correctCol=['Black','Black','Black','Black']
            print(inp,'is the correct answer, you win!!') 
            win()
            
        else:      
            tries += 1  
            correctCol = []
            ln=ans.copy()
            for i in range(0, 4):  
                if (inp[i] == ln[i]):   
                    count += 1  
                    correctCol.append('Black')
                    ln[i]=None
                
            for i in range(4):
                if inp[i] in ln and inp[i] != ans[i]:
                    correctCol.append('White')
                    ln[ln.index(inp[i])]=None
            if (count < 4) and (count != 0):   
                print("\nNot quite the colours. But you did get some colours right...") 
                random.shuffle(correctCol)
                print(correctCol)
                    
                #print('\n') 
                print("Try again -") 
        
            elif correctCol==[]:   
                print("\nNone of the colours in your input match.") 
                print("Try again -")
        
        xpad=0
        lb_try=Label(root,text='Try {}:'.format(tries) , font=('Consolas' ,10))
        lb_try.place(x=0,y=35+ypad)
        lb_gives=Label(root,text='gives' , font=('Consolas' ,10))
        lb_gives2=Label(root,text='gives nothing' , font=('Consolas' ,10))

        circl_c1=can.create_oval(5, 5+ypad, 30, 30+ypad,fill=inp[0])
        circl_c2=can.create_oval(35, 5+ypad, 60, 30+ypad,fill=inp[1])
        circl_c3=can.create_oval(65, 5+ypad, 90, 30+ypad,fill=inp[2])
        circl_c4=can.create_oval(95, 5+ypad, 120, 30+ypad,fill=inp[3])
        if correctCol == []:
        	lb_gives2.place(x=180,y=35+ypad)
        else:
        	lb_gives.place(x=180,y=35+ypad)
        for i in correctCol:
            circl_c1=can.create_oval(185+xpad, 5+ypad, 210+xpad, 30+ypad,fill=i)
            xpad+=30
        can.pack()
        ypad+=30
    else:
        lost()
        print('You lost :(')
    


def enter():
    global c1
    global c2
    global c3
    global c4
    global can
    global main_title
    global rules
    global bt_enter

    can=Canvas(root,height='300',width='300')

    main_title.destroy()
    rules.destroy()
    bt_enter.destroy()
    bt_hs.destroy()

    c1=StringVar()
    c2=StringVar()
    c3=StringVar()
    c4=StringVar()

    c1.set('Select')
    c2.set('Select')
    c3.set('Select')
    c4.set('Select')

    opt_col1=OptionMenu(root,c1,*cols)
    opt_col2=OptionMenu(root,c2,*cols)
    opt_col3=OptionMenu(root,c3,*cols)
    opt_col4=OptionMenu(root,c4,*cols)

    opt_col1.place(x=12.5,y=300)
    opt_col2.place(x=112.5,y=300)
    opt_col3.place(x=212.5,y=300)
    opt_col4.place(x=312.5,y=300)

    bt_test=Button(root,text='Check',command=check)
    bt_test.pack()
    root.mainloop()
    
    
    
mainScreen()