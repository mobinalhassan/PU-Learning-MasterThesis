import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# .\tensorflow_gpu_env\Scripts\activate