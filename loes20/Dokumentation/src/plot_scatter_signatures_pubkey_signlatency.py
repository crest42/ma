from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import SIGN_DF




plt = plot_cryptosystems_seaborn(SIGN_DF, 'pk_plus_sigmany', 'sum-50th',
                                 hue_col="Type",
                                 style_col='Type',
                                 xlabel='Public Key Size + Single Signature Size (Bytes)',
                                 ylabel='Sign 59B Latency in CPU Cycles',
                                 title='Multivariate Signature Schemes')

plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_signatures_pubkey_signlatency.pdf')

#plt.show()

