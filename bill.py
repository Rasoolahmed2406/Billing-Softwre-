from tkinter import *
import math,random
from tkinter import messagebox
import os 

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        title = Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg="cadetblue",fg="black",font=("times new roma",30,"bold"),pady=2).pack(fill=X)

#=========================Vairiable========================================================================================================

#=========================Cosmetics=========================================================================================================
        self.soap = IntVar()
        self.face_cream  = IntVar()
        self.face_wash  = IntVar()
        self.spray  = IntVar()
        self.gell  = IntVar()
        self.loshan  = IntVar()
        self.shampoo  = IntVar()
        self.nail_polisf = IntVar()

#=========================Grocery==========================================================================================================
        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.tea = IntVar()
        self.sugar =IntVar()
        self.salt =IntVar()
        self.chili = IntVar()

#=========================Coold Drinks====================================================================================================
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti =  IntVar()
        self.thums_up =  IntVar()
        self.limca =  IntVar()
        self.sprite = IntVar()
        self.mirinda =  IntVar()
        self.slice = IntVar() 

#========================= ===Total Products Price And Tax Variable ======================================================================
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_derink_price =StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_derink_tax =StringVar()

#=========================Custmors ====================================================================================================

        self.c_name =  StringVar()
        self.c_phone =  StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill =  StringVar()

#============================customer Details =============================================================================================

        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="black",bg="lightgrey")
        F1.place(x=0,y=80,relwidth=1)

        cnmae_lbl =Label(F1,text="Customer Name",bg="lightgrey",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5)

        cphn_lbl =Label(F1,text=" Cell No",bg="lightgrey",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt = Entry(F1,width=20,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5)

        bill_lbl =Label(F1,text="Bill NO",bg="lightgrey",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        bill_txt = Entry(F1,width=20,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5)

        bill_btn = Button(F1,text="Search",width=20,command=self.find_bill,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=80,pady=5)

#============================Cosmetic Frame =============================================================================================

        F2 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),bg="lightgrey")
        F2.place(x=5,y=180,width=325,height=480)

        bath_lbl = Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=0,column=1,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=2,padx=10,pady=10)

        face_lbl = Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=1,column=1,padx=10,pady=10,sticky="w")
        face_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=10)

        face_w_lbl = Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=2,column=1,padx=10,pady=10,sticky="w")
        face_w_txt = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=10)

        hair_lbl = Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=3,column=1,padx=10,pady=10,sticky="w")
        hair_txt = Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)

        hair_s_lbl = Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=4,column=1,padx=10,pady=10,sticky="w")
        hair_s_txt = Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=10)

        loshan_lbl = Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=5,column=1,padx=10,pady=10,sticky="w")
        loshan_txt = Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=2,padx=10,pady=10)

        shampoo_lbl = Label(F2,text="Hair Shampoo",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=6,column=1,padx=10,pady=10,sticky="w")
        shampoo_txt = Entry(F2,width=10,textvariable=self.shampoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=2,padx=10,pady=10)

        nail_lbl = Label(F2,text="Nail Polish",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=7,column=1,padx=10,pady=10,sticky="w")
        nail_txt = Entry(F2,width=10,textvariable=self.nail_polisf,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=2,padx=10,pady=10)
        #=======================================Grosory products =====================================================

        F3 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),bg="lightgrey")
        F3.place(x=340,y=180,width=325,height=480)

        rice_lbl = Label(F3,text="Rice",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=0,column=1,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=2,padx=10,pady=10)

        oil_lbl = Label(F3,text="Food oil",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=1,column=1,padx=10,pady=10,sticky="w")
        oil_txt = Entry(F3,width=10,textvariable=self.oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=10)

        daal_lbl = Label(F3,text="Daal ",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=2,column=1,padx=10,pady=10,sticky="w")
        daal_txt = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=10)

        wheat_lbl = Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=3,column=1,padx=10,pady=10,sticky="w")
        wheat_txt = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)

        sugar_s_lbl = Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=4,column=1,padx=10,pady=10,sticky="w")
        sugar_s_txt = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=10)

        tea_lbl = Label(F3,text="Tea",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=5,column=1,padx=10,pady=10,sticky="w")
        tea_txt = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=2,padx=10,pady=10)

        
        salt_lbl = Label(F3,text="Salt",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=6,column=1,padx=10,pady=10,sticky="w")
        salt_txt = Entry(F3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=2,padx=10,pady=10)

        chili_lbl = Label(F3,text="chili Powder",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=7,column=1,padx=10,pady=10,sticky="w")
        chili_txt = Entry(F3,width=10,textvariable=self.chili,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=2,padx=10,pady=10)

        #====================================Coold Drinks ===============================================

        F4 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks ",font=("times new roman",15,"bold"),bg="lightgrey")
        F4.place(x=670,y=180,width=325,height=480)

        maza_lbl = Label(F4,text="Maza",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=0,column=1,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=2,padx=10,pady=10)

        cock_lbl = Label(F4,text="Cock",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=1,column=1,padx=10,pady=10,sticky="w")
        cock_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=2,padx=10,pady=10)

        frooti_w_lbl = Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=2,column=1,padx=10,pady=10,sticky="w")
        frooti_w_txt = Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=10)

        thumsUp_lbl = Label(F4,text="Thums Up",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=3,column=1,padx=10,pady=10,sticky="w")
        thumsUp_txt = Entry(F4,width=10,textvariable=self.thums_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)

        limca_s_lbl = Label(F4,text="Limca",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=4,column=1,padx=10,pady=10,sticky="w")
        limca_s_txt = Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=10)

        sprite_lbl = Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=5,column=1,padx=10,pady=10,sticky="w")
        sprite_txt = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=2,padx=10,pady=10)

        mirinda_lbl = Label(F4,text="Mirinda",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=6,column=1,padx=10,pady=10,sticky="w")
        mirinda_txt = Entry(F4,width=10,textvariable=self.mirinda,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=2,padx=10,pady=10)

        slice_lbl = Label(F4,text="Slice",font=("times new roman",16,"bold"),bg="lightgrey",fg="black").grid(row=7,column=1,padx=10,pady=10,sticky="w")
        slice_txt = Entry(F4,width=10,textvariable=self.slice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=2,padx=10,pady=10)

        #====================================bill Area =================================================
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=520,height=480)
        bill_title = Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=True)

        #=================Button Frame =======================================
        F6 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="black",bg="lightgrey")
        F6.place(x=0,y=660,relwidth=1,height=140)

        m1_lbl = Label(F6,text="Total Cosmetic Price",bg="lightgrey",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6,text="Total Grocery Price",bg="lightgrey",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt = Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl = Label(F6,text="Total Cold Driks Price",bg="lightgrey",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt = Entry(F6,width=18,textvariable=self.cold_derink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl = Label(F6,text=" Cosmetic Tax",bg="lightgrey",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt = Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl = Label(F6,text=" Grocery Tax",bg="lightgrey",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt = Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl = Label(F6,text=" Cold Driks Tax",bg="lightgrey",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt = Entry(F6,width=18,textvariable=self.cold_derink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        #===============================Button Frame ====================================================
        
        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=780,width=730,height=105)

        total_btn = Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="Black",bd=5,pady=15,width=13,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)

        bill_btn = Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="Black",bd=5,pady=15,width=13,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)

        clear_btn = Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="Black",bd=5,pady=15,width=12,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)

        exit_btn = Button(btn_F,text="Exit",command=self.Exita_app,bg="cadetblue",fg="Black",bd=5,pady=15,width=13,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcom_bill()

#============================================================================================================================

    def total(self):
            self.c_s_p = self.soap.get()*40
            self.c_fc_p =self.face_cream.get()*120
            self.C_fw_p = self.face_wash.get()*60
            self.c_sp_p = self.spray.get()*180
            self.c_g_p = self.gell.get()*140
            self.c_l_p = self.loshan.get()*180
            self.c_sh_p = self.shampoo.get()*120
            self.c_n_p = self.nail_polisf.get()*150

            self.total_cosmetic_price=float(
                                   self.c_s_p+
                                   self.c_fc_p+
                                   self.C_fw_p+
                                   self.c_sp_p+
                                   self.c_g_p+
                                   self.c_l_p+
                                   self.c_sh_p+
                                   self.c_n_p
                                  )

            self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
            self.c_tax = round((self.total_cosmetic_price*0.05),2)
            self.cosmetic_tax.set("Rs. "+str(self.c_tax))


            self.g_r_p = self.rice.get()*50
            self.g_o_p = self.oil.get()*170
            self.g_d_p= self.daal.get()*160
            self.g_w_p = self.wheat.get()*180
            self.g_s_p = self.sugar.get()*40
            self.g_t_p = self.tea.get()*200
            self.g_sl_p = self.salt.get()*10
            self.g_c_p = self.chili.get()*150

            self.total_grocery_price = float(
                                        self.g_r_p+
                                        self.g_o_p+
                                        self.g_d_p+
                                        self.g_w_p+
                                        self.g_s_p+
                                        self.g_t_p+
                                        self.g_sl_p+
                                        self.g_c_p 
                                  )
            self.grocery_price.set("Rs. "+str(self.total_grocery_price))
            self.g_tax = round((self.total_grocery_price*0.15),2)
            self.grocery_tax.set("Rs. "+str(self.g_tax))

            self.d_m_p = self.maza.get()*80
            self.d_c_p = self.cock.get()*80
            self.d_f_p = self.frooti.get()*120
            self.d_t_p = self.thums_up.get()*100
            self.d_l_p = self.limca.get()*80
            self.d_s_p = self.sprite.get()*80
            self.d_m_p =self.mirinda.get()*180
            self.d_sl_p = self.slice.get()*150

            self.total_cold_drink_price = float(
                                        self.d_m_p+
                                        self.d_c_p+
                                        self.d_f_p+
                                        self.d_t_p+
                                        self.d_l_p+
                                        self.d_s_p+
                                        self.d_m_p+
                                        self.d_sl_p
                                  )
            self.cold_derink_price.set("Rs. "+str(self.total_cold_drink_price))
            self.d_tax = round((self.total_cold_drink_price*0.03),2)
            self.cold_derink_tax.set("Rs. "+str(self.d_tax))

            self.Total_bill =      float(self.total_cosmetic_price+
                                         self.total_grocery_price+
                                         self.total_cold_drink_price+
                                         self.c_tax+
                                         self.g_tax+
                                         self.d_tax
                                        )
                                        
        
    def welcom_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\t\tWelcom to AR Retail Servises\n\n")
            self.txtarea.insert(END,f"\n Bill Number   :{self.bill_no.get()} ")
            self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()} ")
            self.txtarea.insert(END,f"\n Phone NUmber  :{self.c_phone.get()}")
            self.txtarea.insert(END,f"\n\n===========================================================")
            self.txtarea.insert(END,f"\n Products\t\t\tQTY\t\t\tPrice")
            self.txtarea.insert(END,f"\n===========================================================")

    def bill_area(self):
            if self.c_name.get()=="" or self.c_phone ==0:
                    messagebox.showerror("Eroor","Customer details are empty")
            elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_derink_price.get() =="Rs. 0.0":
                    messagebox.showerror("Erroe","No Products are Selected")

            else:
                self.welcom_bill()
                #===============cosmetics ========================================
                if self.soap.get()!=0:
                        self.txtarea.insert(END,f"\n Bath Soap\t\t\t{self.soap.get()}\t\t\t{self.c_s_p}") 
                
                if self.face_cream.get()!=0:
                        self.txtarea.insert(END,f"\n Face cream \t\t\t{self.face_cream.get()}\t\t\t{self.c_fc_p}")
                
                if self.face_wash.get()!=0:
                        self.txtarea.insert(END,f"\n Face wash \t\t\t{self.face_wash.get()}\t\t\t{self.C_fw_p}")
                
                if self.gell.get()!=0:
                        self.txtarea.insert(END,f"\n Hair Gell \t\t\t{self.gell.get()}\t\t\t{self.c_g_p}")

                if self.spray.get()!=0:
                        self.txtarea.insert(END,f"\n Hair Spray \t\t\t{self.spray.get()}\t\t\t{self.c_sp_p}")

                if self.loshan.get()!=0:
                        self.txtarea.insert(END,f"\n Body loshan \t\t\t{self.loshan.get()}\t\t\t{self.c_l_p}")

                if self.shampoo.get()!=0:
                        self.txtarea.insert(END,f"\n Hair Shampoo \t\t\t{self.shampoo.get()}\t\t\t{self.c_sh_p}")

                if self.nail_polisf.get()!=0:
                        self.txtarea.insert(END,f"\n Nail Poslish \t\t\t{self.nail_polisf.get()}\t\t\t{self.c_n_p}")

                #====================================Grocery =============================================================

                if self.rice.get()!=0:
                        self.txtarea.insert(END,f"\n Rice\t\t\t{self.rice.get()}\t\t\t{self.g_r_p}") 
                
                if self.oil.get()!=0:
                        self.txtarea.insert(END,f"\n Food oil \t\t\t{self.oil.get()}\t\t\t{self.g_o_p}")
                
                if self.daal.get()!=0:
                        self.txtarea.insert(END,f"\n Daal \t\t\t{self.daal.get()}\t\t\t{self.g_d_p}")
                
                if self.wheat.get()!=0:
                        self.txtarea.insert(END,f"\n Wheat \t\t\t{self.wheat.get()}\t\t\t{self.g_w_p}")

                if self.sugar.get()!=0:
                        self.txtarea.insert(END,f"\n Sugar \t\t\t{self.sugar.get()}\t\t\t{self.g_s_p}")

                if self.tea.get()!=0:
                        self.txtarea.insert(END,f"\n Tea \t\t\t{self.tea.get()}\t\t\t{self.g_t_p}")

                if self.salt.get()!=0:
                        self.txtarea.insert(END,f"\n Salt \t\t\t{self.salt.get()}\t\t\t{self.g_s_p}")

                if self.chili.get()!=0:
                        self.txtarea.insert(END,f"\n Chilli Powder \t\t\t{self.chili.get()}\t\t\t{self.g_c_p}")

                #========================================cold Drinks ====================================================

                if self.maza.get()!=0:
                        self.txtarea.insert(END,f"\n Maza \t\t\t{self.maza.get()}\t\t\t{self.d_m_p}") 
                
                if self.cock.get()!=0:
                        self.txtarea.insert(END,f"\n Cock \t\t\t{self.cock.get()}\t\t\t{self.d_c_p}")
                
                if self.frooti.get()!=0:
                        self.txtarea.insert(END,f"\n Frooti \t\t\t{self.frooti.get()}\t\t\t{self.d_f_p}")
                
                if self.thums_up.get()!=0:
                        self.txtarea.insert(END,f"\n Thums up \t\t\t{self.thums_up.get()}\t\t\t{self.d_t_p}")

                if self.limca.get()!=0:
                        self.txtarea.insert(END,f"\n Limca \t\t\t{self.limca.get()}\t\t\t{self.d_l_p}")

                if self.sprite.get()!=0:
                        self.txtarea.insert(END,f"\n Sprite \t\t\t{self.sprite.get()}\t\t\t{self.d_s_p}")

                if self.mirinda.get()!=0:
                        self.txtarea.insert(END,f"\n Mirinda \t\t\t{self.mirinda.get()}\t\t\t{self.d_m_p}")

                if self.slice.get()!=0:
                        self.txtarea.insert(END,f"\n Slice \t\t\t{self.slice.get()}\t\t\t{self.d_sl_p}")

        #=====================================================================================================================================
                self.txtarea.insert(END,f"\n-----------------------------------------------------------")
                if self.cosmetic_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t\t\t\tRs{self.cosmetic_tax.get()}")

                if self.grocery_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Grocery Tax\t\t\t\t\t\tRS{self.grocery_tax.get()}")

                if self.cold_derink_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t\t\t\tRs{self.cold_derink_tax.get()}")

                self.txtarea.insert(END,f"\n-----------------------------------------------------------")
                self.txtarea.insert(END,f"\n Total bill  \t\t\t\t\t\tRs {self.Total_bill}")
                self.txtarea.insert(END,f"\n-----------------------------------------------------------")
                self.save_bill()

    def save_bill(self):
            op = messagebox.askyesno("Save Bill","Do you want to save the Bill?")
            if op>0:
                self.bill_data = self.txtarea.get('1.0',END)
                f = open("bills/"+str(self.bill_no.get())+".txt","w")
                f.write(self.bill_data)
                f.close()
                messagebox.showinfo("Saved",f"Bill no: {self.bill_no.get()} Saved Successfully")
            else:
                return

    def find_bill(self):
            present = 'no'
            for i in os.listdir("bills/"):
                    if i.split('.')[0]==self.search_bill.get():
                            f = open(f"bills/{i}","r")
                            self.txtarea.delete('1.0',END)
                            for d in f:
                                self.txtarea.insert(END,d)
                            f.close()
                            present=="yes"
            
            if present=="no":
                    messagebox.showerror("Erro","Invalid Bill NO.")
                    

    def clear_data(self):
#=========================Cosmetics=======================================
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        self.shampoo.set(0)
        self.nail_polisf.set(0)
#=========================Grocery=======================================
        self.rice.set(0)
        self.oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.tea.set(0)
        self.sugar.set(0)
        self.salt.set(0)
        self.chili.set(0)
#=========================Coold Drinks====================================
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thums_up.set(0)
        self.limca.set(0)
        self.sprite.set(0)
        self.mirinda.set(0)
        self.slice.set(0) 
#=========================Total Products Price And Tax Variable ==========================
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_derink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_derink_tax.set("")
#=========================Custmors ===================================
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")

        self.welcom_bill()

    def Exita_app(self):
            op = messagebox.askyesno("Exit","Do you really want Exit ?")
            if op>0:
                    self.root.destroy()
                

root = Tk()
obj = Bill_App(root)
root.mainloop()