import pandas as pd
from textblob import TextBlob
df = pd.read_csv (r'C:\Users\Kwiksales\Desktop\English.csv')
print (df)
# files upload via google colab.
from google.colab import files 
uploaded = files.upload()
print("original text: "+str(uploaded))
b = TextBlob(uploaded)
# prints the corrected spelling
print("corrected text: "+str(b.correct()))