import pandas as pd
df=pd.read_csv('bank.csv')
from tkinter import *
root=Tk()
root.geometry("550x250")
root.title("My Bank")
name=Label(root,text="Enter you name ")
name.grid(column=3,row=1)
nameEntry=Entry()
nameEntry.grid(column=4,row=1)
card=Label(root,text="Enter your card number ")
card.grid(column=3,row=2)
cardEntry=Entry()#to enter input
cardEntry.grid(column=4,row=2)
Password=Label(root,text="\nEnter your password")
Password.grid(column=3,row=3)
passwordEntry=Entry( show="*")#to enter input
passwordEntry.grid(column=4,row=3)

Deposite=Label(root,text="\n\nEnter money you want to \n deposite in dollares")
Deposite.grid(column=5,row=1)
depositeEntry=Entry()#to enter input
depositeEntry.grid(column=6,row=1)
withdraw=Label(root,text="Enter money you want to \n withdraw in dollares")
withdraw.grid(column=5,row=2)
withdrawEntry=Entry()#to enter input
withdrawEntry.grid(column=6,row=2)
currentMoney=0
accounts=0
current=0
money=[]
listOfcards=[]
listOfnames=[]
listOfpasswords=[]
def depositeFun():
      global current
      global money
      global accounts
      global listOfcards
      global currentMoney
      global listOfnames
      global listOfpasswords
      password=passwordEntry.get()
      name=nameEntry.get()
      Deposite= depositeEntry.get()
      cardnum=cardEntry.get()
      if name=="" or cardnum =="" or password=="" or Deposite=="":
         messagebox.showinfo(title="You cant deposite",message="please fill your cardnumberm, name , passord,\n and the deposite number")
      elif (cardnum not in listOfcards):
          messagebox.showinfo(title="You dont have an account",message="you should creat an account to deposite")
      elif (password not in listOfpasswords)or (name not in listOfnames):
           messagebox.showinfo(title="Somthing Wrong",message="Your cardnumber or name or password is wrong!")
      else:
          cardIn = listOfcards.index(cardnum)
          nameIn=listOfnames.index(name)
          passIn=listOfpasswords.index(password)
      
          if(listOfcards[cardIn]== cardnum and listOfnames[cardIn]==name and  listOfpasswords[cardIn]==password)or ((listOfcards[passIn]== cardnum and listOfnames[passIn]==name and  listOfpasswords[passIn]==password)or (listOfcards[nameIn]== cardnum and listOfnames[nameIn]==name and  listOfpasswords[nameIn]==password)):
              if accounts==0:
                 currentMoney = currentMoney +  int(Deposite)
                 money.append(currentMoney)
                 current=money[cardIn]
                 monyIn=money.index(current)
                 print(len(money))
              elif (len(money) != cardIn+1):
                 currentMoney=0
                 currentMoney=currentMoney+int(Deposite)
                 money.append(currentMoney)
                 money[cardIn]=currentMoney
                 
              else:
                 current=money[cardIn]
                 current = current+  int(Deposite)
                 money[cardIn]=current 
                 messagebox.showinfo(title="Deposite done",message=" hi {name}, your current account has {my} dollares\n you deposited {deposite}".format(name=name,my=money[cardIn], deposite=Deposite))
                 row=len(df)
                 df.loc[row+1,"name"]=name
                 df.loc[row+1,"cardnumber"]=cardnum
                 df.loc[row+1,"password"]=password
                 df.to_csv(r'C:\Users\compulife\Desktop\bank.csv', index = False)
              accounts+=1
            
          else:
             messagebox.showinfo(title="Somthing Wrong",message="Your cardnumber or name or password is wrong!")
def creataccount():
    
    global currentMoney
    cardnum=cardEntry.get()
    password=passwordEntry.get()
    name=nameEntry.get()
    deposite=depositeEntry.get()
    global listOfcards
    global listOfnames
    global listOfpasswords
    if name=="" or cardnum =="" or password=="" or deposite<"200":
         messagebox.showinfo(title="You cant creat an account",message="you should fill your name , cardnumber,password and \n deposite 200$ at least to creat an account")
         
    elif cardnum in listOfcards:
         messagebox.showinfo(title="You cant creat an account",message="This cardnumber is already used")
    
    else:
        messagebox.showinfo(title="congratulation",message="hi {name},Now you have an account and you can deposite and withdraw".format(name=name))
        listOfcards.append(cardnum)
        listOfnames.append(name)
        listOfpasswords.append(password)
        depositeFun()

def status():
    global current
    global money
    global accounts
    global currentMoney
    global listOfcards
    global listOfnames
    global listOfpasswords
    cardnum=cardEntry.get()
    password=passwordEntry.get()
    name=nameEntry.get()
    if name=="" or cardnum =="" or password=="" or Deposite=="":
        messagebox.showinfo(title="There is no status",message="You dont have an account to show the status")
    elif (cardnum not in listOfcards):
          messagebox.showinfo(title="There is no status",message="You dont have an account to show the status")
    elif (password not in listOfpasswords)or (name not in listOfnames):
           messagebox.showinfo(title="Somthing Wrong",message="Your cardnumber or name or password is wrong!")
    else:
          cardIn = listOfcards.index(cardnum)
          nameIn=listOfnames.index(name)
          passIn=listOfpasswords.index(password)
      
          if(listOfcards[cardIn]== cardnum and listOfnames[cardIn]==name and  listOfpasswords[cardIn]==password)or ((listOfcards[passIn]== cardnum and listOfnames[passIn]==name and  listOfpasswords[passIn]==password)or (listOfcards[nameIn]== cardnum and listOfnames[nameIn]==name and  listOfpasswords[nameIn]==password)):
             current=money[cardIn]
             messagebox.showinfo(title="your sataus",message=" hi {name}, your current account has {my} dollares".format(name=name,my=current))
          else:
             messagebox.showinfo(title="Somthing Wrong",message="Your cardnumber or name or password is wrong!")
    
def withdrawFun():
        global current
        global currentMoney
        global listOfcards
        global listOfnames
        global listOfpasswords
        withdraw=withdrawEntry.get()
        cardnum=cardEntry.get()
        password=passwordEntry.get()
        name=nameEntry.get()
        if name=="" or cardnum =="" or password=="" or Deposite=="":
             messagebox.showinfo(title="You cant withdraw",message="please fill your cardnumberm, name , passord,\n and the withdraw number")
        elif (cardnum not in listOfcards):
             messagebox.showinfo(title="You dont have an account",message="you should creat an account to withdraw")
        elif (password not in listOfpasswords)or (name not in listOfnames):
             messagebox.showinfo(title="Somthing Wrong",message="Your cardnumber or name or password is wrong!")
        else:
              cardIn = listOfcards.index(cardnum)
              nameIn=listOfnames.index(name)
              passIn=listOfpasswords.index(password)
      
              if(listOfcards[cardIn]== cardnum and listOfnames[cardIn]==name and  listOfpasswords[cardIn]==password)or ((listOfcards[passIn]== cardnum and listOfnames[passIn]==name and  listOfpasswords[passIn]==password)or (listOfcards[nameIn]== cardnum and listOfnames[nameIn]==name and  listOfpasswords[nameIn]==password)):
                  cardIn = listOfcards.index(cardnum)
                  current=money[cardIn]
                  if (int(withdraw) > current):
                         messagebox.showinfo(title="you cant woithdraw",message="your current mony is less than what you wnt to withdraw, try again!")
                  else:
                         current = current- int(withdraw)
                         money[cardIn]=current
                         messagebox.showinfo(title="withdraw done",message="hi {name},you withdraw {withdraw}".format(name=name,withdraw=withdraw))
              else:
                 messagebox.showinfo(title="Somthing Wrong",message="Your cardnumber or name or password is wrong!")

bu1=Button(root,text="creat account",bg="#2596be")
bu1.grid(row=10,column=3,ipadx=20,ipady=20)
bu1.config(command= creataccount)

bu2=Button(root,text="Status",bg="#2596be")
bu2.grid(row=10,column=4,ipadx=30,ipady=20)
bu2.config(command=status)


bu3=Button(root,text="deposite",bg="#2596be")
bu3.grid(row=10,column=5,ipadx=30,ipady=20)
bu3.config(command=depositeFun)

bu4=Button(root,text="withdraw",bg="#2596be")
bu4.grid(row=10,column=6,ipadx=30,ipady=20)
bu4.config(command= withdrawFun)


root.mainloop()