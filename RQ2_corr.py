import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import argparse
import csv

from matplotlib.ticker import FormatStrFormatter
plt.style.use('seaborn-paper')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

FONTSIZE = 14
#matplotlib.rcParams.update({'font.size': FONTSIZE})

labels = ['KMNC', 'NC', 'TKNC']
style = ['r-o', 'g--^', 'm-.D']
style_wo_mark = ['r-', 'g--', 'm-.']


class Plot(object):
    def __init__(self, inFile, outFile):
        self.inFile = inFile
        self.outFile = outFile

    def dataLoader(self):
        data = []
        with open(self.inFile, 'r') as dataFile:
            dataReader = csv.reader(dataFile, delimiter='\t')
            for row in dataReader:
                numbers = []
                for item in row:
                    if item.strip() != '':
                        numbers.append(float(item))
                data.append(numbers)
        return data

    def plot(self, width=0.35,):
        data = self.dataLoader()
        print(data)
        fig, ax = plt.subplots(figsize=(5, 5))
        for i in range(3):
            ax.plot(data[3*i], data[3*i+1], style_wo_mark[i])
            sig_idx = []
            sig_data = []
            for (k, item) in enumerate(data[3*i+1]):
                if data[3*i+2][k] == 0:
                    sig_idx.append(data[3*i][k])
                    sig_data.append(item)
            ax.plot(sig_idx, sig_data, style[i], label=labels[i])
        ax.set_ylabel('Pearson Correlation Coefficient', fontsize=FONTSIZE)
        ax.set_xlabel('Test Suite Size', fontsize=FONTSIZE)
        # ax.set_title(self.title.replace('_', '\\_'))
        ax.set_xticks(np.arange(1100, step=100))
        ax.set_ylim((-0.1, 0.65))
        ax.yaxis.set_tick_params(labelsize=FONTSIZE - 4)
        ax.xaxis.set_tick_params(labelsize=FONTSIZE - 4)
        ax.legend(fontsize=FONTSIZE - 4, loc='upper right')
        fig.tight_layout()
        plt.savefig(self.outFile, format='pdf', bbox_inches='tight')
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot the correlation lines')
    parser.add_argument('-input', default='RQ2_Pearson_LeNet1.txt')
    parser.add_argument('-output', default='RQ2_Pearson_LeNet1.pdf')

    args = parser.parse_args()
    lines = Plot(args.input, args.output)
    lines.plot()
