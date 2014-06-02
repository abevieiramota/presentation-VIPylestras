from math import ceil
from matplotlib import pyplot as pl

MODEL_NAME = 'model'

NUM_COLS = 5
PLOT_LEN = 3
FONT_SIZE = 25
CMAP = 'gray_r'

def show_digits(digitos, ini, fim):
    
    num_digits = fim - ini + 1
    num_rows = int(ceil((1.*num_digits)/NUM_COLS))
    
    fig, axis = pl.subplots(num_rows, NUM_COLS, figsize=(PLOT_LEN*NUM_COLS, PLOT_LEN*num_rows))
    
    for ax in axis.ravel():
        
        ax.axis('off')
    
    for ax, i in zip(axis.ravel(), xrange(ini, fim+1)):
        
        # no lugar de data[i].reshape((8,8)) pode-se utilizar images[i]
        ax.imshow(digitos.data[i].reshape((8, 8)), cmap=CMAP, interpolation='nearest')
        ax.set_title('%d' % digitos.target[i], fontsize=FONT_SIZE)
        
def show_confusion_matrix(cm):
    
    fig = pl.figure(figsize=(5,5))
    ax = fig.add_subplot(1,1,1)
    im = ax.matshow(cm)
    ax.set_xlabel('predito')
    ax.set_ylabel('real')
    r_10 = range(10)
    ax.set_xticks(r_10)
    ax.set_xticklabels(r_10)
    ax.set_yticklabels(r_10)
    ax.set_yticks(r_10)
    _ = fig.colorbar(im)