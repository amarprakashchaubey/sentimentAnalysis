def computerate(stars):
    if(stars in range(0,3)):
        return "negative"
    elif(stars in range(4,6)):
        return "positive"
    else:
        return "neutral"