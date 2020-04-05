from parse_history import extract, parser
import matplotlib.pyplot as plt

def draw_plot(data, data_label, val, val_label, title):
    x = ["epoch"+str(i+1) for i in range(len(data))]
    plt.plot(x, data, label=data_label)
    plt.plot(x, val, label=val_label)
    plt.xticks(rotation=-90)
    plt.legend(loc="best")
    plt.title(title)
    plt.show()
    
    
    
def draw_history(history):
    label_value = ["loss", "acc", "precision", "recall"]
    for i, v in enumerate(label_value):
        draw_plot(history[i], v, history[i+4], "val_"+v, v.upper())