import matplotlib.pyplot as plt
def readSignal(path):
    noOfSamples=[]

    with open(path,"r") as f:
        n=0
        while True :
            l=f.readline()
            if not l :
                break
            n=int(l.strip())
            if n>0:
                break
        if(n<=0):
            print('There is not correct N in the file')
        else :
            for _ in range(n):
                indx,val=f.readline().split()
                noOfSamples.append((int(indx),float(val)))
    return n,noOfSamples

def plot_signal(samples, title, mode="plot", color='r', marker='o'):
    indexes = [x for x, _ in samples]
    values = [y for _, y in samples]

    plt.figure(figsize=(6,4)) 

    if mode == "plot":   
        plt.plot(indexes, values, marker=marker, linestyle='-', color=color)
    elif mode == "stem": 
        plt.stem(indexes, values, linefmt=color, markerfmt=color+marker, basefmt=" ")
    else:
        raise ValueError("mode must be either 'plot' or 'stem'")

    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def addOrSubSignals(sig1,sig2,op):

    sig1Dict=dict(sig1)
    sig2Dict=dict(sig2)
    all_Index=sig1Dict.keys() | sig2Dict.keys()
    print(all_Index)
    sorted_keys = sorted(all_Index)
    print(sorted_keys)
    addedsig=[]
    for i in (sorted_keys):
        valSig1=sig1Dict.get(i,0)
        valSig2=sig2Dict.get(i,0)
        print(valSig1)
        print(valSig2)
        if(op=='+'):
            addedSigval=valSig1+valSig2
        else:
              addedSigval=valSig1-valSig2
        addedsig.append((int(i),float(addedSigval)))

    print(addedsig)
# for _ in range(all_Index):
n1, sig1 = readSignal("txtFiles/Signal1.txt")
plot_signal(sig1, "Signal 1 visualization", mode="stem", color='r')

n2, sig2 = readSignal("txtFiles/Signal2.txt")
plot_signal(sig2, "Signal 2 visualization", mode="stem", color='b')

addOrSubSignals(sig1,sig2,'-')
plot_signal(sig2, "addedsignal visualization", mode="stem", color='g')

addOrSubSignals(sig1,sig2,'+')
plot_signal(sig2, "subsignal visualization", mode="stem", color='m')



        