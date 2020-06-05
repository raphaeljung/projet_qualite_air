import pandas as pd


# import du dataset
URL = "https://trouver.datasud.fr/dataset/8bfa93b0-ac2f-4148-b550-0ec5c917bb28/resource/52a8f5dd-758d-4e54-a837-8fc7ad57d378/download/eco2mix-regional-tr.csv"

df = pd.read_csv(URL, sep = ';')

# nettoyage rapide
df = df.replace("-", 0)
df.fillna(0)