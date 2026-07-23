import pandas as pd
df=pd.read_csv('music_streaming_habits_2026.csv')
print("original data:")
print(df)
df=df.drop_duplicates()
df=df.dropna()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()
    df.columns=df.columns.str.lower()
    df.to_csv('cleaned_music_streaming_habits_2026.csv', index=False)
    print("cleaned data:")
print(df)