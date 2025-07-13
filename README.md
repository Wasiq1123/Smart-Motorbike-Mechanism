# 🏍️ Smart Motorbike Mechanism

A **real-time multi-threaded system** that uses **YOLO object detection**, **speed tracking**, and a **graphical user interface (GUI)** to simulate a smart motorbike tracking platform. The system tracks and evaluates two users' (Jawwad and Okasha) movement behavior based on speed, estimates the distance traveled, and performs object tracking and live detection simultaneously.

---

## 📌 Key Features

✅ **YOLO-based Detection & Tracking**

✅ **User Movement Monitoring by Speed**

✅ **Speed-Based Distance Estimation**

✅ **Multi-threaded Execution**

✅ **Tkinter GUI with Logs and Controls**

✅ **Live Webcam Detection & Video Annotation**

✅ **Thread Stopping with Button or Keyboard Press**

---

## 📁 Directory Structure

```
📁 Smart_Motorbike_Mechanism
├── Smart Motorbike Mechanism.py          # 🧠 Main Python file (GUI + threads)
├── README.md                             # 📄 This file
├── jawwad.txt                            # 📊 Distance log for Jawwad
├── okasha.txt                            # 📊 Distance log for Okasha
├── speed.txt                             # 📈 Input speed values
├── new_speed.txt                         # ⚙️ Adjusted speed values
├── total.txt                             # 📊 Cumulative distance log
├── tracking.mp4                          # 🎥 Input video for tracking
├── output.mp4                            # 🧾 Output video with YOLO + SORT annotations
```

---

## 🧠 System Overview

This system integrates **YOLOv11** models for detection with custom logic to:

* Detect whether a rider (Okasha or Jawwad) is moving too fast
* Adjust the speed if necessary and calculate distance
* Annotate a pre-recorded video using `YOLOv11m` and `SORT` tracking
* Perform **live object detection** on webcam using `YOLOv11n`
* Display logs in a **scrollable Tkinter GUI**

---

## 🚀 How It Works

### 👤 User Thread (`user()`)

* Reads user's name from GUI

* Loads previous distance from `.txt` files

* Iterates through speeds in `speed.txt`

* Calculates traveled distance using:

  ```
  distance = speed × (time_elapsed / 3600)
  ```

* Adjusts speed if it exceeds safe thresholds:

  * > 52 km/h for **Jawwad** → adjusted to 45
  * > 45 km/h for **Okasha** → adjusted to 40

* Logs new distances in respective `.txt` files

---

### 📦 Object Tracking Thread (`tracking()`)

* Loads `tracking.mp4`
* Uses:

  * `YOLOv11m` for detection
  * `SORTTracker` for ID-based tracking
* Saves annotated output to `output.mp4`

---

### 🎥 Live Webcam Detection (`detection()`)

* Opens webcam feed using `OpenCV`
* Detects objects using `YOLOv11n`
* Displays live bounding boxes
* Exits on pressing **`q`** or **`k`**

---

## 💡 Tkinter GUI

* Input field for entering **name** (`jawwad` or `okasha`)
* **Start All** button: Starts all three threads
* **Stop All** button or **press `k`**: Stops threads immediately
* **Log window** shows real-time activity

---

## 🔧 Requirements

Install the following packages:

```bash
pip install ultralytics opencv-python supervision keyboard
```

> ⚠️ On Windows, `keyboard` may require admin privileges. Run Python as Administrator.

---

## 🧪 Example Workflow

1. Run `Smart Motorbike Mechanism.py`
2. Enter `jawwad` or `okasha` in the name field
3. Click **Start All**
4. Observe:

   * Speed-based distance logging
   * Object tracking on video
   * Real-time detection via webcam
5. Stop using **Stop All** or press **`k`**

---

## 📈 Distance Calculation Logic

For each speed reading:

```python
interval = (time.time() - start) / 3600  # Time in hours
distance = speed * interval              # Distance = speed × time
```

Speeds are conditionally adjusted and saved to `new_speed.txt`.

---

## 🧰 Technologies Used

| Tool                  | Purpose                           |
| --------------------- | --------------------------------- |
| YOLOv11 (Ultralytics) | Object detection (video + live)   |
| SORT Tracker          | Object tracking (ID-wise)         |
| OpenCV                | Video handling & live camera      |
| Supervision           | Annotation & detection management |
| Tkinter               | GUI design                        |
| Threading             | Parallel execution of features    |
| File I/O              | Logs speed and distance per user  |

---

## 🚧 Future Enhancements

* 📍 Integrate GPS/IMU for real-world tracking
* 📤 Upload data to cloud dashboards
* 📳 SMS/Notification system for overspeed alerts
* 🧠 ML model to predict accident risk based on speed behavior

---

## 🏁 Conclusion

This system acts as a prototype for **intelligent vehicle behavior monitoring**, combining **computer vision**, **GUI interactivity**, and **multi-threaded execution** for real-time detection and analysis.

---
