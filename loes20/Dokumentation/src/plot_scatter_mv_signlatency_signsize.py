from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import SIGN_DF

SIGN_DF = SIGN_DF[SIGN_DF['Round'] == 3]
plt = plot_cryptosystems_seaborn(SIGN_DF, 'sign23B', 'sign59B-50th',
                                 type='Multivariate',
                                 hue_col="Level",
                                 style_col='Algorithm',
                                 size_col='Public Key Size',
                                 xlabel='Signature Size for 23 Bytes Data',
                                 ylabel=r'Runtime to sign 59 Bytes in CPU Cycles',
                                 xscale='log',
                                 sizes= (40,200),
                                 yscale='log',
                                 title='Multivariate Signature Schemes', s=50)

#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_scatter_mv_signlatency_signsize.pdf')
