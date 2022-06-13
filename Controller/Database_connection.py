import mysql.connector
#import Classes.classLogin
from Classes.classUser import user

def get_connection():
    connection = mysql.connector.connect(user='s206001', password='sSEszSMCHlQGKsYLjxfkm',
                              host='mysql-db.caprover.diplomportal.dk',
                              database='s206001')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def check_username(username):
    connection = get_connection()
    mycursor = connection.cursor()
    query = ("SELECT userName, userPassword FROM s206001.user where userName = %s")
    mycursor.execute(query, (username,))
    myresult=mycursor.fetchall()
    if myresult:
        return True
    else:
        return False

def check_password(username, pw):
    connection = get_connection()
    mycursor = connection.cursor()
    if not check_username(username):
        return (False, "No user found", 0, 0)
    query = ("SELECT userName, userPassword FROM s206001.user where userName = %s")
    mycursor.execute(query, (username,))
    results = mycursor.fetchall()
    print(results)
    users_list = []
    for result in results:
        users_list.append(user(result[0], result[1]))
    if pw == result[1]:
        return (True, "Success", result[0], result[1])
    else:
        return (False, "Wrong password", 0, 0)

def get_classes(userid):
    connection = get_connection()
    mycursor = connection.cursor()
    query = ("SELECT courseId FROM s206001.attendscourse where userid = %s")
    mycursor.execute(query, (userid,))
    this_courseids = []
    for (course) in mycursor:
        this_courseids.append(course)
    query2 = ("SELECT * FROM s206001.classes where courseId = %s")
    class_list=[]
    for (courses) in this_courseids:
        mycursor.execute(query2, (courses[0],))
        for (classes) in mycursor:
            class_list.append(classes)
    mycursor.close()
    connection.close()
    return class_list

def get_classes_on_date(userid):
    connection = get_connection()
    mycursor = connection.cursor()
    class_list=[]
    query = ("SELECT courseID FROM s206001.attendscourse where userid = %s")
    mycursor.execute(query, (userid,))
    for (classes) in mycursor:
        class_list.append(classes)
    mycursor.close()
    connection.close()
    return class_list
