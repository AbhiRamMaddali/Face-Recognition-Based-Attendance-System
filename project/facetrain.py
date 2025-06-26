import cv2
import numpy as np
import os

dataset_dir = "dataset"
model = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}  # maps label number to name
current_label = 0

for person_name in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person_name)
    if not os.path.isdir(person_path):
        continue

    label_map[current_label] = person_name

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        faces.append(img)
        labels.append(current_label)

    current_label += 1

print("[INFO] Training model...")
model.train(faces, np.array(labels))
model.save("trainer.yml")

# Save the label map for later use
import pickle
with open("labels.pickle", "wb") as f:
    pickle.dump(label_map, f)

print("[✅] Training complete and model saved.")
