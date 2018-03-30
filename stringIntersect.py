#Ray Tso
#3/30/18
#stringUnion.py

def stringIntersect(word1,word2):
    totalStr = ''
    totalStr += word1
        
    totalStr +=word2
    finalStr = ''
    for ch in totalStr:
        if ch in word1 and ch in word2:
            if not ch in finalStr:
                finalStr += ch
    return finalStr
    
print(stringIntersect('mississippi','pennsylvania'))
