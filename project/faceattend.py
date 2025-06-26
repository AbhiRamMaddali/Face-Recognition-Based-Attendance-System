import cv2
import os
import pickle
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load trained recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Load label-to-name map
with open("labels.pickle", "rb") as f:
    label_map = pickle.load(f)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("FaceAttendance").sheet1

# Start webcam
cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

marked_names = set()
print("[INFO] Starting camera... Press ESC to stop")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi)
        name = label_map.get(label, "Unknown")

        if name != "Unknown" and name not in marked_names and confidence < 80:
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")

            sheet.append_row([name, date_str, time_str])
            marked_names.add(name)
            print(f"[✅] Marked attendance for {name} at {date_str} {time_str}")

        color = (0, 255, 0) if confidence < 80 else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
print("[INFO] Attendance session ended.")
