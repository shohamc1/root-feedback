import sqlite3, csv

con = sqlite3.connect('C:\\Users\\Shoham\\Desktop\\root-feedback\\feedback\\db.sqlite3')
cur = con.cursor()

data = cur.execute("SELECT * FROM feedbackpage_fbcontent")
#data = cur.execute("SELECT * FROM \'sqlite_master\'")

#cur.execute('.header on')
#cur.execute('.mode csv')    
#cur.execute('.once feedback.csv')
#cur.execute('SELECT * FROM feedbackpage_fbcontent;')

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'fb'])
    writer.writerows(data)