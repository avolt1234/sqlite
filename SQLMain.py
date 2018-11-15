import sqlite3
import os
import image
import base64
import matplotlib.pyplot as plt

def main():

    #Connect to the DB, if it doesnt exist then it creates it
    conn = sqlite3.connect('database.db')

    conn.execute(''' CREATE TABLE IMAGES
                (ID STRING PRIMARY KEY         NOT NULL,
                IMAGE       BLOB            NOT NULL
                );''')

    print('Opened Database Successfully')
    filePath = r'C:\Users\Alex PC\Desktop\Images\salmon.jpeg'
    insertImage(filePath, conn)

    extract_picture(conn, 'salmon.jpeg')

    return

def insertImage(filePath):
    conn = sqlite3.connect('database.db')

    fileName = os.path.basename(filePath)

    with open(filePath, 'rb') as input_file:
        ablob = input_file.read()

    conn.execute('INSERT INTO IMAGES (ID, IMAGE) values (?,?)',
                 (fileName, sqlite3.Binary(ablob)))
    conn.commit()

def extract_picture(pictureID):
    conn = sqlite3.connect('database.db')
    sql = "SELECT ID, IMAGE FROM IMAGES WHERE id = :id"
    param = {'id': pictureID}
    fileName, blob = conn.execute(sql, param).fetchone()

    print(blob)
    return blob


if __name__ == '__main__':
    value = input('Enter 1 to initialize db, enter 2 to add image, enter 3 to get image: ')
    if value == '1':
        main()
    elif value == '2':
        file = input('Enter the fileName: ')
        insertImage(file)
    else:
        file = input('Enter Image Name: ')
        extract_picture(file)