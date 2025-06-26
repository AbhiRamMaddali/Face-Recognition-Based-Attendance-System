# Face Recognition Based Attendance System

## 🌟 Overview

This project is a real-time face recognition attendance system that detects and identifies faces through a webcam and logs the attendance data directly into a Google Sheet using Google Sheets API.

---

## 📊 Tech Stack

* **Python 3.11** or later
* **OpenCV** for face detection and recognition
* **Google Cloud Platform** for service credentials
* **gspread** + **oauth2client** for integrating with Google Sheets API
* **Google Sheets** as cloud-based data storage

---

## 📊 Features

| Feature                | Description                                  |
| ---------------------- | -------------------------------------------- |
| 📹 Live Camera Feed    | Captures real-time video to detect faces     |
| 🧠 Face Recognition    | Identifies registered users using LBPH model |
| 🗒️ Attendance Logging | Logs name & timestamp into Google Sheet      |
| ✅ Session Management   | Ends attendance session on `ESC` key press   |

---

## 📦 File Structure

```
FaceAttendance/
|
|-- credentials.json        # Google API credentials file
|-- dump.py                 # Main Python script
|-- trainer.yml             # LBPH trained model file
|-- face_dataset/           # Dataset folder of captured face images
|-- attendance_log.csv      # (Optional) Local attendance backup
```

---

## ⚡ Workflow

1. **Camera Start** – Opens webcam using OpenCV.
2. **Face Detection** – Detects face using Haar cascade classifier.
3. **Face Recognition** – Recognizes faces using trained LBPH model.
4. **Google Sheet Logging** – Marks name & time on Google Sheet.
5. **ESC Key to Exit** – Ends camera feed and attendance logging.

---

## 🏢 Use Cases

* Classroom Attendance Automation
* Office Entry Logging
* Lab and Resource Access
* AI/ML-based Personal Security Systems

---

## ✨ Future Enhancements

* Face registration GUI
* Admin dashboard for reports
* Alert for unknown face detection
* Integration with email/SMS notifications

---

## 🌟 Credits

Built using Python, OpenCV, and Google Sheets API.

---

Want to collaborate or contribute? Feel free to [reach out](mailto:your.email@example.com) or fork the repo!
