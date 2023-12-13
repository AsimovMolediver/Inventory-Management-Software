import Stock_Level_Tracking
import Button1
import Button2
import Button3
import Button4
import Button5
import Button6
import Button7

while True:

    Stock_Level_Tracking.stock_lvl()

    print("""
    Welcome!

    Please, select your option:

    1 - Add
    2 - Update Item
    3 - Supplier Management
    4 - Inventory Valuation
    5 - Purchase order
    6 - Barcode reader
    7 - Sales and History
    0 - exit
    """)

    action = input('')

    if action == '1':
        
        Button1.opt1()

    elif action =='2':

        Button2.opt2()

    elif action == '3':

        Button3.opt3()

    elif action == '4':

        Button4.opt4()

    elif action == '5':

        Button5.opt5()
    
    elif action == '6':

        Button6.opt6()
    
    elif action == '7':
        Button7.opt7()

    elif action == '0':
        break