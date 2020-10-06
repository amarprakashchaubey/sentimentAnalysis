from StopWordProcess import removeStopWords2
from properties import properties
def getcategory(review):
    p=0
    n=0
    total=0
    listofwords=review.split(" ")
    total=len(listofwords)
    updated_list=removeStopWords2(listofwords)
    p=positivedataprocess2(updated_list)
    n=negativedataprocess2(updated_list)
    properties.pcount=p
    properties.ncount=n
    perp=(p*100)/total
    pern=(n*100)/total
    status =""
    if(perp>pern):
        status ="positive"
    elif(pern>perp):
        status ="negative"
    else:
        status ="neutral"
    return updated_list, status

def positivedataprocess2(listofwords):
    f = open("positivedataset.csv", "r")
    records = f.readlines()
    f.close()
    n=0
    for rows in records:
        templist = rows.split(",")
        pword = templist[1].replace("\n", "")
        if (pword in listofwords):
            n = n + 1
    return n

def negativedataprocess2(listofwords):
    f = open("negativedataset.csv", "r")
    records = f.readlines()
    f.close()
    n=0
    for rows in records:
        templist = rows.split(",")
        pword = templist[1].replace("\n", "")
        if (pword.lower() in listofwords):
            n = n + 1
    return n


'''
def positivedataprocess(listofwords):
    p = 0
    import pymysql
    con = pymysql.connect(host="localhost", user="root", passwd="root", db="preview")
    mycursor = con.cursor()
    for word in listofwords:
        query = "select * from positivedataset where positive='"+word+"'"
        mycursor.execute(query)
        records = mycursor.fetchall()
        if(len(records)>0):
            p=p+1
    return p

def negativedataprocess(listofwords):
    n = 0
    import pymysql
    con = pymysql.connect(host="localhost", user="root", passwd="root", db="preview")
    mycursor = con.cursor()
    for word in listofwords:
        query = "select * from negativedataset where negative='"+word+"'"
        mycursor.execute(query)
        records = mycursor.fetchall()
        if(len(records)>0):
            n=n+1
    return n
'''