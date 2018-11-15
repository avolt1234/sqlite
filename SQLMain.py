import sqlite3
import os
import image
import base64

def main():

    #Connect to the DB, if it doesnt exist then it creates it
    conn = sqlite3.connect('database.db')

    conn.execute(''' CREATE TABLE IMAGES
                (ID STRING PRIMARY KEY         NOT NULL,
                IMAGE       BLOB            NOT NULL
                );''')

    print 'Opened Database Successfully'
    return


def insertImage(filePath):
    conn = sqlite3.connect('database.db')

    fileName = os.path.basename(filePath)

    with open(filePath, 'rb') as input_file:
        ablob = base64.b64encode(input_file.read())

    conn.execute('INSERT INTO IMAGES (ID, IMAGE) values (?,?)',
                 (fileName, sqlite3.Binary(ablob)))
    conn.commit()


def extract_picture(pictureID):
    conn = sqlite3.connect('database.db')
    sql = "SELECT ID, IMAGE FROM IMAGES WHERE id = :id"
    param = {'id': pictureID}
    fileName, blob = conn.execute(sql, param).fetchone()

    blob = base64.b64decode(blob)

    fh = open(r'C:\Users\Alex PC\Desktop\Images\test.jpeg', 'wb')
    fh.write(blob)
    fh.close()

    print blob


if __name__ == '__main__':
    value = raw_input('Enter 1 to initialize db, enter 2 to add image, enter 3 to get image: ')
    if value == '1':
        main()
    elif value == '2':
        file = raw_input('Enter the fileName: ')
        insertImage(file)
    else:
        file = raw_input('Enter Image Name: ')
        extract_picture(file)