import cv2
import os

# Ask user for name
name = input("Enter the name of the person: ").strip()

# Create a directory for the dataset if it doesn't exist
dataset_dir = "dataset"
person_dir = os.path.join(dataset_dir, name)

if not os.path.exists(person_dir):
    os.makedirs(person_dir)
    print(f"[✅] Created directory for {name}")
else:
    print(f"[ℹ️] Directory already exists. New images will be added.")

# Start camera
cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print("[INFO] Starting camera. Press ESC to stop...")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        count += 1
        face = gray[y:y+h, x:x+w]
        img_path = os.path.join(person_dir, f"{str(count)}.jpg")
        cv2.imwrite(img_path, face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Capturing Faces", frame)

    key = cv2.waitKey(1)
    if key == 27 or count >= 50:  # ESC or 50 images
        break

cap.release()
cv2.destroyAllWindows()

print(f"[✅] Finished capturing faces for {name}.")
