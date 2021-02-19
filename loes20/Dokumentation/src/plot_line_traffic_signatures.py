from plot_cryptosystems import plot_cryptosystems_single_dim
from cryptosystems import SIGN_DF
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas
def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)
    percentile_.__name__ = 'percentile_%s' % n
    return percentile_

def traffic(single, subscriber):
    return float(subscriber*(2.0*single))

df = SIGN_DF
df = df[df['Level'] == 3]
df= df.reset_index(drop=True)
colors = sns.color_palette("Paired")
df = df[['Level','Type','Data Size']].groupby(['Type','Level']).agg([percentile(25), percentile(50), percentile(75)])

data = np.empty((0,6))
for x in df.index:
    p10 = df.loc[x]['Data Size']['percentile_25']
    p50 = df.loc[x]['Data Size']['percentile_50']
    p90 = df.loc[x]['Data Size']['percentile_75']
    for i in range(10,100, 1):
        val =[x[0], x[1], int(i),  traffic(p10, i), traffic(p50, i), traffic(p90, i)]
        data = np.vstack((data, val))

data_df = pandas.DataFrame(data, columns=['Type', 'Level', 'num','lower', 'val', 'upper'])
data_df.lower = data_df.lower.astype(float) 
data_df.val = data_df.val.astype(float) 
data_df.upper = data_df.upper.astype(float) 
data_df.num = data_df.num.astype(int) 
print(data_df)

g = sns.relplot(data=data_df, x="num", y="val", row="Type", kind="line", facet_kws={'sharey': False, 'sharex': True})
#g = g.map(plt.lineplot, "num", "val")

#g = sns.lineplot(data=data_df, x='num', y='val', hue='Type')
#g.set_yscale('log')

#plt.show()
#plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_line_traffic_signature.pdf')
