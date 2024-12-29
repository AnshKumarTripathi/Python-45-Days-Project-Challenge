import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from unet_model import unet_model
from load_data import X_train, Y_train

# Data augmentation
data_gen_args = dict(rotation_range=15,
                     width_shift_range=0.1,
                     height_shift_range=0.1,
                     shear_range=0.1,
                     zoom_range=0.2,
                     horizontal_flip=True,
                     fill_mode='nearest')

image_datagen = ImageDataGenerator(**data_gen_args)
mask_datagen = ImageDataGenerator(**data_gen_args)

# Creating image and mask generators
image_generator = image_datagen.flow(X_train, batch_size=32, seed=1)
mask_generator = mask_datagen.flow(Y_train, batch_size=32, seed=1)

def generate_data(image_gen, mask_gen):
    while True:
        image_batch = image_gen.__next__()
        mask_batch = mask_gen.__next__()
        yield (image_batch, mask_batch)

# Create TensorFlow dataset
train_dataset = tf.data.Dataset.from_generator(
    lambda: generate_data(image_generator, mask_generator),
    output_signature=(tf.TensorSpec(shape=(None, 32, 32, 3), dtype=tf.float32),
                      tf.TensorSpec(shape=(None, 32, 32, 1), dtype=tf.float32))
)

# Model compilation
model = unet_model(input_size=(32, 32, 3))
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# Model training
model.fit(train_dataset, epochs=10, steps_per_epoch=len(X_train)//32)
model.save('unet_model.h5')
