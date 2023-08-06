import cv2
import numpy as np
from deepface import DeepFace
from deepface.commons import functions

from .. import preprocess

img_path = "deepface_cv2/tests/dataset/img10.jpg"

print(DeepFace.analyze(img_path, actions=('age',)))

faces = preprocess.preprocess_faces(img=img_path, target_size=(224, 224), grayscale=False,
                                    enforce_detection=True,
                                    detector_backend='opencv',
                                    return_region=True,
                                    align=True)

model = cv2.dnn.readNetFromONNX("deepface_cv2/age_model.onnx")

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
    age_predictions = out[0, :]
    # print(age_predictions)
    output_indexes = np.arange(101)
    apparent_age = np.sum(age_predictions * output_indexes)
    print(int(apparent_age))




