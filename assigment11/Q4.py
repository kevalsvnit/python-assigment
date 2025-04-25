import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'John': [True, False, False, True, False, True, False, False, True, False],
    'Judy': [True, True, False, False, False, True, True, False, True, False]
})

# Both John and Judy are at the party
df['party'] = df['John'] & df['Judy']

# Initialize a list to store days until next party
days_till_party = [None] * len(df)

# Find indices where a party happens
party_indices = df.index[df['party']].tolist()

# If no party at all
if not party_indices:
    df['days_till_party'] = np.nan
else:
    next_party_idx = None
    for i in reversed(range(len(df))):
        if i in party_indices:
            days_till_party[i] = 0
            next_party_idx = i
        else:
            days_till_party[i] = next_party_idx - i if next_party_idx is not None else np.nan

    # Add the result to the DataFrame
    df['days_till_party'] = days_till_party

# Drop the helper column
df.drop(columns='party', inplace=True)

# Print the final DataFrame
print(df)
