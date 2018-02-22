import os, sys
sys.path.append(os.getcwd())
from bow_new import bagOfWords
import pandas as pd
d = {}
d["stemming"] = True
d["with_html"] = False
d["split_type"] = "problem"
d["model_type"] = "NB"
x = bagOfWords(**d)
answer = x.predict()
for i,j in d.items():
	answer[i] = [j]*5
df = pd.DataFrame(answer)
df.to_csv("Result/BOW/bow6.csv", sep=",", index=False)
print (df)
