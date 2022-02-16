#import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import resultimport



#===================================


# Test with Raspi 3
sent_MBps_31 = resultimport.result31.sent_Mbps
received_Mbps_31 = resultimport.result31.received_Mbps

sent_MBps_32 = resultimport.result32.sent_Mbps
received_Mbps_32 = resultimport.result32.received_Mbps

sent_MBps_33 = resultimport.result33.sent_Mbps
received_Mbps_33 = resultimport.result33.received_Mbps

sent_MBps_34 = resultimport.result34.sent_Mbps
received_Mbps_34 = resultimport.result34.received_Mbps

sent_MBps_35 = resultimport.result35.sent_Mbps
received_Mbps_35 = resultimport.result35.received_Mbps

# Test with Raspi 4

sent_MBps_41 = resultimport.result41.sent_Mbps
received_Mbps_41 = resultimport.result41.received_Mbps

sent_MBps_42 = resultimport.result42.sent_Mbps
received_Mbps_42 = resultimport.result42.received_Mbps

sent_MBps_43 = resultimport.result43.sent_Mbps
received_Mbps_43 = resultimport.result43.received_Mbps

sent_MBps_44 = resultimport.result44.sent_Mbps
received_Mbps_44 = resultimport.result44.received_Mbps

sent_MBps_45 = resultimport.result45.sent_Mbps
received_Mbps_45 = resultimport.result45.received_Mbps





labels = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']
sent_MBps_3 = [sent_MBps_31, sent_MBps_32, sent_MBps_33, sent_MBps_34, sent_MBps_35]
sent_MBps_4 = [sent_MBps_41, sent_MBps_42, sent_MBps_43, sent_MBps_44, sent_MBps_45]

#men_means = [received_Mbps_31, received_Mbps_32, received_Mbps_33]
#women_means = [received_Mbps_41, received_Mbps_42, received_Mbps_43]

print("Mean 3: " + str(np.mean(sent_MBps_3)) + ' Mean 4: ' + str(np.mean(sent_MBps_4)))
print("Deviation 3: " + str(np.std(sent_MBps_3)) + ' Deviation 4: ' + str(np.std(sent_MBps_4)))

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sent_MBps_3, width, label='RP3B+ zu RP3B+', color='#72aa9d')
rects2 = ax.bar(x + width/2, sent_MBps_4, width, label='RP4B zu RP4B', color='#5176a5')
ax.axhline(y=np.mean(sent_MBps_3), color='#72aa9d', linestyle='--')
ax.axhline(y=np.mean(sent_MBps_4), color='#5176a5', linestyle='--')

# Set Y-Axis Limit to 620 --> Diagram boundary and labels touching
ax.set_ylim(0, 620)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Bandbreite (MBit/s)')
ax.set_title('Erreichte Bandbreite')
ax.set_xticks(x, labels)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()