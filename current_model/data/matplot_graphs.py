import matplotlib.pyplot as plt

def plot_graph(data_1):

    #plt.style(["science","notebook","grid"])

    plt.plot(data_1.time,data_1.change,markeredgecolor = "#FF0000")

    plt.title("energy change over time")

    plt.xlabel("time")
    plt.ylabel("% energy change")

    plt.show()