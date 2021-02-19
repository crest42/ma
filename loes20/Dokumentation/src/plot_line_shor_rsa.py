import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

warnings.filterwarnings("ignore",
                        message='Source ID', category=Warning, module='', lineno=0, append=False)


sns.set(context='paper', palette=sns.color_palette("Paired"))
sns.set_style(sns.axes_style("ticks"),
              {'axes.grid': True})
p = sns.color_palette("Paired")
def rsa_bit_to_qubit(n): #pylint: disable=invalid-name
    return 2*n+2

def dlog_bit_to_qubit(n): #pylint: disable=invalid-name
    return 9*n+np.log2(n)

types = ['Prime Factoring (RSA)', 'DLP (DH)']
bits = []
for i in range(2, 16):
    bits.append(2**i)

t = []
b = []
q = []
for bit in bits:
    qubits = rsa_bit_to_qubit(bit)
    t.append('rsa')
    b.append(bit)
    q.append(qubits)
for bit in bits:
    qubits = dlog_bit_to_qubit(bit)
    t.append('dlog')
    b.append(bit)
    q.append(qubits)


from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
tick = ticker.ScalarFormatter(useOffset=False, useMathText=True)

tc = [u"$2^{{{0}}}$".format((x)) for x in bits]

QC_MAX = {'Company': 'Google', 'Name': 'Bristlecone', 'qubit': 72}

d = {'type': t, 'Problem Space': b, 'Qubits': q}
df = pd.DataFrame(data=d)

fig, ax = plt.subplots()
ax.set_yscale('log')
g = sns.barplot(data=df, x='Problem Space', y='Qubits', hue='type', ax=ax)
g.set_xticklabels(tc)
g.axhline(QC_MAX['qubit'], c=p[5], linestyle='dashed', label='horizontal')


text = f"{QC_MAX['Company']} {QC_MAX['Name']} ({QC_MAX['qubit']})"

labels = [text] + types
handles, _ = ax.get_legend_handles_labels()
plt.legend(handles=handles, labels=labels)

#plt.show()
plt.savefig('loes20/Dokumentation/Latex/Bilder/plot_line_shor_rsa.pdf')
