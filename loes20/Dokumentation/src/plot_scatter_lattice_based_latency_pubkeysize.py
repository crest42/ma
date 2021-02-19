from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import KEM_KEX_DF

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = KEM_KEX_DF[KEM_KEX_DF['IND'] == 'CCA']
df = df[df['Round'] == 3]

#plt = plot_cryptosystems(x,y,legend=a,annotations=None, xlabel='k/Cycles', ylabel='Pubkeysize', xscale='log', yscale='log')
plt = plot_cryptosystems_seaborn(df, 'sum-50th', 'Public Key Size',
                                 type='Lattice',
                                 hue_col="Algorithm",
                                 style_col='Algorithm',
                                 xlabel=r'Key Exchange Runtime in CPU Cycles',
                                 ylabel='Public Key Bytes',
                                 xscale='log', yscale='log',
                                 title='Lattice-Based Key Exchanges',
                                 s=50 )


plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_lattice_based_latency_pubkeysize.pdf')
#plt.show()
