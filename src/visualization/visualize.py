import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importances(model, feature_names):
    """Plot the importance of features for a given model."""
    importances = model.coef_[0]
    indices = np.argsort(importances)
    plt.figure(figsize=(10, 6))
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.show()
