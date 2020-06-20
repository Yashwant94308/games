from tkinter import *


class Variable:
    def __init__(self):
        # =========================================customer details=============================
        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        self.bill_number = StringVar()

        # ============================================cosmetics================================

        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.hair_gel = IntVar()
        self.body_lotion = IntVar()

        # ==========================================grocery=====================================

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ============================================cold drinks====================================

        self.maza = IntVar()
        self.coco_cola = IntVar()
        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ===========================================total====================================

        self.total_cosmetic_price = StringVar()
        self.total_grocery_price = StringVar()
        self.total_cold_drinks_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
