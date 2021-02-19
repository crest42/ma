#!/usr/bin/python
from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import KEM_KEX_DF

df = KEM_KEX_DF[KEM_KEX_DF['IND'] == 'CCA']

df = df[df['Round'] == 3]

plt = plot_cryptosystems_seaborn(df, 'sum-50th', 'Public Key Size',
                                 type='Isogeny',
                                 hue_col="Cipher",
                                 style_col='Cipher',
                                 xlabel=r'Key Exchange Runtime in CPU Cycles',
                                 ylabel='Public Key Bytes',
                                 title='Isogeny-Based Key Exchanges', s=50)

plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_isogeny_based_latency_pubkeysize.pdf')
#plt.show()
