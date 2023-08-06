import os
import sys

import keras
import onnx
import tf2onnx

from deepface.extendedmodels import Age, Gender, Race, Emotion

from deepface.basemodels import VGGFace, OpenFace, Facenet, Facenet512, FbDeepFace, DeepID, DlibWrapper, ArcFace, Boosting, SFaceWrapper


# model = Age.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "age_model.onnx")


# model = Gender.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "gender_model.onnx")
#
# model = Race.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "race_model.onnx")

# model = Emotion.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# #onnx.save_model(model_pro, "facial_expression_model.onnx")
# print(onnx.helper.printable_graph(model_pro.graph))


# model = VGGFace.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "vgg_face.onnx")

#
# model = OpenFace.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "open_face.onnx")
#
# model = Facenet.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "facenet.onnx")
#
# model = Facenet512.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "facenet512.onnx")
#
# model = DeepID.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "deepid.onnx")
#
# model = ArcFace.loadModel()
# model_pro, storage = tf2onnx.convert.from_keras(model)
# onnx.save_model(model_pro, "arcface.onnx")

model = FbDeepFace.loadModel()
model_pro, storage = tf2onnx.convert.from_keras(model)
onnx.save_model(model_pro, "fbdeepface.onnx")
