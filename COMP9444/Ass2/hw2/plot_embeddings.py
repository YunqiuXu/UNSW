import numpy as np
import matplotlib

# if you get the error: "TypeError: 'figure' is an unknown keyword argument"
# uncomment the line below:
# matplotlib.use('Qt4Agg')

try:
    # pylint: disable=g-import-not-at-top
    from sklearn.manifold import TSNE
    import matplotlib.pyplot as plt
except ImportError as e:
    print(e)
    print('Please install sklearn, matplotlib, and scipy to show embeddings.')
    exit()

def plot_with_labels(low_dim_embs, labels, filename='tsne_embeddings.png'):
    assert low_dim_embs.shape[0] >= len(labels), 'More labels than embeddings'

    plt.figure(figsize=(18, 18))  # in inches
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label,
                     xy=(x, y),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')

    plt.savefig(filename)
    print("plots saved in {0}".format(filename))

if __name__ == "__main__":
    # Step 6: Visualize the embeddings.
    reverse_dictionary = np.load("Idx2Word.npy").item()
    embeddings = np.load("CBOW_Embeddings.npy")
    tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000, method='exact')
    plot_only = 500
    low_dim_embs = tsne.fit_transform(embeddings[:plot_only, :])
    labels = [reverse_dictionary[i] for i in range(plot_only)]
    plot_with_labels(low_dim_embs, labels)
    plt.show();
