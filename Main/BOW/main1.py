import os, sys
sys.path.append(os.getcwd())
from bow_new import bagOfWords
import pandas as pd
d = {}
d["stemming"] = False
d["with_html"] = True
d["split_type"] = "problem"
d["model_type"] = "NN"
x = bagOfWords(**d)
answer = x.predict()
for i,j in d.items():
	answer[i] = [j]
print (answer)
# df = pd.DataFrame(answer)
# df.to_csv("Result/BOW/hellbow1.csv", sep=",", index=False)
# print (df)
