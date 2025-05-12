import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'precincts-with-results.csv'

df = pd.read_csv(file_path)

vote_column = 'votes_total'  #'votes_dem'or'votes_rep'

votes = df[vote_column]
votes = votes[votes > 0]

leading_digits = votes.astype(str).str[0].astype(int)

actual_counts = leading_digits.value_counts().sort_index()
actual_distribution = actual_counts / actual_counts.sum()

benford_distribution = [np.log10(1 + 1/d) for d in range(1, 10)]

plt.figure(figsize=(10, 6))
plt.bar(range(1, 10), actual_distribution, alpha=0.7, label='distribution')
plt.plot(range(1, 10), benford_distribution, 'r--', label='benford's law', linewidth=2)
plt.xlabel('first digit')
plt.ylabel('ratio')
plt.title(f'{vote_column} analysis ')
plt.xticks(range(1, 10))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
