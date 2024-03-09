import tkinter
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

def train() :
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    #Taking input 
    gender=e1.get()
    married=e2.get()
    dependents=int(e3.get())
    Education=e4.get()
    SelfEmployed=e5.get()
    Applicantincome=int(e6.get())
    coapplicantincome=int(e7.get())
    loanamount=int(e8.get())
    loanamountterm=int(e9.get())
    credithistory=int(e10.get())
    propertyarea=e11.get()

    #Storing data 
    data = [[gender,married,dependents,Education,SelfEmployed,Applicantincome,coapplicantincome,loanamount,loanamountterm,credithistory,propertyarea]]

    #Read file
    df=pd.read_csv('train.csv')

    X=df.drop(['Loan_Status','Loan_ID'], axis=1)
    y=df['Loan_Status']

    #Filling null values
    X['Gender'].fillna("Male", inplace=True)
    X['Married'].fillna("Yes", inplace=True)
    X['Dependents'].fillna(0,inplace=True)
    X['Self_Employed'].fillna('No',inplace=True)
    mean_loan=X['LoanAmount'].mean()
    X['LoanAmount'].fillna(mean_loan,inplace=True)
    X['Loan_Amount_Term'].fillna(X['Loan_Amount_Term'].mean(),inplace=True)
    X['Credit_History'].fillna(X['Credit_History'].mean(),inplace=True)

    #Removing categorical data
    X=pd.get_dummies(X)

    #Training
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.30)
    X_train.shape
    X_test.shape
    y_test.shape

    #Using Method
    model = LogisticRegression()
    model.fit(X,y)
    model.score(X,y)

    #Creating new data frame
    newdf = pd.DataFrame(data, columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'])
    newdf = pd.get_dummies(newdf)

    #Filling missing values
    missing_cols = set( X_train.columns ) - set( newdf.columns )
    for c in missing_cols:
        newdf[c] = 0

    #Using training data 
    newdf = newdf[X_train.columns]

    #Now predicting Loan
    yp=model.predict(newdf)
    if (yp[0]=='Y'):
        messagebox.showinfo("Result", "Your Loan is approved, Please contact at HDFC Bank Any Branch for further processing",icon = "info")
    else:
        messagebox.showinfo("Result", "Sorry ! Your Loan is not approved" , icon = "error")


top = tkinter.Tk()
top.title("Loan Prediction Application By Abhishek Yadav")

# Load and resize the background image
bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((800, 600))  
bg_img = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tkinter.Label(top, image=bg_img)
bg_label.place(relwidth=1, relheight=1) 

# Colorful theme
label_color = "#333333"
button_color = "#4CAF50"  # Green
frame_color = "#E6E6FA"  # Lavender

# Create a transparent frame for the title and form
frame = tkinter.Frame(top, bg=frame_color)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Title Label inside the frame
title_label = tkinter.Label(frame, text="Loan Prediction", font=("Helvetica", 20, "bold"), fg=label_color, bg=frame_color)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

l1 = tkinter.Label(frame,text = "What is your gender:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l1.grid(row=1, column=0, padx=20, pady=5, sticky='w')
e1 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e1.grid(row=1, column=1, padx=20, pady=5, sticky='w')

l2 = tkinter.Label(frame , text = "Married:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l2.grid(row=2, column=0, padx=20, pady=5, sticky='w')
e2 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e2.grid(row=2, column=1, padx=20, pady=5, sticky='w')

l3 = tkinter.Label(frame ,text = "Dependents Value:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l3.grid(row=3, column=0, padx=20, pady=5, sticky='w')
e3 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e3.grid(row=3, column=1, padx=20, pady=5, sticky='w')

l4 = tkinter.Label(frame ,text = "Enter Your Education:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l4.grid(row=4, column=0, padx=20, pady=5, sticky='w')
e4 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e4.grid(row=4, column=1, padx=20, pady=5, sticky='w')

l5 = tkinter.Label(frame ,text = "Self Employed:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l5.grid(row=5, column=0, padx=20, pady=5, sticky='w')
e5 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e5.grid(row=5, column=1, padx=20, pady=5, sticky='w')

l6 = tkinter.Label(frame ,text = "Enter Applicant Income:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l6.grid(row=6, column=0, padx=20, pady=5, sticky='w')
e6 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e6.grid(row=6, column=1, padx=20, pady=5, sticky='w')

l7 = tkinter.Label(frame , text = "Enter co Applicant Income:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l7.grid(row=7, column=0, padx=20, pady=5, sticky='w')
e7 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e7.grid(row=7, column=1, padx=20, pady=5, sticky='w')

l8 = tkinter.Label(frame ,text = "Enter Loan Amount:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l8.grid(row=8, column=0, padx=20, pady=5, sticky='w')
e8 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e8.grid(row=8, column=1, padx=20, pady=5, sticky='w')

l9 = tkinter.Label(frame , text = "Enter Loan Amount Term:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l9.grid(row=9, column=0, padx=20, pady=5, sticky='w')
e9 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e9.grid(row=9, column=1, padx=20, pady=5, sticky='w')

l10 = tkinter.Label(frame ,text = "Enter Credit History:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l10.grid(row=10, column=0, padx=20, pady=5, sticky='w')
e10= tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e10.grid(row=10, column=1, padx=20, pady=5, sticky='w')

l11= tkinter.Label(frame , text = "Enter Property Area:" , font=("Helvetica", 12), fg=label_color, bg=frame_color)
l11.grid(row=11, column=0, padx=20, pady=5, sticky='w')
e11 = tkinter.Entry(frame, bd=5, font=("Helvetica", 12))
e11.grid(row=11, column=1, padx=20, pady=5, sticky='w')

b = tkinter.Button(frame, text="Predict", command=train, font=("Helvetica", 12), bg=button_color)
b.grid(row=12, column=0, columnspan=2, pady=10)

top.geometry("800x600")
top.mainloop()