import customtkinter as ctk

app= ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
app.configure( bg_color= "white", fg_color= "white")

calcFrame = ctk.CTkFrame(master=app, width=340, height= 70,
                         bg_color="white" , fg_color="white")
calcFrame.grid(row=0, column=0, padx=5, pady=5)

calcLabel=ctk.CTkLabel(master=calcFrame,text="0", width= 330, height= 70,
                       anchor="e", font=ctk.CTkFont(size=50),
                       bg_color= "white", fg_color= "white")
calcLabel.grid(row=0, column=0, padx=5)

btnFrame = ctk.CTkFrame(master=app, width=340, height= 400)
btnFrame.grid(row=1, column=0, padx=5, pady=5)

# row = 0
btnCE= ctk.CTkButton(master=btnFrame, text="CE", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnCE.grid(row=0, column=0, padx=2, pady=2)

btnBack= ctk.CTkButton(master=btnFrame, text="<--", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnBack.grid(row=0, column=1, padx=2, pady=2)

btnpercent= ctk.CTkButton(master=btnFrame, text="%", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnpercent.grid(row=0, column=2, padx=2, pady=2)

btndivid= ctk.CTkButton(master=btnFrame, text="/", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btndivid.grid(row=0, column=3, padx=2, pady=2)

btnseven= ctk.CTkButton(master=btnFrame, text="7", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnseven.grid(row=1, column=0, padx=2, pady=2)

btneight= ctk.CTkButton(master=btnFrame, text="8", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btneight.grid(row=1, column=1, padx=2, pady=2)

btnnine= ctk.CTkButton(master=btnFrame, text="9", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnnine.grid(row=1, column=2, padx=2, pady=2)

btnmultiplcation= ctk.CTkButton(master=btnFrame, text="x", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnmultiplcation.grid(row=1, column=3, padx=2, pady=2)

btnfour= ctk.CTkButton(master=btnFrame, text="4", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnfour.grid(row=2, column=0, padx=2, pady=2)

btnfive= ctk.CTkButton(master=btnFrame, text="5", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnfive.grid(row=2, column=1, padx=2, pady=2)

btnsix= ctk.CTkButton(master=btnFrame, text="6", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnsix.grid(row=2, column=2, padx=2, pady=2)

btnsubtraction= ctk.CTkButton(master=btnFrame, text="-", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnsubtraction.grid(row=2, column=3, padx=2, pady=2)

btnone= ctk.CTkButton(master=btnFrame, text="1", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnone.grid(row=3, column=0, padx=2, pady=2)

btntwo= ctk.CTkButton(master=btnFrame, text="2", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btntwo.grid(row=3, column=1, padx=2, pady=2)

btnthree= ctk.CTkButton(master=btnFrame, text="3", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnthree.grid(row=3, column=2, padx=2, pady=2)

btnplus= ctk.CTkButton(master=btnFrame, text="+", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnplus.grid(row=3, column=3, padx=2, pady=2)

btnaddingaminus= ctk.CTkButton(master=btnFrame, text="+/-", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnaddingaminus.grid(row=4, column=0, padx=2, pady=2)

btnzero= ctk.CTkButton(master=btnFrame, text="0", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnzero.grid(row=4, column=1, padx=2, pady=2)

btndecimaldot= ctk.CTkButton(master=btnFrame, text=".", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btndecimaldot.grid(row=4, column=2, padx=2, pady=2)

btnequalsign= ctk.CTkButton(master=btnFrame, text="=", width=75, height=65,
                        font=ctk.CTkFont(size=30),
                       fg_color="gray", bg_color="white")
btnequalsign.grid(row=4, column=3, padx=2, pady=2)

app.mainloop()