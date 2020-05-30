import pandas as pd

df = pd.read_csv("./text_emotion.csv")
df.drop(columns=['tweet_id', 'author'], inplace=True)
df.dropna(axis=1, inplace=True)
df = df[df.columns[::-1]]
df.to_csv(r'text.csv', index=False)
