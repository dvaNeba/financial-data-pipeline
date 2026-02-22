import matplotlib.pyplot as plt

def visualize(df):
    plt.figure(figsize=(12,6))
    #plt.plot(df["close"], label="Close Price")
    #plt.plot(df["ma_20"], label="MA 20")
    #plt.plot(df["ma_50"], label="MA 50")

    plt.plot(df["date"], df["close"], label="Close Price")
    plt.plot(df["date"], df["ma_20"], label="MA 20")
    plt.plot(df["date"], df["ma_50"], label="MA 50")


    plt.legend()
    plt.title("Stock Price with Moving Averages")
    plt.show()

