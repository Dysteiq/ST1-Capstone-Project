import tensorflow as tf

print("GPU support:", tf.test.is_built_with_gpu_support())
print("GPU available: ", tf.config.list_physical_devices('GPU'))
print(tf.__version__)
