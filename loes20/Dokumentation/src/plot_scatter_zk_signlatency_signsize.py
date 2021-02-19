from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import SIGN_DF

plt = plot_cryptosystems_seaborn(SIGN_DF, 'sign23B', 'sign59B-50th',
                                 type='ZK-Proof',
                                 hue_col="Cipher",
                                 size_col='Public Key Size',
                                 sizes= (40,200),
                                 xlabel='Signature Size for 23 Bytes Data',
                                 ylabel=r'Runtime to sign 59 Bytes in CPU Cycles',
                                 title='ZK-Based Signature Schemes', s=50)

#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_zk_signlatency_signsize.pdf')


