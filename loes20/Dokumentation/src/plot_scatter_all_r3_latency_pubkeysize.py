from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import KEM_KEX_DF

df = KEM_KEX_DF[KEM_KEX_DF['IND'] == 'CCA']
df = KEM_KEX_DF[KEM_KEX_DF['Round'] == 3]

plt = plot_cryptosystems_seaborn(df, 'sum-50th', 'Public Key Size',
                                 hue_col="Algorithm",
                                 style_col='Type',
                                 xlabel='Runtime CPU Cycles',
                                 ylabel='Public Key Bytes',
                                 xscale='log', yscale='log',
                                 title='')


plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_all_r3_latency_pubkeysize.pdf')
#plt.show()
