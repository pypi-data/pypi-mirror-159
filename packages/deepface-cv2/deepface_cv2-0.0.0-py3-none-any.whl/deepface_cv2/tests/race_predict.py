import cv2
import numpy as np
from deepface import DeepFace
from deepface.commons import functions

from .. import preprocess

img_path = "deepface_cv2/tests/dataset/img10.jpg"

print(DeepFace.analyze(img_path, actions=('race',)))

faces = preprocess.preprocess_faces(img=img_path, target_size=(224, 224), grayscale=False,
                                    enforce_detection=True,
                                    detector_backend='opencv',
                                    return_region=True,
                                    align=True)


model = cv2.dnn.readNetFromONNX("deepface_cv2/race_model.onnx")

img, region = functions.preprocess_face(img=img_path, target_size=(224, 224), grayscale=False,
                                        return_region=True, align=False)

model.setInput(img)
out = model.forward()
print(out)

for f, r in faces:
    print("region test", r)
    print(f.shape)
    model.setInput(f)
    out = model.forward()
    # print(out)
    race_predictions = out[0, :]
    race_labels = ['asian', 'indian', 'black', 'white', 'middle eastern', 'latino hispanic']

    sum_of_predictions = race_predictions.sum()
    race = {}
    for i in range(0, len(race_labels)):
        race_label = race_labels[i]
        race_prediction = 100 * race_predictions[i] / sum_of_predictions
        race[race_label] = race_prediction

    dominant_race = race_labels[np.argmax(race_predictions)]
    print(race)
    print(dominant_race)

