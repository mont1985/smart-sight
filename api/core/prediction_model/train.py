# USAGE
# python train_network.py --dataset images --model dme.model
import matplotlib
# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from .lenet import LeNet
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import cv2
import os
from django.conf import settings
# set the matplotlib backend so figures can be saved in the background
matplotlib.use("Agg")


def generate_prediction_model():
    epochs = 2  # initialize the number of epochs to train for, initial learning rate, and batch size
    path_to_model = settings.MODEL_URL
    # path to general folder of images
    path_to_dataset = settings.DATASET_URL

    INIT_LR = 1e-3

    EPOCHS = int(epochs)

    BS = int(32)

    # initialize the data and labels
    print("[INFO] loading images...")
    data = []
    labels = []

    # grab the image paths and randomly shuffle them
    image_paths = sorted(list(paths.list_images(path_to_dataset)))

    random.seed(42)
    random.shuffle(image_paths)

    # loop over the input images
    for image_path in image_paths:
        if image_path[-3:] == ".md":
            print("Skipping Readme in {}".format(image_path))
            pass
        else:
            # load the image, pre-process it, and store it in the data list
            image = cv2.imread(image_path)
            image = cv2.resize(image, (28, 28))
            image = img_to_array(image)
            data.append(image)

            # extract the class label from the image path and update the
            # labels list
            label = image_path.split(os.path.sep)[-2]
            label = 1 if label == "Diabetic Macular Edema" else 0
            labels.append(label)
            pass

    # scale the raw pixel intensities to the range [0, 1]
    data = np.array(data, dtype="float") / 255.0
    labels = np.array(labels)

    # partition the data into training and testing splits using 75% of
    # the data for training and the remaining 25% for testing
    (trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.25, random_state=42)

    # convert the labels from integers to vectors
    trainY = to_categorical(trainY, num_classes=2)
    testY = to_categorical(testY, num_classes=2)

    # construct the image generator for data augmentation
    aug = ImageDataGenerator(
        rotation_range=30, width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest")

    # initialize the model
    print("[INFO] compiling model...")
    model = LeNet.build(width=28, height=28, depth=3, classes=2)
    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
    model.compile(
        loss="binary_crossentropy",
        optimizer=opt,
        metrics=["accuracy"])

    # train the network
    print("[INFO] training network...")
    H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
                            validation_data=(testX, testY),
                            steps_per_epoch=len(trainX) // BS,
                            epochs=EPOCHS, verbose=1)

    # save the model to disk
    print("[INFO] serializing network...")
    model.save(os.path.join(path_to_model, 'test.model'))

    print(
        "\n Training Accuracy: {}%\n Validation Accuracy: {}%\n Training Losss: {}%\n Validation Loss: {}%\n".format(
            round(H.history["acc"][-1]*100, 2),
            round(H.history["val_acc"][-1]*100, 2),
            round(H.history["loss"][-1]*100, 2),
            round(H.history["val_loss"][-1]*100, 2),
            indent=3))

    # plot the training loss and accuracy
    plt.style.use("ggplot")
    plt.figure()
    N = EPOCHS
    plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
    plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
    plt.title("Training Loss and Accuracy on Diabetic Macular Edema(DME)/Not DME")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")

    # Plot the coordinartes on a graph
    graph_path = os.path.join(settings.DATASET_URL, 'graphs/')
    plt.savefig(str(epochs) + "epochs.png")

    # Move generated image to the graphs folder
    file_path = os.path.join(os.getcwd(), str(epochs) + "epochs.png")
    os.replace(file_path, graph_path + str(epochs) + "epochs.png")