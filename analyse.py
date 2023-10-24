import pandas as pd

dataset = pd.read_csv("spotify_wrapped.csv")
#print(dataset)

stg_dataset = dataset["artist"].value_counts()

top_5_artists = stg_dataset.head(5)


result_df = top_5_artists.reset_index()
result_df.columns = ["Artist", "Count"]

print(result_df)