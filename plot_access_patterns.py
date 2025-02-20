import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read data from CSV file
df = pd.read_csv('./access_patterns/500M/L2_miss/rnd.out')

# Plotting
plt.figure(figsize=(15, 10))

# Create scatter plot
for eip in df['eip'].unique():
    subset = df[df['eip'] == eip]
    
    if subset.size > 10000:
        print(eip , subset.size, subset['vpn'].min(), subset['vpn'].max())

        for event in df['e'].unique():
            event_subset = subset[subset['e'] == event]

            plt.scatter(event_subset['ts'], event_subset['vpn'], label=f'Event {event}', alpha=0.7)
            plt.plot(event_subset['ts'], event_subset['vpn'], alpha=0.7)


        # plt.scatter(subset['ts'], subset['vpn'], label=f'eip {eip}', alpha=0.7)
        # plt.plot(subset['ts'], subset['vpn'], label=f'eip {eip}', alpha=0.7)

        # Adding labels and title
        plt.xlabel('Clock Cycle')
        plt.ylabel('vpn')
        plt.title(f'VPNs Accessed by eip {eip}')
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

