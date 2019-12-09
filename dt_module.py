import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score 
import matplotlib.pyplot as plt
import seaborn as sns

from tkinter import *
root = Tk()

def ins():
	data = pd.read_csv("data.csv")
	y = data['price_range']
	x = data.drop('price_range',axis=1)
	x_train, x_valid, y_train, y_valid = train_test_split(x,y,test_size=0.2,random_state=101,stratify=y)
	
	dt = DecisionTreeClassifier(random_state=101)
	dt_model = dt.fit(x_train, y_train)

	
	x_test=[[0]*20]*1

	x_test[0][0] = float(u0.get())
	x_test[0][1] = float(u1.get())
	x_test[0][2] = float(u2.get())
	x_test[0][3] = float(u3.get())
	x_test[0][4] = float(u4.get())
	x_test[0][5] = float(u5.get())
	x_test[0][6] = float(u6.get())
	x_test[0][7] = float(u7.get())
	x_test[0][8] = float(u8.get())
	x_test[0][9] = float(u9.get())
	x_test[0][10] = float(v0.get())
	x_test[0][11] = float(v1.get())
	x_test[0][12] = float(v2.get())
	x_test[0][13] = float(v3.get())
	x_test[0][14] = float(v4.get())
	x_test[0][15] = float(v5.get())
	x_test[0][16] = float(v6.get())
	x_test[0][17] = float(v7.get())
	x_test[0][18] = float(v8.get())
	x_test[0][19] = float(v9.get())

	y_pred_dt = dt.predict(x_test)
	blank.insert(0,*y_pred_dt*3000 + 2000)
	print(*y_pred_dt)
	

root.geometry("900x500")
root.maxsize(900,500)
root.minsize(900,500)
root.title("Mobile Price Prediction Module")

head = Label(root, text="Tell Me ! \n What are Your Requirements?", font="comicsansms 13 bold",bg='light gray', padx="20",pady="30")
head.pack(fill='x')

f1 = Frame(root,bg='#DCB2E3',borderwidth=0)
f1.pack(side=LEFT)

root2 = Frame(root,bg='#DCB2E3',borderwidth=0)
root2.pack(side=LEFT)

root1 = Frame(root,bg='#DCB2E3',borderwidth=0)
root1.pack(side=RIGHT)

f2 = Frame(root,bg='#DCB2E3',borderwidth=0)
f2.pack(side=RIGHT)

f3 = Frame(root,bg='#3D0C46',borderwidth=0)
f3.pack(side=BOTTOM)

l0 = Label(f1,text='Battery Power',bg='#DCB2E3',padx=20,pady=10)
l0.pack()
u0 = StringVar()
u0_entry = Entry(root2,textvariable=u0)
u0_entry.pack(anchor='nw',padx=20,pady=10)

l1 = Label(f1,text='Blue',bg='#DCB2E3',padx=20,pady=10)
l1.pack()
u1 = StringVar()
u1_entry = Entry(root2,textvariable=u1)
u1_entry.pack(anchor='nw',padx=20,pady=10)

l2 = Label(f1,text='Clock Speed',bg='#DCB2E3',padx=20,pady=10)
l2.pack()
u2 = StringVar()
u2_entry = Entry(root2,textvariable=u2)
u2_entry.pack(anchor='nw',padx=20,pady=10)


l3 = Label(f1,text='Dual Sim',bg='#DCB2E3',padx=20,pady=10)
l3.pack()
u3 = StringVar()
u3_entry = Entry(root2,textvariable=u3)
u3_entry.pack(anchor='nw',padx=20,pady=10)

l4 = Label(f1,text='Front Camera',bg='#DCB2E3',padx=20,pady=10)
l4.pack()
u4 = StringVar()
u4_entry = Entry(root2,textvariable=u4)
u4_entry.pack(anchor='nw',padx=20,pady=10)

l5 = Label(f1,text='4G',bg='#DCB2E3',padx=20,pady=10)
l5.pack()
u5 = StringVar()
u5_entry = Entry(root2,textvariable=u5)
u5_entry.pack(anchor='nw',padx=20,pady=10)

l6 = Label(f1,text='Internal Memory',bg='#DCB2E3',padx=20,pady=10)
l6.pack()
u6 = StringVar()
u6_entry = Entry(root2,textvariable=u6)
u6_entry.pack(anchor='nw',padx=20,pady=10)

l7 = Label(f1,text='Dep',bg='#DCB2E3',padx=20,pady=10)
l7.pack()
u7 = StringVar()
u7_entry = Entry(root2,textvariable=u7)
u7_entry.pack(anchor='nw',padx=20,pady=10)

l8 = Label(f1,text='Mobile Weight',bg='#DCB2E3',padx=20,pady=10)
l8.pack()
u8 = StringVar()
u8_entry = Entry(root2,textvariable=u8)
u8_entry.pack(anchor='nw',padx=20,pady=10)

l9 = Label(f1,text='Cores',bg='#DCB2E3',padx=20,pady=10)
l9.pack()
u9 = StringVar()
u9_entry = Entry(root2,textvariable=u9)
u9_entry.pack(anchor='nw',padx=20,pady=10)




v0 = StringVar()
v0_entry = Entry(root1,textvariable=v0)
v0_entry.pack(anchor='ne',padx=20,pady=10)
t0 = Label(f2,text='PC',bg='#DCB2E3',padx=20,pady=10)
t0.pack()

v1 = StringVar()
v1_entry = Entry(root1,textvariable=v1)
v1_entry.pack(anchor='ne',padx=20,pady=10)
t1 = Label(f2,text='Pixel Height',bg='#DCB2E3',padx=20,pady=10)
t1.pack()

v2 = StringVar()
v2_entry = Entry(root1,textvariable=v2)
v2_entry.pack(anchor='ne',padx=20,pady=10)
t2 = Label(f2,text='Pixel Width',bg='#DCB2E3',padx=20,pady=10)
t2.pack()

v3 = StringVar()
v3_entry = Entry(root1,textvariable=v3)
v3_entry.pack(anchor='ne',padx=20,pady=10)
t3 = Label(f2,text='Ram',bg='#DCB2E3',padx=20,pady=10)
t3.pack()

v4 = StringVar()
v4_entry = Entry(root1,textvariable=v4)
v4_entry.pack(anchor='ne',padx=20,pady=10)
t4 = Label(f2,text='Screen Height',bg='#DCB2E3',padx=20,pady=10)
t4.pack()

v5 = StringVar()
v5_entry = Entry(root1,textvariable=v5)
v5_entry.pack(anchor='ne',padx=20,pady=10)
t5 = Label(f2,text='Screen Width',bg='#DCB2E3',padx=20,pady=10)
t5.pack()

v6 = StringVar()
v6_entry = Entry(root1,textvariable=v6)
v6_entry.pack(anchor='ne',padx=20,pady=10)
t6 = Label(f2,text='TalkTime',bg='#DCB2E3',padx=20,pady=10)
t6.pack()

v7 = StringVar()
v7_entry = Entry(root1,textvariable=v7)
v7_entry.pack(anchor='ne',padx=20,pady=10)
t7 = Label(f2,text='3G',bg='#DCB2E3',padx=20,pady=10)
t7.pack()

v8 = StringVar()
v8_entry = Entry(root1,textvariable=v8)
v8_entry.pack(anchor='ne',padx=20,pady=10)
t8 = Label(f2,text='Touch Screen',bg='#DCB2E3',padx=20,pady=10)
t8.pack()

v9 = StringVar()
v9_entry = Entry(root1,textvariable=v9)
v9_entry.pack(anchor='ne',padx=20,pady=10)
t9 = Label(f2,text='Wi-Fi',bg='#DCB2E3',padx=20,pady=10)
t9.pack()

p = Label(f3,text='To Confirm Click the Submit Button',font="comicsansms 8 bold",pady=20)
p.pack()
b1 = Button(f3,fg='white',bg='#3D0C46',width=27,text="Submit",command=ins)
b1.pack()
p1 = Label(f3,text='Predicted Price is near about ',font="comicsansms 10 bold",fg='white',bg='#3D0C46')
p1.pack()
blank = Entry(f3)
blank.pack(pady=20)
root.mainloop()