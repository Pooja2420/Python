# import PyPDF2
# import textract
# #import re
# #import string
# import pandas as pd
#import matplotlib.pyplot as plt
from translate import Translator
#%matplotlib inline
# pip install pandas 
import pandas as pd

# Read the csv file
data = pd.read_csv('English.csv')

# Print it out if you want
print(data)
translator= Translator(to_lang="spanish")
translation = translator.translate("Good Morning!")
print (translation)