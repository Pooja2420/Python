from textblob import TextBlob
 
a = "cmputr,dres,shin,comad,rigt,sni"           # incorrect spelling
print("original text: "+str(a))
 
b = TextBlob(a)
 
# prints the corrected spelling
print("corrected text: "+str(b.correct()))