import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

root=tk.Tk()
root.title("PYPT graphs")
root.geometry("400x1000")

def enable_dark_mode():
 choice=var2.get()
 if choice==1:
  plt.style.use('dark_background')
 elif choice==0:
  plt.style.use('default')


def another_graph():
 global label6,label7,label8,label9,entry6,entry7,entry8,entry9
 choice=var.get()
 if choice==1:

  label6=tk.Label(root, text="Enter y-values", font=("Times New Roman",10))
  label6.pack(pady=10)

  entry6=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
  entry6.pack(pady=10)

  label7=tk.Label(root, text="Enter error bar for y values", font=("Times New Roman",10))
  label7.pack(pady=10)

  entry7=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
  entry7.pack(pady=10)

  label8=tk.Label(root, text="enter title for line 1", font=("Times New Roman",10))
  label8.pack(pady=10)

  entry8=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
  entry8.pack(pady=10)

  label9=tk.Label(root, text="enter title for line 2", font=("Times New Roman",10))
  label9.pack(pady=10)

  entry9=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
  entry9.pack(pady=10)
  
  button2=tk.Button(root, text="create graph with now two lines", command=graph2)
  button2.pack()

def graph2():
 x=[]
 y=[]
 y2=[]
 a = entry1.get().split(",")
 for i in range(len(a)):
  x.append(float(a[i]))

 b = entry2.get().split(",")
 for i in range(len(b)):
   y.append(float(b[i]))
 y_err = float(entry3.get())  

 c = entry6.get().split(",")
 for i in range(len(c)):
   y2.append(float(c[i]))

 y2_err = float(entry7.get())  
 fig, ax = plt.subplots()

 ax.errorbar(x, y, yerr=y_err,label=entry8.get() ,color="red", fmt='o-', markersize=4, capsize=5, capthick=1)
 ax.errorbar(x, y2, yerr=y2_err, label=entry9.get(),color="blue", fmt='o-', markersize=4, capsize=5, capthick=1)
 ax.set_xlabel(entry4.get())
 ax.set_ylabel(entry5.get())

 ax.legend()
 plt.show()

def graph():
 x=[]
 y=[]
 x_vals = entry1.get().split(",")
 for i in range(len(x_vals)):
  x.append(float(x_vals[i]))

 y_vals = entry2.get().split(",")
 for i in range(len(y_vals)):
   y.append(float(y_vals[i]))
 y_err = float(entry3.get())  

 fig, ax = plt.subplots()

 ax.errorbar(x, y, yerr=y_err ,color="red", fmt='o-', markersize=4, capsize=5, capthick=1)
 ax.set_xlabel(entry4.get())
 ax.set_ylabel(entry5.get())

 ax.legend()
 plt.show()

label1=tk.Label(root, text="Enter x-values seperated by a comma", font=("Times New Roman",10))
label1.pack(pady=10)

entry1=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
entry1.pack(pady=10)

label2=tk.Label(root, text="Enter y-values seperated by a comma", font=("Times New Roman",10))
label2.pack(pady=10)

entry2=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
entry2.pack(pady=10)

label3=tk.Label(root, text="Enter error bars for y", font=("Times New Roman",10))
label3.pack(pady=10)

entry3=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
entry3.pack(pady=10)

label4=tk.Label(root, text="Enter title for x values", font=("Times New Roman",10))
label4.pack(pady=10)

entry4=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
entry4.pack(pady=10)

label5=tk.Label(root, text="Enter title for y values", font=("Times New Roman",10))
label5.pack(pady=10)

entry5=tk.Entry(root,width=48, borderwidth=4, font=("Times New Roman", 10))
entry5.pack(pady=10)

button=tk.Button(root, text="create graph with one line", command=graph)
button.pack()
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Enter another graph", variable=var, onvalue=1, offvalue=0,command=another_graph)
checkbutton.pack()
var2 = tk.IntVar()
checkbutton2 = tk.Checkbutton(root,text="Dark Mode", variable=var2, onvalue=1, offvalue=0,command=enable_dark_mode)
checkbutton2.pack()
root.mainloop()