import matplotlib.pyplot as plt
import pandas as pd


def show_plot(a: int, args: tuple, path: str):
    df = pd.read_excel(path)
    df['Length'] = df['Length'] + a
    plt.plot(df['Length'], df['Value'], label='Численное решение', color='blue')
    plt.plot(args[0], args[1], label='Аналитическое решение', color='tab:red', marker='o', linestyle='')
    plt.legend()
    plt.show()
