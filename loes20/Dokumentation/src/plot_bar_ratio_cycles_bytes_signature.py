from plot_cryptosystems import plot_cryptosystems_single_dim, sns
from cryptosystems import SIGN_DF, max_abs_scaler, np
import matplotlib
df = SIGN_DF
p = sns.color_palette("Paired")
sns.set(context='paper', palette=sns.color_palette("Paired"))
sns.set_style(sns.axes_style("ticks"),
              {'axes.grid': True})

df = df[df['Level'] == 3]
df['test'] = np.where(df['ratio_data_to_cycles']<1, -1, df['ratio_data_to_cycles']**2)/df['ratio_data_to_cycles']
df= df.reset_index(drop=True)
#df = df.sort_values(['Algorithm','Total Cost'])

import matplotlib.pyplot as plt

g=sns.barplot(data=df, x='Cipher', y='test',color=p[0])
for item in g.get_xticklabels():
    item.set_rotation(90)
#g.set_yscale("log")
g.set(xlabel='', ylabel='Bytes/Cycles')
#plt.show()
#plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_bar_ratio_comp_sign.pdf')
