import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

X_TITLE = 'Workload'
Y_TITLE = 'STLB Miss Penalty (Cycles)'
Y_MIN = 0
Y_MAX = 200
FILE_NAME = 'stlb_mp'
Y_TICKS = 20


# Read the CSV data into a DataFrame
df = pd.read_csv('csvs/' + FILE_NAME + '.csv')

# Set the workload column as the index
df.set_index('workload', inplace=True)

# Generate a range of monochrome colors
colors = [str(0.75/(len(df.columns)) * i) for i in range(1, len(df.columns) + 1)]

# Determine the number of columns to set figure width accordingly
fig_width = max(10, 3.5 * len(df.columns))

# Create a figure and axes
fig, ax = plt.figure(figsize=(fig_width, 4)), plt.gca()

# Plot each column as a separate bar group
bar_width = 0.6 / len(df.columns)  # Adjust bar width for spacing
x = np.arange(len(df.index))  # X locations for the groups

for i, col in enumerate(df.columns):
    ax.bar(x + i * bar_width, df[col], width=bar_width, color=colors[i], label=col)

# Set the labels and ticks
ax.set_xlabel(X_TITLE, fontsize=18, fontweight='bold')
ax.set_ylabel(Y_TITLE, fontsize=18, fontweight='bold')
ax.set_xticks(x + bar_width * (len(df.columns) - 1) / 2)
ax.set_xticklabels(df.index, fontsize=14, rotation=45)
ax.set_yticks(np.arange(Y_MIN, Y_MAX + 0.05, Y_TICKS))
ax.set_ylim(Y_MIN, Y_MAX)
ax.tick_params(axis='y', labelsize=14)

# Position the legend at the top inside the chart area without overlapping
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=len(df.columns), fontsize=14)

# Add gridlines
ax.grid(axis='y')

# Save the plot with minimal white space
plt.savefig('figs/' + FILE_NAME + '.png', dpi=300, bbox_inches='tight', pad_inches=0.2)

# Show the plot
# plt.show()
