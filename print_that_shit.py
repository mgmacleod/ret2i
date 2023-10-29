import pandas as pd

# Load the csv file
df = pd.read_csv("log_wavy.csv")

# Print the 'prompt' and 'filename' columns
for index, row in df.iterrows():
    print(f"Prompt: {row['prompt']}, Filename: {row['filename']}")
