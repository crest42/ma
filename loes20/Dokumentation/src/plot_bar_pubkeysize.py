from plot_cryptosystems import plot_cryptosystems_single_dim
from cryptosystems import KEM_KEX_DF

df = KEM_KEX_DF[KEM_KEX_DF['IND'] == 'CCA']
df = df.drop(['NTS-13-80'], level=2)
df = df.drop(['mceliece460896'], level=2)
df = df.sort_values('Public Key Size')

plt = plot_cryptosystems_single_dim(data=df, x_col='Cipher', 
                                    y_col='Public Key Size',
                                    level=3,
                                    hue_col='Type',
                                    rotation=45,
                                    )


plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_bar_pubkeysize.pdf')
#plt.show()
