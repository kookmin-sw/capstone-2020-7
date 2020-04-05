import re

def parser(x=""):
    loss = float(re.findall('[^val]?\s*loss\d*\:\s*([^ ]*)\s*', x)[0])
    acc = float(re.findall('[^val]?\s*acc\d*\:\s*([^ ]*)\s*', x)[0])
    precision = float(re.findall('[^val]?\s*precision\d*\:\s*([^ ]*)\s*', x)[0])
    recall = float(re.findall('[^val]?\s*recall.?\d?\:\s*([^ ]*)\s*', x)[0])
    val_loss = float(re.findall('\s*val_loss\d*\:\s*([^ ]*)\s*', x)[0])
    val_precision = float(re.findall('\s*val_precision\d*\:\s*([^ ]*)\s*', x)[0])
    val_acc = float(re.findall('\s*val_acc\d*\:\s*([^ ]*)\s*', x)[0])
    val_recall = float(re.findall('\s*val_recall.?\d?\:\s*([^ ]*)\s*', x)[0])
    output = [loss, acc, precision, recall, val_loss, val_acc, val_precision, val_recall]
    return output

    
    
def extract(doc):
    loss = []
    acc = []
    precision = []
    recall = []
    val_loss = []
    val_acc = []
    val_precision = []
    val_recall = []
    seq = [loss, acc, precision, recall, val_loss, val_acc, val_precision, val_recall]
    for i, line in enumerate(doc):
        temp = []
        if "Epoch 000" in line:
            temp = parser(x=doc[i+1])
            for j, v in enumerate(temp):
                seq[j].append(v)
    return seq



if __name__=="__main__":
    PATH = ""
    with open(PATH, "r") as f:
        doc = f.read()
    loss = []
    acc = []
    precision = []
    recall = []
    val_loss = []
    val_acc = []
    val_precision = []
    val_recall = []
    loss, acc, precision, recall, val_loss, val_acc, val_precision, val_recall = extract(doc)