import pymysql
import os
import random

connection = pymysql.connect(host='localhost',
    user='root',
    password='@z1m[N9C',
    database='ecommerce2')

cursor = connection.cursor()

a=0

while (a!=3) :
    print ("-------WELCOME------\n")
    print ("1. Login")
    print("2. Register")
    print ("3. Exit")
    a=input ("Choice : ")
    if (a==1) :
        os.system('cls')
        print ("------LOGIN------\n")
        print ("Select \n1. for Customer\n 2. for Admin\n 3. for Supplier")
        b=input("Choice : ")
        if (b==1) :
            Username=input("Enter Username : ")
            Password=input("Enter password : ")

            q="select customer_id from customers where username= '" + Username + "' AND password= '" + Password + "'"
            cursor.execute(q)
            res= cursor.fetchone()
            c=str(res)
            if (c=="None") :
                print ("No Customer Found with the following details.")
            else :
                e=0
                while (e==0) :
                    print ("---------eCommerceStore.0--------\n")
                    print ("Select :")
                    print ("1. View Cart")
                    print ("2. Edit Cart")
                    print ("3. Add product to Cart")
                    print ("4. View products")
                    print ("5. View Category")
                    print ("6. Add card details")
                    print ("7. Edit card details")
                    print ("8. View available coupons")
                    print ("9. Apply a coupon to the cart")
                    print ("10. Place order")
                    print ("11. View order details")
                    print ("12. Exit")
                    d=int(input("Choice : "))
                    if (d==1) :
                        q="select product_id, no_of_items, total_cost from cart_section where customer_id= " + c + ""
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)
                    
                    elif (d==2) :
                        p_id=input("Enter Product ID to update")
                        p_n=input("Enter Number of Products")
                        if (p_n > 0):
                            q="Update Cart_section set no_of_items = " + p_n + "where product_id = " + p_id
                            cursor.execute(q)
                            connection.commit()
                        
                        else:
                            q = "delete from cart_section where product_id = " + p_id
                            cursor.execute(q)
                            connection.commit()

                    elif (d==3) :
                        p_id = input("Enter product id: ")
                        p_n=input("Enter Number of Products")
                        tc = random.uniform(50, 20000)
                        amount = round(amount, 2)

                        q = "insert into cart_section values(" + p_n + ", " + str(amount) + ", " + p_id + ")"
                        cursor.execute(q)
                        connection.commit()
                    
                    elif (d==4) :
                        q = "select * from products"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==5) :
                        q = "select * from categories"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==6) :
                        continue

                    elif (d==7) :
                        pcard = input('Enter previous card details: ')
                        ncard = input("Enter new card details: ")

                        q = " update payment set card_deatils = '" + ncard + "' where card_details = '" + pcard + "'"
                        cursor.execute(q)
                        connection.commit()

                    elif (d==8) :
                        q = "select * from coupons"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==9) :
                        co_id = input("Enter coupon id: ")
                        q = "select * from coupons where coupon_id = " + co_id
                        cursor.execute(q)
                        res = cursor.fetchone()

                        discount = res[2]
                        discount = float(discount)
                        discount = round(discount, 2)

                        q = "select * from "

                    elif (d==10) :
                        continue

                    elif (d==11) :
                        q = "select * from orders"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)
                    
                    elif (d==12) :
                        e=1

                    elif (d!=12) :
                        print ("Please Enter a Valid Choice.")



            

        elif (b==2) :
            Admin_id=input("Enter Admin ID : ")
            Admin_name=input("Enter Admin Name : ")

            q="select admin_id from Administration where admin_id= " + Admin_id + " AND admin_name= '" + Admin_name + "' "
            cursor.execute(q)
            res=cursor.fetchone()
            c=str(res)
            if (c=="None") :
                print ("No Admin Found with the following details.")
            else :
                e=0
                while (e==0) :
                    print ("----------------eCommerceStore.0----------------\n")
                    print ("Select : ")
                    print ("1. View Customers")
                    print ("2. View Products")
                    print ("3. View suppliers")
                    print ("4. Modify Coupons")
                    print ("5. View Details of Delivery Section")
                    print ("6. View payment Details")
                    print ("7. Exit")
                    d=int(input("Choice : "))
                    if (d==1) :
                        q = "select * from customers"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==2) :
                        q = "select * from products"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==3) :
                        q = "select * from suppliers"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==4) :
                        continue
                    elif (d==5) :
                        q = "select * from delivery_section"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==6) :
                        q = "select * from payment"
                        cursor.execute(q)
                        res = cursor.fetchall()
                        for r in res:
                            print(r)

                    elif (d==7) :
                        e=1

                    elif (d!=7) :
                        print ("Please Enter a Valid Choice.")









        elif (b==3) :
            Suppliers_id=input("Enter Supplier ID : ")
            Suppliers_name=input("Enter Supplier Name : ")
            
            q="select suppliers_id from Suppliers where suppliers_id= " + Suppliers_id + " AND suppliers_name= '" + Suppliers_name + "'"
            cursor.execute(q)
            res=cursor.fetchone()
            c=str(res)
            if (c=="None") :
                print ("No Supplier found with the following details.")
            else:
                e=0
                while (e==0) :
                    print ("---------------------eCommerceStore.0---------------------\n")
                    print ("Select : ")
                    print ("1. Add New Products")
                    print ("2. Modify Product Name")
                    print ("3. Modify Product Count")
                    print ("4. Modify Product Price")                
                    print ("5. Modify Product Description")
                    print ("6. Modify Product stock")                                  
                    print ("7. Exit")
                    d=int(input("Choice : ")) 
                    if (d==1) :
                        q = "select * from products where product_id = (select max(product_id) from products)"
                        cursor.execute(q)
                        res = cursor.fetchone()
                        pid = res[1] + 1

                        name = input("Enter name: ")
                        count = input("Enter count: ")
                        price = input("Enter price: ")
                        desc = input("Enter description: ")
                        stock = input("Enter stock: ")
                        mdate = input("Manufacturing date: ")
                        edate = input("expiry_date: ")

                        q = "insert into products values(100, " + pid + ", '" + name + "', " + count + ", " + price + ", '" + desc + "', '" + stock + "', " + mdate + ", " + edate + ")"
                        cursor.execute(q)
                        connection.commit()

                    elif (d==2) :
                        pid = input("Enter product id: ")
                        name = input("Enter new name: ")

                        q = "update products set p_name = '" + name + "' where product_id = " + pid
                        cursor.execute(q)
                        print("Name modified")
                        

                    elif (d==3) :
                        pid = input("Enter product id: ")
                        count = input("Enter new count: ")

                        q = "update products set count = '" + count + "' where product_id = " + pid
                        cursor.execute(q)
                        print("Count modified")

                    elif (d==4) :
                        pid = input("Enter product id: ")
                        price = input("Enter new price: ")

                        q = "update products set price = '" + price + "' where product_id = " + pid
                        cursor.execute(q)
                        print("Price modified")

                    elif (d==5) :
                        pid = input("Enter product id: ")
                        desc = input("Enter new description: ")

                        q = "update products set description = '" + desc + "' where product_id = " + pid
                        cursor.execute(q)
                        print("Description modified")

                    elif (d==6) :
                        pid = input("Enter product id: ")
                        stock = input("Enter new stock: ")

                        q = "update products set stock = '" + stock + "' where product_id = " + pid
                        cursor.execute(q)
                        print("Stock modified")

                    elif (d==7) :
                        e =1
      

                    elif (d!=7) :
                        print ("Please Enter a Valid Choice.")             










        else :
            print ("Enter a Valid choice.")
    elif (a==2) :
        print ("------REGISTER------\n")
        print ("Enter Customer Details :")

        q = "select * from customers where customer_id = (select max(customer_id) from customers)"
        cursor.execute(q)
        res = cursor.fetchone()

        customer_id= res[0] + 1
        first_name=input("Enter First Name : ")
        last_name=input("Enter Last Name : ")
        username=input("Enter Username : ")
        password=input("Enter password : ")
        contact_info=input("Enter Contact Info :")

        q = "insert into customers valuse(" + customer_id + ", '" + first_name + "', '" + last_name + "', '" + username + "', '" + password + "', '" + contact_info + "')"
        cursor.execute(q)
        connection.commit()

        print("Successfully Registered")

    elif (a!=3) :
        print ("Enter a Valid choice.")