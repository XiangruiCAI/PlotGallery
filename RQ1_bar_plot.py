import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import argparse

from matplotlib.ticker import FormatStrFormatter
plt.style.use('seaborn-paper')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

FONTSIZE = 14
#matplotlib.rcParams.update({'font.size': FONTSIZE})

labels = ['NC', 'KMNC', 'TKNC']
legends = ['Pearson', 'Kendall', 'Spearman']
colors = ['cornflowerblue', 'sandybrown', 'silver']
hatches = ['////', '\\\\\\', '.']


class Plot(object):
    def __init__(self, inFile, outFile, title):
        self.inFile = inFile
        self.outFile = outFile
        self.title = title

    def dataLoader(self):
        return np.loadtxt(self.inFile, delimiter='\t')

    def plot(self, width=0.35,):
        data = self.dataLoader()
        print(data[0])
        assert len(labels) == data.shape[-1]
        data = data.transpose()
        x = np.arange(len(labels))
        fig, ax = plt.subplots(figsize = (4, 4))
        for (i, legend) in enumerate(legends):
            rect = ax.bar(x + (width + 0.15) * (i - 1) / 2.0, data[i], 0.6 * width, label=legend, color = colors[i]) # , hatch = hatches[i]
            #self._autoLabel(ax, rect)
        ax.set_ylabel('Correlation Coefficients', fontsize = FONTSIZE)
        ax.set_xlabel('Test Coverage Criteria', fontsize = FONTSIZE)
        # ax.set_title(self.title.replace('_', '\\_'))
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize = FONTSIZE - 2)
        ax.yaxis.set_tick_params(labelsize = FONTSIZE - 2)
        ax.set_ylim([0, 0.6])
        ax.legend(fontsize = FONTSIZE - 4)
        fig.tight_layout()
        plt.savefig(self.outFile, format='pdf', bbox_inches='tight')
        plt.show()

    def _autoLabel(self, ax, rects):
        '''Attach a text label above each bar in *reacts*, displaying its height.'''
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot the bar')
    parser.add_argument('-input', default='RQ1_LeNet1.txt')
    parser.add_argument('-output', default='RQ1_1.pdf')
    parser.add_argument('-title', default='LeNet_1')

    args = parser.parse_args()
    bar = Plot(args.input, args.output, args.title)
    bar.plot()
