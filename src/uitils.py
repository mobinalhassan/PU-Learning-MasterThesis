import os


ROOT = __file__
def get_full_path(*paths):
    root_dir = os.path.dirname(ROOT)
    full_path = os.path.join(root_dir, *paths)
    return full_path

# fp=get_full_path('..\datasets\creditcard.csv')
# print(f"fullPath:{fp}")


import matplotlib.pyplot as plt
import numpy as np

def plot_images(images, labels, predictions=None):
    """Plot images with their labels. Show predictions if provided."""
    n = images.shape[0]
    sqrt_val = int(np.ceil(np.sqrt(n)))
    fig, axes = plt.subplots(sqrt_val, sqrt_val, figsize=(10, 10))
    
    for i, ax in enumerate(axes.flat):
        if i >= n:
            break
        ax.imshow(images[i], cmap='binary')
        
        if predictions is not None:
            ax.set_title(f"True: {labels[i]}\nPred: {predictions[i]}")
        else:
            ax.set_title(f"Label: {labels[i]}")
        
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()



def extract_samples(x, y, n_samples=100):
    # Initialize empty lists to hold the samples and labels
    x_samples = []
    y_samples = []
    
    # Loop over each unique class in the dataset
    for class_num in np.unique(y):
        # Find the indices where the class label equals the current class number
        class_indices = np.where(y == class_num)[0]
        # Select n_samples of these indices randomly
        sample_indices = np.random.choice(class_indices, n_samples, replace=False)
        # Append the selected samples and labels to the lists
        x_samples.append(x[sample_indices])
        y_samples.append(y[sample_indices])
    
    # Concatenate all class samples and labels together
    x_samples = np.concatenate(x_samples, axis=0)
    y_samples = np.concatenate(y_samples, axis=0)
    
    return x_samples, y_samples