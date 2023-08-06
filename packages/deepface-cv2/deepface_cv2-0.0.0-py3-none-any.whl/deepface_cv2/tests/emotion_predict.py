import cv2
import numpy as np
from deepface import DeepFace
from deepface.commons import functions

from .. import preprocess

img_path = "deepface_cv2/tests/dataset/img10.jpg"

print(DeepFace.analyze(img_path, actions=('emotion',)))

faces = preprocess.preprocess_faces(img=img_path, target_size=(48, 48), grayscale=True,
                                    enforce_detection=True,
                                    detector_backend='opencv',
                                    return_region=True,
                                    align=True)

model = cv2.dnn.readNetFromONNX("deepface_cv2/facial_expression_model.onnx")

img, region = functions.preprocess_face(img=img_path, target_size=(48, 48), grayscale=True,
                                        return_region=True, align=False)

print("region benchmark", region)

model.setInput(img)
out = model.forward()
print(out)

for f, r in faces:
    print("region test", r)
    print(f.shape)
    model.setInput(f)
    out = model.forward()
    print(out)
    emotion_predictions = out[0, :]
    sum_of_predictions = emotion_predictions.sum()

    emotion = {}
    emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    for i in range(0, len(emotion_labels)):
        emotion_label = emotion_labels[i]
        emotion_prediction = 100 * emotion_predictions[i] / sum_of_predictions
        emotion[emotion_label] = emotion_prediction
    print(emotion)
    print(emotion_labels[np.argmax(emotion_predictions)])




