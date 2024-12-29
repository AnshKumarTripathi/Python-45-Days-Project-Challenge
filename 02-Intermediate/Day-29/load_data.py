import numpy as np
import pickle
from tensorflow.keras.utils import to_categorical

def load_cifar10_batch(batch_filename):
    with open(batch_filename, 'rb') as file:
        dict = pickle.load(file, encoding='bytes')
        X = dict[b'data']
        Y = dict[b'labels']
        X = X.reshape(len(X), 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
        Y = np.array(Y)
    return X, Y

def load_cifar10_dataset(cifar10_dir):
    X_train = []
    Y_train = []
    for i in range(1, 6):
        batch_filename = cifar10_dir + '/data_batch_' + str(i)
        X, Y = load_cifar10_batch(batch_filename)
        X_train.append(X)
        Y_train.append(Y)
    X_train = np.concatenate(X_train)
    Y_train = np.concatenate(Y_train)
    
    X_test, Y_test = load_cifar10_batch(cifar10_dir + '/test_batch')
    
    return X_train, Y_train, X_test, Y_test

def preprocess_data(X, Y):
    X = X / 255.0
    Y = np.expand_dims(Y, axis=-1)  # Add a channel dimension
    Y = np.repeat(Y, 32 * 32, axis=-1).reshape(Y.shape[0], 32, 32, 1)
    return X, Y

cifar10_dir = 'D:/45-Days-Challege-JS-Python/Python/Learning-Projects/Python-45-Days-Project-Challenge/02-Intermediate/Day-29/dataset/cifar-10-batches-py'
X_train, Y_train, X_test, Y_test = load_cifar10_dataset(cifar10_dir)
X_train, Y_train = preprocess_data(X_train, Y_train)
X_test, Y_test = preprocess_data(X_test, Y_test)

print(f'Training data shape: {X_train.shape}')
print(f'Training mask shape: {Y_train.shape}')
print(f'Test data shape: {X_test.shape}')
print(f'Test mask shape: {Y_test.shape}')


