import pandas as pd

df = pd.read_excel(#insertpath, usecols="I,J,K,L")

df = df[df['Propert Description'].str.contains('DWL')]

#df["Street Address"] = df["Road #"] + " " + df["Road Name"] + "Charlotte, VT 05445"
df["Road #"] = df["Road #"].astype(str)

df["Street Address"] = df[["Road #","Road Name"]].agg(" ".join, axis=1)

df["Street Address"] = df["Street Address"] + ", Charlotte VT, 05445"

df = df.drop("Road #", axis=1)
df = df.drop("Road Name", axis=1)
df = df.drop("Tax Map Reference", axis=1)
df = df.drop("Propert Description", axis=1)

filepath= #insertpath
df.to_csv(filepath, index=False)

a = df.head()
print (a)
