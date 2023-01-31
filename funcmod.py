def plot_figs(df):
    """
    受け取ったデータを全てプロットする関数
    need to import: itertools, matplotlib.pyplot as plt, from matplotlib.dates import DateFormatter
    :param df: plotしたいpandas.Dataframe
    :return:
    """
    
    color_iter = itertools.cycle(["#02A8F3", "#33B490", "#FF5151", "#B967C7"])
    n_figs = df.columns.size # columnsの種類数
    fig = plt.figure(figsize=(6, 2.0*n_figs), dpi=100)
    x = df.index
    for i in range(n_figs):
        y = df.iloc[:, i]
        title = df.columns[i]
        ax = fig.add_subplot(n_figs, 1, i+1)
        ax.plot(x, y, color=next(color_iter), linewidth=1.0)
        ax.xaxis.set_major_formatter(DateFormatter("%H:%M"))
        ax.set_xlim(x[0], x[-1])
        ax.set_title(title, fontsize=12)
    fig.tight_layout()
    plt.show()
    plt.close()