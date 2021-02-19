from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import SIGN_DF
import pandas as pd

SIGN_DF = SIGN_DF[SIGN_DF['Type'] == 'Hash']
SIGN_DF = SIGN_DF[SIGN_DF['Round'] == 3]
SIGN_DF['s'] =  SIGN_DF['Cipher'].str.split('sphincs', expand=True)[1]
SIGN_DF['sorf'] = SIGN_DF['s'].str[:1]
SIGN_DF['Key Size'] = SIGN_DF['s'].str[1:4]
SIGN_DF['type'] = None
tmp1 = SIGN_DF[SIGN_DF['sorf'] == 's'] 
tmp1['type'] = 's(ize)-variant'
tmp2 = SIGN_DF[SIGN_DF['sorf'] == 'f'] 
tmp2['type'] = 'f(ast)-variant'

SIGN_DF = pd.concat([tmp1,tmp2])

plt = plot_cryptosystems_seaborn(SIGN_DF, 'sign23B', 'sign59B-50th',
                                 type='Hash',
                                 hue_col="Level",
                                 style_col='type',
                                 size_col='Public Key Size',
                                 xlabel='Signature Size for 23 Bytes Data',
                                 ylabel=r'Runtime to sign 59 Bytes in CPU Cycles',
                                 #xscale='log',
                                 yscale='log',
                                 sizes= (40,200),
                                 title='Hash-Based Signature Schemes', s=50)

#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_hash_based_signlatency_signsize.pdf')


