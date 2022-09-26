
from audioop import add
import requests
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Shool")



labelHeading = tk.Label(root, text="Student Details",font=("Times New Roman",20)).grid(column=2,row=1)
labelName = tk.Label(root, text="Name:",font=("Times New Roman", 15)).grid(column=1, row=2)
labelAge = tk.Label(root, text="Age:",font=("Times New Roman", 15)).grid(column=1, row=3)
labelEmail = tk.Label(root, text="Email:",font=("Times New Roman", 15)).grid(column=1, row=4)

entryNameValue = tk.StringVar()
entryTextName = ttk.Entry(root, textvariable=entryNameValue).grid(column=2, row=2,padx=10)

age_value = tk.StringVar(value=0)
spinboxAge= tk.Spinbox(root,from_=0,to=60,textvariable=age_value,wrap=False).grid(column=2, row=3,padx=10)

entryEmail = tk.StringVar()
entryTextName = ttk.Entry(root, textvariable=entryEmail).grid(column=2, row=4,padx=10)








def clickAdd():
    print("add")
    nameInput=entryNameValue.get()
    ageInput=age_value.get()
    emailInput=entryEmail.get()
    api_endpoint="http://127.0.0.1:8000/saveStudent"
    
    paramsInput = {'name':nameInput,'age':ageInput,'email':emailInput}
    
    req = requests.post(url = api_endpoint, params= paramsInput)
    print(req.text)
    
addButton=tk.Button(root,text="Add",command=clickAdd)
addButton.grid(column=1,row=5)

    

def clickDelete():
    print("delete")
deleteButton=tk.Button(root,text="Delete",command=clickDelete)
deleteButton.grid(column=4,row=5)   
    
def clickUpdate():
    print("update")
updateButton=tk.Button(root,text="update",command=clickUpdate)
updateButton.grid(column=3,row=5)
   
def clickEdit():
    print("edit")   
editButton=tk.Button(root,text="Edit",command=clickEdit)
editButton.grid(column=2,row=5)


root.mainloop()


'''

def click(event):
    print("Save")
    btn = tk.Button(root, text='Save')
    btn.grid(column=4,row=10)
    btn.bind('<Button-1>',click)
    btn.focus()
    '''
    
