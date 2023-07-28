import sqlite3,  hashlib


conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Foydalanuvchilar jadvalini yaratish
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                userID INTEGER PRIMARY KEY,
                first_name TEXT ,
                last_name TEXT ,
                birth_day data,
                phone TEXT ,
                username TEXT UNIQUE,
                password TEXT,
                is_admin BOOLEAN)'''
            )

# Kurslar jadvalini yaratish
cur.execute('''CREATE TABLE IF NOT EXISTS courses (
                courseID INTEGER PRIMARY KEY,
                name TEXT,
                number_of_students INTEGER,
                is_active BOOLEAN)'''
            )


# Kurs qo'shish
def add_course(name, number_of_students):
    cur.execute("INSERT INTO courses (name, number_of_students, is_active) VALUES (?, ?, ?)",
                (name, number_of_students, True))
    conn.commit()
    print("Kurs qo'shildi.")


# Kurslarga o'quvchi yozish
def add_student_to_course(student_id, course_id):
    cur.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
                (student_id, course_id))
    cur.execute("UPDATE courses SET number_of_students = number_of_students + 1 WHERE courseID = ?",
                (course_id,))
    conn.commit()
    print("O'quvchi kursga yozildi.")


# Aktiv kurslarni ko'rish
def view_active_courses():
    cur.execute("SELECT * FROM courses WHERE is_active = 1")
    courses = cur.fetchall()
    print("Aktiv kurslar:")
    for course in courses:
        print(f"{course[0]}. {course[1]}")


# O'quchilar ro'yhatini ko'rish
def view_students():
    cur.execute("SELECT * FROM users WHERE is_admin = 0")
    students = cur.fetchall()
    print("O'quvchilar ro'yhati:")
    for student in students:
        print(f"{student[0]}. {student[1]} {student[2]}")


# Kurslarni ozgartirish
def change_course_status(course_id, is_active):
    cur.execute("UPDATE courses SET is_active = ? WHERE courseID = ?",
                (is_active, course_id))
    conn.commit()
    print("Kurs holati o'zgartirildi.")

def register_user():
    cur = conn.cursor()
    firs_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    brith_day = input("Enter birthday (yyyy-mm-dd): ")
    phone = input("Enter phone: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    is_admin = ("Enter is admin (boolean)")
    cur.execute("insert into users (firs_name, last_name, brith_day, phone, username, password, is_admin) values (?, ?, ?, ?, ?, ?, ?)", (firs_name, last_name, brith_day, phone, username, password, is_admin))
    conn.commit()
    conn.close()

def close_database():
    conn.close()

def con():
    return sqlite3.connect("databse.db")


def register_usere():
    conn = con()
    cur = conn.cursor()
    firs_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    brith_day = input("Enter birthday (yyyy-mm-dd): ")
    phone = input("Enter phone: ")
    username = input("Enter username: ")
    password = passwordtest()
    is_admin = ("Enter is admin (boolean)")
    cur.execute("insert into user (firs_name, last_name, brith_day, phone, username, password, is_admin) values (?, ?, ?, ?, ?, ?, ?)", (firs_name, last_name, brith_day, phone, username, password, is_admin))
    conn.commit()
    conn.close()
def hashlib_passiword(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode("utf-8"))
    return sha256.hexdigest()
def passwordtest():
    password = input("Enter password: ")
    password1 = input("Reenter password: ")
    if password  == password1:
        return hashlib_passiword(password)
    else:
        print("parollar mos emas ")
        return passwordtest()
def regester_course():
    conn = con()
    cur = conn.cursor()
    name = input("Enter cours name: ")
    number_of_students = input("Enter : number_of_students ")
    is_active = ("Enter is course (boolean)")
    cur.execute("insert into courses (name, number_of_students, is_active) values (?, ?, ?)", (name, number_of_students, is_active))
    conn.commit()
    conn.close()
def ControlPanel():
    print("Select an input block:")
    print(" 1 = register the user")
    print(" 3 = register the course")
    print(" 4 = kursga yozilish uquvchilar uchun ")
    print(" 5 = kurs qushish Adminlar uchun ")
    print(" 7 = Aktiv kurslar royhatini korish uquvchilar uchun ")
    print(" 8 = Aktiv kurslarga yozilish; ")
    print(" 9 = Ozi yozilgan kurslar royhatini korish uquvchilar uchun ")
    selectinputblock = input( "please select ")
    if int(selectinputblock)==1:
        register_usere()
    elif int(selectinputblock) == 2:
         regester_course()
    elif int(selectinputblock) == 3:
        pass
    elif int(selectinputblock) == 4:
        pass
    elif int(selectinputblock) == 5:
        pass
    elif int(selectinputblock) == 6:
        pass
    elif int(selectinputblock) == 7:
        pass
    elif int(selectinputblock) == 8:
        pass
    elif int(selectinputblock) == 9:
        pass

ControlPanel()

