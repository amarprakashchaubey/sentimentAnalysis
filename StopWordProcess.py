def removeStopWords(listofwords):
    import pymysql
    con = pymysql.connect(host="localhost", user="root", passwd="root", db="preview")
    mycursor = con.cursor()
    query = "select words from stopwords"
    mycursor.execute(query)
    records = mycursor.fetchall()
    for rows in records:
        if(rows[0] in listofwords):
            listofwords.remove(rows[0])
    return listofwords

def removeStopWords2(listofwords):
    f = open("stopwords.csv", "r")
    records = f.readlines()
    f.close()
    for rows in records:
        templist=rows.split(",")
        stopword=templist[1].replace("\n","")
        if(stopword in listofwords):
            listofwords.remove(stopword)
    return listofwords