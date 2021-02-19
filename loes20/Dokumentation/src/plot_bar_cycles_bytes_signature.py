from plot_cryptosystems import plot_cryptosystems_single_dim, sns
from cryptosystems import SIGN_DF, max_abs_scaler, np
import matplotlib
df = SIGN_DF
p = sns.color_palette("Paired")
sns.set(context='paper', palette=sns.color_palette("Paired"))
sns.set_style(sns.axes_style("ticks"),
              {'axes.grid': True})

#df = df[df['Level'] == 3]
df = df[df['Round'].isin([3,-1])]
df= df.reset_index(drop=True)
df['test'] = df['Total Cost'] + df['Data Size']
df = df.sort_values(['test'])

import matplotlib.pyplot as plt
df1 = df[['Cipher', 'Total Cost', 'Data Size','Algorithm']]
df1= df1.rename(columns={"Total Cost": "CPU Cycles", "Data Size": "Bytes"})

#tidy = df1.melt(id_vars='Cipher').rename(columns=str.title)
#g=sns.barplot(data=tidy, x='Cipher', y='Value', hue='Variable')
#for item in g.get_xticklabels():
#    item.set_rotation(90)


g=sns.scatterplot(data=df1, x='CPU Cycles', y='Bytes', hue='Algorithm')
g.set_yscale("log")
g.set_xscale("log")
#g.set(xlabel='', ylabel='Min-Max Scaled Costs')
#plt.gcf().set_figheight(11)
#plt.gcf().set_figwidth(13)
#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_bar_cycles_bytes_signature.pdf')
