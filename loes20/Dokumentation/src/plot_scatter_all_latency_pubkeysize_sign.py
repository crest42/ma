from plot_cryptosystems import plot_cryptosystems_seaborn
from cryptosystems import SIGN_DF

df = SIGN_DF
df = df[df['Round'].isin([-1,3])]
df = df[df['Level'].isin([5,3])]

plt, ax = plot_cryptosystems_seaborn(df, 'sum-50th', 'Public Key Size',
                                 hue_col="Algorithm",
                                 style_col='Type',
                                 xlabel=r'Authentication Runtime in CPU Cycles',
                                 ylabel='Public Key Bytes',
                                 xscale='log', yscale='log',
                                 title='')

rsa = df[df['Cipher'] == 'donald2048']
rsay = rsa['Public Key Size'].values[0]
rsax = rsa['sum-50th'].values[0]
curve25519 = df[df['Cipher'] == 'ed25519']
curve25519y = curve25519['Public Key Size'].values[0]
curve25519x = curve25519['sum-50th'].values[0]


ax.annotate('RSA2048',
            xy=(rsax+800000, rsay), xycoords='data',
            xytext=(60, -5), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')


ax.annotate('curve25519',
            xy=(curve25519x+80000, curve25519y), xycoords='data',
            xytext=(70, -5), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')


plt.savefig('loes20/Dokumentation/abschlussvortrag/plot_scatter_all_latency_pubkeysize_sign.pdf')
#plt.show()
