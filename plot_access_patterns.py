import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read data from CSV file
df = pd.read_csv('./access_patterns/10M/L2_miss/victima_ptw_2MBL2_rnd.out')

df['SN'] = range(1, len(df) + 1)

# Plotting
plt.figure(figsize=(15, 10))

# Create scatter plot
for eip in df['EIP'].unique():
    subset = df[df['EIP'] == eip]
    
    if subset.size > 100:
        print(eip , subset.size, subset['VPN'].min(), subset['VPN'].max())


        for event in df['E'].unique():
            event_subset = subset[subset['E'] == event]

            plt.scatter(event_subset['SN'], event_subset['VPN'], label=f'Event {event}', alpha=0.7)
            plt.plot(event_subset['SN'], event_subset['VPN'], alpha=0.7)


        # plt.scatter(subset['SN'], subset['VPN'], label=f'EIP {eip}', alpha=0.7)
        # plt.plot(subset['SN'], subset['VPN'], label=f'EIP {eip}', alpha=0.7)

        # Adding labels and title
        plt.xlabel('Serial Number')
        plt.ylabel('VPN')
        plt.title(f'VPNs Accessed by EIP {eip}')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        # Adjust layout
        plt.tight_layout()

        # Show plot
        plt.show()









# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# # Read data from CSV file
# df = pd.read_csv('./access_patterns/10M/L2_miss/victima_ptw_2MBL2_bc.out')

# df['SN'] = range(1, len(df) + 1)

# # Plotting
# plt.figure(figsize=(15, 10))

# # Create scatter plot
# for eip in df['EIP'].unique():
#     subset = df[df['EIP'] == eip]
    
#     if subset.size > 100:
#         print(eip , subset.size, subset['VPN'].min(), subset['VPN'].max())
#         plt.scatter(subset['SN'], subset['VPN'], label=f'EIP {eip}', alpha=0.7)
#         plt.plot(subset['SN'], subset['VPN'], alpha=0.7)


# # Adding labels and title
# plt.xlabel('Serial Number')
# plt.ylabel('VPN')
# plt.title(f'VPNs Accessed by EIPs')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# # Adjust layout
# plt.tight_layout()

# # Show plot
# plt.show()

