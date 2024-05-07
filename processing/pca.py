import matplotlib.pyplot as plt

def plot_correlation_circle(pca_result, feature_names, component1 = 0, component2 = 1, title = "PCA Correlation Circle"):
    plt.figure(figsize=(20, 20))
    circle = plt.Circle((0, 0), 1, color='blue', fill=False)
    plt.gca().add_patch(circle)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    for i, feature in enumerate(feature_names):
        plt.arrow(0, 0, pca_result.components_[component1, i] * 2, pca_result.components_[component2, i] * 2, color='red', alpha=0.5, linewidth=0.5)
        plt.text(pca_result.components_[component1, i] * 2.5, pca_result.components_[component2, i] * 2.5, feature, color='black', ha='right', va='bottom', fontsize=8)

    plt.xlabel(f'PC1 ({pca_result.explained_variance_ratio_[0]*100:.2f}%)')
    plt.ylabel(f'PC2 ({pca_result.explained_variance_ratio_[1]*100:.2f}%)')
    plt.title(title)
    plt.grid()
    plt.axis('equal')
    plt.show()