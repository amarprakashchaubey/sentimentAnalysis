def replaceoldwords(short_word):
    f=open("newagewords.csv","r")
    newagelist=f.readlines()
    f.close()
    replace=short_word

    for line in newagelist:
        templist=line.split(",")
        print ("check",short_word,"with",templist[1].lower())
        if(short_word.lower()==templist[1].lower()):
            print ("replaced",short_word)
            replace=templist[2]
        else:
            pass
    return replace