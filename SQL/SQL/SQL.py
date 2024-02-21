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
                                       user='Bapll',
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
        pw = input("password: ")
        pw2 = input("Repeat Password: ")
        if (pw == pw2): passwordready = True
        else: 
            clear()
            print("Passwords don't match!")

    clear()

    myCursor.execute("insert into users(name, password) values(%s, %s)", (un, pw))  
    print("User Created")
    conn.commit()
    print(myCursor)


    

if __name__ == '__main__':
    register()


    


