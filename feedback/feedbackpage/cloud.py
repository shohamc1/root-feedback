import sqlite3, os
from sqlite3 import Error
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#f = open("data.txt", "w+")

def create_conn(dbfile):
    conn = None

    try:
        conn = sqlite3.connect(dbfile)
    except Error as e:
        print (e)

    return conn

def printall(conn):
    strng = ''
    cur = conn.cursor()
    cur.execute("SELECT feedback FROM feedbackpage_fbcontent")
    rows = cur.fetchall()

    for row in rows:
        strng = strng + ''.join(row) + ' '

    return strng

def main():
    conn = create_conn('db.sqlite3')
    #printall(conn)
    #f.close()


    #file_content = open("data.txt").read()
    file_content = printall(conn)



    wordcloud = WordCloud(stopwords=STOPWORDS, background_color = 'white', width=1200, height=1000).generate(file_content)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig (os.getcwd() + '/static/images/cloud.png')