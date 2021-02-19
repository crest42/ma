from plot_cryptosystems import plot_cryptosystems_single_dim
from cryptosystems import SIGN_DF
import matplotlib

df = SIGN_DF
#df = df.drop(['NTS-13-80'], level=2)
df = df[df['Level'] == 3]
df= df.reset_index(drop=True)
df = df.sort_values(['ratio'])


import seaborn as sns
import matplotlib.pyplot as plt
colors = sns.color_palette("Paired")
#g.set_xticklabels(g.get_xticklabels(), rotation=54)

g=sns.barplot(data=df, x='Cipher', y='ratio')
for item in g.get_xticklabels():
    item.set_rotation(45)
g.set_yscale("log")
#plt.show()
#plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_bar_ratio_comp_sign.pdf')
