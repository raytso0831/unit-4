#Ray Tso
#3/28/18
#stringUnion.py

def stringUnion(word1,word2):
    totalStr = ''
    totalStr += word1
        
    totalStr +=word2
    finalStr = ''
    for ch in totalStr:
        if ch in word1:
            if not ch in finalStr:
                finalStr += ch
        if ch in word2:
            if not ch in finalStr:
                finalStr+= ch
    return finalStr
    
print(stringUnion('mississippi','pennsylvania'))
        
   
    
