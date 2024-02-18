from keras.models import load_model
import numpy as np

labels = ['Red Soil', 'Clay Soil', 'Black Soil', 'Alluvial Soil', 'Slit SOil', 'Sand', 'Mary Soil', 'Chalky Soil']
MODEL_PATH = r"D:\Official\Reseach Projects\Official Project\soil-type-classification\models\DenseNet121v2_95.h5"

def load_CNN_model():
    model = load_model(MODEL_PATH)
    return model

def classify_image(img):
    model = load_CNN_model()
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)

    predicted_label = labels[predicted_class]
    accuracy = prediction[0][predicted_class]

    return predicted_label, accuracy
