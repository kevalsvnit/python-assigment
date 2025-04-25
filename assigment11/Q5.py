import pandas as pd
import numpy as np
from itertools import product

# Define the data
data = {
    'artist': ['Adele', 'Adele', 'Drake', 'Adele', 'Drake', 'Taylor Swift'],
    'venue': ['MSG', 'MSG', 'MSG', 'Barclays', 'MSG', 'MSG'],
    'date': pd.to_datetime([
        '2023-01-15', '2023-01-20', '2023-01-15',
        '2023-02-01', '2023-02-20', '2023-01-25'
    ])
}

# Create DataFrame
concerts_df = pd.DataFrame(data)

# Extract year-month as period
concerts_df['year_month'] = concerts_df['date'].dt.to_period('M')

# Get all unique artists and venues
artists = pd.Series(concerts_df['artist'].unique(), name="artist")
venues = pd.Series(concerts_df['venue'].unique(), name="venue")

# Create all possible (artist, venue) pairs using cartesian product
artist_venue_pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])

# Group by year_month, artist, venue and count concerts
grouped = concerts_df.groupby(['year_month', 'artist', 'venue']).size()

# Convert to wide table
wide_table = grouped.unstack(['artist', 'venue'])

# Ensure all artist-venue pairs are present as columns, fill missing with 0
wide_table = wide_table.reindex(columns=artist_venue_pairs, fill_value=0)

# Reset index to make year_month a column
wide_table = wide_table.reset_index()

# Display the final table
print(wide_table)
