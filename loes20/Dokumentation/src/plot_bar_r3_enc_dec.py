from plot_cryptosystems import plot_cryptosystems_single_dim
from cryptosystems import KEM_KEX_DF
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
df = KEM_KEX_DF[KEM_KEX_DF['IND'] == 'CCA']
df = KEM_KEX_DF[KEM_KEX_DF['Round'].isin([-1,3])]
#df = df.drop(['NTS-13-80'], level=2)
df = df[df['Level'] == 3]
df= df.reset_index(drop=True)
df = df.sort_values(['Algorithm','kexrt-50th'])

ghz = float(10**9)

df['kexrt-50th'] = df['kexrt-50th']/ghz
df['dec-50th'] = df['dec-50th']/ghz
df['enc-50th'] = df['enc-50th']/ghz

colors = sns.color_palette("Paired")

g = sns.FacetGrid(data=df, col="Type", sharex=False, sharey=False)

ax = g.map(sns.barplot, 'Cipher', "kexrt-50th",  edgecolor = 'none', color=colors[0])
ax = g.map(sns.barplot, 'Cipher', "enc-50th", edgecolor = 'none', color=colors[1])

[plt.setp(ax.get_xticklabels(), rotation=90) for ax in g.axes.flat]

mv = None
for f in g.axes.flat:
    f.set(xlabel='', ylabel='')
    if f.get_title() == 'Type = Isogeny':
        mv = f
    f.set(xlabel='', ylabel='')
g.axes.flat[0].set(ylabel='Cycles')

for p in mv.patches:
    centre = p.get_x()+p.get_width()/2.
    p.set_x(centre-0.05/2.)
    p.set_width(0.05)

legend_labels  = ['Decryption Time', 'Encryption Time']


legend_patches = [matplotlib.patches.Patch(color=C, label=L) for
                  C, L in zip([item.get_facecolor() for item in mv.patches],
                              legend_labels)]

# Plot the legend
plt.legend(handles=legend_patches)
plt.gcf().set_figheight(7)
plt.gcf().set_figwidth(13)
#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_bar_r3_enc_dec.pdf')
