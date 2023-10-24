# @title Keras Test Model
# EDA Step : . Goal:

import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import os

# Paths and Model Name
training_dir = '/content/drive/MyDrive/ST1 Capstone Project Image Dataset/training/'
validation_dir = '/content/drive/MyDrive/ST1 Capstone Project Image Dataset/validation/'
model_name = 'my_model.h5'
model_dir = '/content/drive/MyDrive/ST1 Capstone Project Image Dataset/'
model_path = os.path.join(model_dir, model_name)

# Constants and Class Names
class_names = ['Cheetahs', 'Lions']
num_epochs = 10
batch_size = 64

# Menu Dictionary
menu_options = {
    'initialise': {
        'A': 'Train New Model (Overwrites saved model)',
        'B': 'Fine Tune Current Model',
        'C': 'Validate Current Model',
        'X': 'Exit'
    },
    'save': {
        'A': 'Save Model',
        'B': 'Discard Changes'
    },
    'overwrite': {
        'A': 'Yes, overwrite the old model',
        'B': 'No, take me back'
    }
}


def create_new_model():
    model = keras.Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def load_existing_model():
    try:
        model = keras.models.load_model(model_path)
        print("Model successfully loaded")
    except FileNotFoundError as e:
        print(f"{e}: Could not find saved model.")
        return
    return model


def train_model(model_type):
    if model_type == 'new_model':
        model = create_new_model()
    elif model_type == 'saved_model':
        model = load_existing_model()

    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=40,
        brightness_range=[0.2, 1.8],
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        vertical_flip=True
    )

    train_generator = train_datagen.flow_from_directory(
        training_dir,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='binary',
        classes=class_names
    )

    model.fit(
        train_generator,
        epochs=num_epochs,
        steps_per_epoch=len(train_generator)
    )
    return model


def validate_model():
    model = load_existing_model()
    validation_datagen = ImageDataGenerator(rescale=1. / 255)

    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='binary',
        classes=class_names
    )

    average_loss, accuracy = model.evaluate(validation_generator)
    print(f'Average Loss: {average_loss:.4f}')
    print(f'Accuracy: {accuracy * 100:.2f}%')


def user_input(options):
    valid_options = options.keys()
    while True:
        option_description = "\n".join([f"{key}: {value}" for key, value in options.items()])
        input_value = input(f"What do you want to do:\n{option_description}\n")
        if input_value.upper() in valid_options:
            return input_value.upper()
        else:
            print("Invalid input. Please try again.")


def save_model(model):  # Save model menu
    input_value = user_input(menu_options['save'])
    if input_value == 'A':
        input_value = user_input(menu_options['overwrite'])
        if input_value == 'A':
            model.save(model_path)
            print(f"The model was saved to {model_path}")
        else:
            print("No model was saved")
    elif input_value is None:
        print("No model was saved")
        return


def main():  # Top level menu
    while True:
        input_value = user_input(menu_options['initialise'])
        if input_value == 'A':  # New model
            model = train_model('new_model')
            save_model(model)
        elif input_value == 'B':  # Fine tune model
            model = train_model('saved_model')
            save_model(model)
        elif input_value == 'C':  # Test model
            model = validate_model()
        elif input_value == 'X':
            break
        elif input_value is None:
            print("No model was saved")
            return


if __name__ == "__main__":
    main()
