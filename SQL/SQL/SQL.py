import mysql.connector
from mysql.connector import Error
import os
import tkinter as tk

def clear():
    print("\n"*100)

def connect():
    clear()
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='bapll',
                                       user='bapll',
                                       password='1234')
    except Error as e:
        print("fejl")
        print(e)
    
    finally:
       if conn is not None and conn.is_connected():
           print('Connected to MySQL database')
           clear()
           
           #myCursor.execute("SHOW TABLES")

           return conn

       else: return None

def login():
    conn = connect()
    if not conn.is_connected(): return
    logged_in = False

def evaluate_password(p):
    import re

    regex = r"(?=.*[a-zæøå])(?=.*[A-ZÆØÅ])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?])(?!.*\s)(?=.*Batman)(?=.*XD)(?=.*69)(?=.*420).{8,22}"
    return bool(re.match(regex, p))


def register():
 
    conn = connect()
    if not conn.is_connected(): return

    nameready = False
    while not nameready:
        un = input("username: ")
        
        myCursor = conn.cursor()
        myCursor.execute("create table if not exists users(id int primary key auto_increment, name varchar(255), password varchar(255) )")
        
        myCursor.execute("SELECT * FROM users WHERE name = %s", (un,))
        if (len(myCursor.fetchall()) <= 0): nameready = True
        else: 
            clear()


            print("Username is already taken :C")

    clear()

    passwordready = False
    while not passwordready:
        print("Password Requirements: \n- At least one upper case letter\n- At least one lower case letter\n- At least one number\n- At least one special character\n- At least 8 characters long\n- At most 22 characters long\n- All of the following words: Batman, XD, 69, 420")
        pw = input("password: ")
        if (evaluate_password(pw)):
            pw2 = input("Repeat Password: ")
            if (pw == pw2): passwordready = True
            else: 
                clear()
                print("Passwords don't match!")
        else: 
            clear()
            print("Password does not meet requirements! Try again")
        

    clear()

    myCursor.execute("insert into users(name, password) values(%s, %s)", (un, pw))  
    print("User Created")
    conn.commit()
    print(myCursor)


    

if __name__ == '__main__':
    register()


    


