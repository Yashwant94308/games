from tkinter import *
from variables import Variable


class Bill_APP:
    def __init__(self, roots, variable):
        self.root = roots
        self.var = variable
        self.root.geometry("1350x710+0+0")
        self.root.title("Bill Management app")
        bg_color = "#074463"
        title = Label(self.root, text="Billing software", bd=12, bg=bg_color, fg="white",
                      relief=GROOVE, font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # =============================customer detail============================ #

        f1 = LabelFrame(self.root, text="Costumer detail", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f1.place(x=0, y=80, relwidth=1)
        c_name = Label(f1, text="Customer name", font=("times new roman", 18, "bold"),
                       bg=bg_color, fg="white").grid(row=0, column=0, padx=20, pady=5)
        c_text = Entry(f1, width=16, textvariable=self.var.customer_name, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=1)

        c_phn = Label(f1, text="Phone No.", font=("times new roman", 18, "bold"),
                      bg=bg_color, fg="white").grid(row=0, column=2, padx=20, pady=5)
        c_phn_text = Entry(f1, width=16, textvariable=self.var.customer_phone, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=0, column=3)

        bill_number = Label(f1, text="Bill Number", font=("times new roman", 18, "bold"),
                            bg=bg_color, fg="white").grid(row=0, column=4, padx=20, pady=5)
        bill_text = Entry(f1, width=16, textvariable=self.var.bill_number, font=("arial", 15), bd=7,
                          relief=SUNKEN).grid(row=0, column=5)

        search_button = Button(f1, width=10, bg="lightyellow", text="Search", font=("times new roman", 18, "bold"),
                               bd=7, relief=SUNKEN).grid(row=0, column=6, padx=20)

        # ==================================products=================================

        # ============================Cosmetics=====================================

        f2 = LabelFrame(self.root, text="Cosmetics", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f2.place(x=0, y=180, height=380)

        b_shop = Label(f2, text="Bath Shop", font=("times new roman", 15, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=20, pady=5, sticky="w")
        b_shop_text = Entry(f2, width=10, textvariable=self.var.soap, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=0, column=1, padx=20, pady=10, sticky="w")

        f_cream = Label(f2, text="Face Cream", font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=20, pady=5, sticky="w")
        f_cream_text = Entry(f2, width=10, textvariable=self.var.face_cream, font=("arial", 15), bd=7,
                             relief=SUNKEN).grid(row=1, column=1, padx=20, pady=10, sticky="w")

        f_wash = Label(f2, text="Face wash", font=("times new roman", 15, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=20, pady=5, sticky="w")
        f_wash_text = Entry(f2, width=10, textvariable=self.var.face_wash, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=2, column=1, padx=20, pady=10)

        h_spray = Label(f2, text="Hair Spray", font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=20, pady=5, sticky="w")
        h_spray_text = Entry(f2, width=10, textvariable=self.var.hair_spray, font=("arial", 15), bd=7,
                             relief=SUNKEN).grid(row=3, column=1, padx=20, pady=10)

        h_gel = Label(f2, text="Hair Gel", font=("times new roman", 15, "bold"),
                      bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=20, pady=5, sticky="w")
        h_gel_text = Entry(f2, width=10, textvariable=self.var.hair_gel, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=4, column=1, padx=20, pady=10)

        b_lotion = Label(f2, text="Body Lotion", font=("times new roman", 15, "bold"),
                         bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=20, pady=5, sticky="w")
        b_lotion_text = Entry(f2, width=10, textvariable=self.var.body_lotion, font=("arial", 15), bd=7,
                              relief=SUNKEN).grid(row=5, column=1, padx=20, pady=10)

        # ===========================Grocery===========================================================

        f3 = LabelFrame(self.root, text="Grocery", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f3.place(x=340, y=180, height=380)
        rice = Label(f3, text="Rice", font=("times new roman", 15, "bold"),
                     bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=20, pady=5, sticky="w")
        rice_text = Entry(f3, width=10, textvariable=self.var.rice, font=("arial", 15), bd=7,
                          relief=SUNKEN).grid(row=0, column=1, padx=30, pady=10)

        f_oil = Label(f3, text="Food Oil", font=("times new roman", 15, "bold"),
                      bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=20, pady=5, sticky="w")
        f_oil_text = Entry(f3, width=10, textvariable=self.var.food_oil, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=1, column=1, padx=30, pady=10)

        daal = Label(f3, text="Daal", font=("times new roman", 15, "bold"),
                     bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=20, pady=5, sticky="w")
        daal_text = Entry(f3, width=10, textvariable=self.var.daal, font=("arial", 15), bd=7,
                          relief=SUNKEN).grid(row=2, column=1, padx=30, pady=10)

        wheat = Label(f3, text="Wheat", font=("times new roman", 15, "bold"),
                      bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=20, pady=5, sticky="w")
        wheat_text = Entry(f3, width=10, textvariable=self.var.wheat, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=3, column=1, padx=30, pady=10)

        sugar = Label(f3, text="Sugar", font=("times new roman", 15, "bold"),
                      bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=20, pady=5, sticky="w")
        sugar_text = Entry(f3, width=10, textvariable=self.var.sugar, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=4, column=1, padx=30, pady=10)

        tea = Label(f3, text="Tea", font=("times new roman", 15, "bold"),
                    bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=20, pady=5, sticky="w")
        tea_text = Entry(f3, width=10, textvariable=self.var.tea, font=("arial", 15), bd=7,
                         relief=SUNKEN).grid(row=5, column=1, padx=30, pady=10)

        # =======================================cold drinks============================================

        f4 = LabelFrame(self.root, text="Cold drinks", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f4.place(x=670, y=180, height=380)
        maza = Label(f4, text="Maza", font=("times new roman", 15, "bold"),
                     bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=20, pady=5, sticky="w")
        maza_text = Entry(f4, width=10, textvariable=self.var.maza, font=("arial", 15), bd=7,
                          relief=SUNKEN).grid(row=0, column=1, padx=30, pady=10)

        c_cola = Label(f4, text="Coco cola", font=("times new roman", 15, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=20, pady=5, sticky="w")
        c_cola_text = Entry(f4, width=10, textvariable=self.var.coco_cola, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=1, column=1, padx=30, pady=10)

        frooti = Label(f4, text="Frooti", font=("times new roman", 15, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=20, pady=5, sticky="w")
        frooti_text = Entry(f4, width=10, textvariable=self.var.frooti, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=2, column=1, padx=30, pady=10)

        t_up = Label(f4, text="Thumbs Up", font=("times new roman", 15, "bold"),
                     bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=20, pady=5, sticky="w")
        t_up_text = Entry(f4, width=10, textvariable=self.var.thumbs_up, font=("arial", 15), bd=7,
                          relief=SUNKEN).grid(row=3, column=1, padx=30, pady=10)

        limca = Label(f4, text="Limca", font=("times new roman", 15, "bold"),
                      bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=20, pady=5, sticky="w")
        limca_text = Entry(f4, width=10, textvariable=self.var.limca, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=4, column=1, padx=30, pady=10)

        sprite = Label(f4, text="Sprite", font=("times new roman", 15, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=20, pady=5, sticky="w")
        sprite_text = Entry(f4, width=10, textvariable=self.var.sprite, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=5, column=1, padx=30, pady=10)

        # ======================Bill area==================================================================

        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1020, y=180, width=330, height=380)
        bill_title = Label(f5, bg="cadetblue", text="Bill Area", font=("arial", 15, "bold"),
                           bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(f5, orient=VERTICAL)
        self.txtarea = Text(f5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ========================================Bill menu===========================

        f6 = LabelFrame(self.root, text="Bill Menu", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f6.place(x=0, y=560, relwidth=1, relheight=1)

        t_c_prize = Label(f6, text="Total Cosmetics Prize", font=("times new roman", 13, "bold"),
                          bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=20, sticky="w")
        t_c_prize_text = Entry(f6, width=10, textvariable=self.var.total_cosmetic_price, font=("arial", 15), bd=7,
                               relief=SUNKEN).grid(row=0, column=1, padx=30)
        t_g_prize = Label(f6, text="Total Grocery Prize", font=("times new roman", 13, "bold"),
                          bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=20, sticky="w")
        t_g_prize_text = Entry(f6, width=10, textvariable=self.var.total_grocery_price, font=("arial", 15), bd=7,
                               relief=SUNKEN).grid(row=1, column=1, padx=30)
        t_cd_prize = Label(f6, text="Total Cold Drink Prize", font=("times new roman", 13, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=20, sticky="w")
        t_cd_prize_text = Entry(f6, width=10, textvariable=self.var.total_cold_drinks_price, font=("arial", 15), bd=7,
                                relief=SUNKEN).grid(row=2, column=1, padx=30)

        # ================================================tax==========================================

        c_tax = Label(f6, text="Cosmetics Tax", font=("times new roman", 13, "bold"),
                      bg=bg_color, fg="lightgreen").grid(row=0, column=2, padx=20, sticky="w")
        c_tax_text = Entry(f6, width=10, textvariable=self.var.cosmetic_tax, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=0, column=3, padx=30)
        g_tax = Label(f6, text="Grocery Tax", font=("times new roman", 13, "bold"),
                      bg=bg_color, fg="lightgreen").grid(row=1, column=2, padx=20, sticky="w")
        g_tax_text = Entry(f6, width=10, textvariable=self.var.grocery_tax, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=1, column=3, padx=30)
        cd_tax = Label(f6, text="Cold Drink Tax", font=("times new roman", 13, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=2, column=2, padx=20, sticky="w")
        cd_tax_text = Entry(f6, width=10, textvariable=self.var.cold_drinks_tax, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=2, column=3, padx=30)

        # ======================================BUTTONS====================================================

        f7 = Frame(f6, bd=7, relief=GROOVE)
        f7.place(x=740, width=595, height=117)
        total = Button(f7, text="Total", fg="white", bg="cadetblue", font=("arial", 15, "bold"), width=10,
                       pady=25, bd=3, relief=SUNKEN).grid(row=0, column=0, padx=5, pady=5)
        total = Button(f7, text="Generate Bill", fg="white", bg="cadetblue", font=("arial", 15, "bold"), width=11,
                       pady=25, bd=3, relief=SUNKEN).grid(row=0, column=1, padx=5, pady=5)
        total = Button(f7, text="Clear", fg="white", bg="cadetblue", font=("arial", 15, "bold"), width=10,
                       pady=25, bd=3, relief=SUNKEN).grid(row=0, column=2, padx=5, pady=5)
        total = Button(f7, text="Exit", fg="white", bg="cadetblue", font=("arial", 15, "bold"), width=10,
                       pady=25, bd=3, relief=SUNKEN).grid(row=0, column=3, padx=5, pady=5)


root = Tk()
var = Variable()
obj = Bill_APP(root, var)
root.mainloop()
