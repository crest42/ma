from plot_cryptosystems import plot_cryptosystems_single_dim, palette
from cryptosystems import SIGN_DF
import matplotlib
import pandas as pd
df = SIGN_DF
#df = df.drop(['NTS-13-80'], level=2)
df = df[df['Level'] == 3]
df = df[df['Round'].isin([-1,3])]
df = pd.concat([df, SIGN_DF[SIGN_DF['Cipher'].isin(['falcon1024dyn','falcon1024tree'])]])

df= df.reset_index(drop=True)
df = df.sort_values(['Type','Data Size'])

#df['enc-25th'] = df['enc-25th']//1000
#df['enc-75th'] = df['enc-75th']//1000
#yerr=[df['enc-50th']-df['enc-25th'],df['enc-75th']-df['enc-50th']]

import seaborn as sns
import matplotlib.pyplot as plt
colors = sns.color_palette("Paired")
#g.set_xticklabels(g.get_xticklabels(), rotation=54)
sns.set(font_scale=1.4, context='paper', palette=palette)
sns.set_style(sns.axes_style("ticks"),
              {'axes.grid': True})
g = sns.FacetGrid(data=df, col="Type", sharex=False, sharey=False)

ax = g.map(sns.barplot, 'Cipher', "Data Size",  edgecolor = 'none', color=colors[0])
ax = g.map(sns.barplot, 'Cipher', "sign23B", edgecolor = 'none', color=colors[1])
[plt.setp(ax.get_xticklabels(), rotation=90) for ax in g.axes.flat]
fig =  g.axes.flat[2]
mv = None
for f in g.axes.flat:
    if f.get_title() == 'Type = ZK-Proof':
        mv = f
    f.set(xlabel='', ylabel='',title=f.get_title()[6:])



g.axes.flat[0].set(ylabel='Bytes')

for p in mv.patches:
    centre = p.get_x()+p.get_width()/2.
    p.set_x(centre-0.2/2.)
    p.set_width(0.2)

legend_labels  = ['PK Size', 'Signature Size']
legend_patches = [matplotlib.patches.Patch(color=C, label=L) for
                  C, L in zip([item.get_facecolor() for item in mv.patches],
                              legend_labels)]

# Plot the legend
plt.legend(handles=legend_patches,loc='lower left')
plt.gcf().set_figheight(7)
plt.gcf().set_figwidth(13)
#plt.show()
plt.tight_layout()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_bar_traffic_signatures.pdf')
