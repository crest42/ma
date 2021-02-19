from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import SIGN_DF
import numpy as np
df = SIGN_DF[SIGN_DF['Round'] == 3]

plt = plot_cryptosystems_seaborn(df, 'sign23B', 'sign59B-50th',
                                 type='Lattice',
                                 hue_col="Level",
                                 style_col='Algorithm',
                                 size_col='Public Key Size',
                                 sizes= (40,200),
                                 xlabel='Signature Size for 23 Bytes Data',
                                 ylabel=r'Runtime to sign 59 Bytes in CPU Cycles',
                                 title='Lattice-Based Signature Schemes', s=50)

#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_lattice_signlatency_signsize.pdf')


