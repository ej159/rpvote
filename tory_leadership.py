# This is a quick and dirty attempt to generate a global ranking of Conservative leadship candidates from pairwise comparisons from the poll data here: https://docs.cdn.yougov.com/6shnrhfen6/ConservativePartyMembers_LeadershipContenders_220713_w.pdf

import pandas as pd
import string
import numpy as np
non_numeric_chars = ''.join(set(string.printable) - set(string.digits))
translation_map = {ord(c):'' for c in non_numeric_chars}


df = pd.read_csv("table-8.csv")
df = df.query("Datesconducted == '12–13 Jul 2022'")
candidates = df.columns[4:]
number_of_voters = int(df['Samplesize'][0].translate(translation_map))
df = df[candidates]
df = df.replace(["–"],int(0))
df.replace(r'[a-zA-Z%]', '', regex=True, inplace=True)
df = df.apply(pd.to_numeric, errors = 'coerce')
df = df.multiply(number_of_voters/100).round(0).astype(int)
print(df)

