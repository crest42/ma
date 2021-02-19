from plot_cryptosystems import plot_cryptosystems_single_dim, palette
from cryptosystems import KEM_KEX_DF
import matplotlib
df = KEM_KEX_DF[KEM_KEX_DF['IND'] == 'CCA']
df = df[df['Level'] == 3]
df = df[df['Round'].isin([3,-1])]
df.loc[('Isogeny', 'SIKE', 'SIKEp610', 'CCA'),'gen-50th'] = 0
df.loc[('Classical', 'ECDH', 'curve25519', 'CCA'),'gen-50th'] = 0
df.loc[('Classical', 'ECDH', 'nistp256', 'CCA'),'gen-50th'] = 0
df.loc[('Classical', 'DH', 'dh2048', 'CCA'),'gen-50th'] = 0
df['sum-50th'] = df['gen-50th']+df['kexrt-50th']

df= df.reset_index(drop=True)
df = df.sort_values(['sum-50th'])


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set(context='paper', palette=sns.color_palette("Paired"))
sns.set_style(sns.axes_style("ticks"),
              {'axes.grid': True})

df['sum'] = df['gen-50th']+df['enc-50th']+df['dec-50th']
df['Hue'] = 'PQ'
df.loc[df[df['Cipher'].isin(['dh2048','rsa2048','nistp256','curve25519'])].index, 'Hue'] = 'Classical'
df.loc[df[df['Cipher'].isin(['SIKEp610'])].index,'Hue'] = 'Isogeny-Based'
ax = sns.barplot(data=df,y='Cipher',x='sum',hue='Hue', palette=palette, dodge=False)
plt.tight_layout()
ax.set_xscale('log')
ax.set_xlabel('CPU Cycles')
#plt.gcf().set_figheight(7)
#plt.gcf().set_figwidth(13)
#p1 = plt.bar(cryptosystems, y, width)
#plt.xticks(rotation=45)
#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_bar_ephemeral.pdf')
