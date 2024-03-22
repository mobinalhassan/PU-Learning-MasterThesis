import tensorflow as tf
from tensorflow.keras.datasets import mnist, cifar10
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from uitils import *
 
class DataLoader():

    def load_mnist(self):
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        # Normalize pixel values
        X_train, X_test = X_train / 255.0, X_test / 255.0
        # Reshape data to (num_samples, height, width, channels)
        X_train = np.expand_dims(X_train, axis=-1)
        X_test = np.expand_dims(X_test, axis=-1)
        return X_train, y_train, X_test, y_test

    def load_cifar10(self):
        (X_train, y_train), (X_test, y_test) = cifar10.load_data()
        # Normalize pixel values
        X_train, X_test = X_train / 255.0, X_test / 255.0
        return X_train, y_train, X_test, y_test
    
    def load_creditcard(self):
        creditcard_path =get_full_path('../datasets/creditcard.csv')
        # print(creditcard_path)
        df = pd.read_csv(creditcard_path)
        print(df.head())
        return df

if __name__ == "__main__":
    dataloader=DataLoader()
    # Load MNIST dataset
    X_train_mnist, y_train_mnist, X_test_mnist, y_test_mnist = dataloader.load_mnist()
    
    # Load CIFAR-10 dataset
    X_train_cifar10, y_train_cifar10, X_test_cifar10, y_test_cifar10 = dataloader.load_cifar10()

    # Load creditcard fraud
    train_test_craditcard= dataloader.load_creditcard()

    print(f"MNIST Train samples: {X_train_mnist.shape[0]}")
    print(f"CIFAR-10 Train samples: {X_train_cifar10.shape[0]}")
    print(f"Craditcard Train and test samples: {train_test_craditcard.shape[0]}")


