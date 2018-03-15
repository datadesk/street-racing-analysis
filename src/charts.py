import squarify
import seaborn as sns
import matplotlib.pyplot as plt


def tree(value_counts, figwidth=12, figheight=5):
    """
    Accepts a DataFrame value_counts series. Returns a donut chart.
    """
    sns.set_color_codes("pastel")
    fig = plt.figure(figsize=(figwidth, figheight))
    squarify.plot(
        sizes=value_counts,
        label=["{} ({:.1f}%)".format(k[:15], v*100) for k, v in zip(value_counts.index, value_counts)],
        color=sns.color_palette("Blues"),
        alpha=.9
    )
    ax = plt.axis('off')
    

def bar(value_counts, figwidth=6, figheight=4):
    """
    Accepts a DataFrame value_counts series. Returns a labeled bar chart.
    """
    sns.set(style="whitegrid")
    sns.set_color_codes("pastel")
    
    # Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(figwidth, figheight))

    # Create the plot
    fig = sns.barplot(x=value_counts.index, y=value_counts, color="b")

    # Trim down the chartjunk
    ax.set(ylabel="")
    sns.despine(left=True, bottom=True)

    # Label the values
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x()+p.get_width()/2.0, # x position
            height + (ax.get_ylim()[1] * 0.0125), # y position
            int(height), # label
            ha="center"
        )
    