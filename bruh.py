import pandas as pd

df = pd.read_json("nonclickbait_with_transcripts.json", lines=True)
print(df.head())
