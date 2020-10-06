from properties import properties
from NewAgeWords import replaceoldwords
from ReviewDetect import getcategory
from star_rating import computerate
comment = input("Enter the comment:")
stars = input("Enter the star rating:")
spolarity =computerate(stars)
s2=" but "
s3=" not "
if(s2 in comment):
    i=comment.index(s2)
    print i
    comment= comment[comment.index(s2) + len(s2):]
print ("org",comment)
if(s3 in comment):
    properties.flag1=True
templist=comment.split(" ")
comment=""
for word in templist:
    comment=comment+replaceoldwords(word)+" "
comment=comment.strip()
print("processed",comment)
updated_words,polarity=getcategory(comment)

if(properties.flag1):
    if(polarity=="negative"):
        polarity="positive"
    elif(polarity=="positive"):
        polarity="negative"

print (updated_words,"Review:->", polarity,"Stars->",spolarity)




'''
f=open("newagewords.csv","r")
str1=f.read()
str1=str1.lower()
f.close()
str1=str1.replace('"','')
templist=str1.split("\n")
print (len(templist))
data=""

for line in templist:
    print line
    if(line.endswith(",")):
        line=line[:len(line)-1]
    data=data+line+"\n"
print data
f=open("newagewords.csv","w")
f.write(data)
f.close()
'''