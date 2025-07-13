import supervision as sv
from trackers import SORTTracker
from ultralytics import YOLO
import time
import keyboard
import cv2
import threading
import tkinter as tk
from tkinter import scrolledtext

stop_event = threading.Event()

# GUI Functions
def log(msg):
    log_box.config(state=tk.NORMAL)
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)
    log_box.config(state=tk.DISABLED)

def user():
    log("User thread started...")
    with open("C://Users//Anas computer//Desktop//IM Project//okasha.txt", "r") as f:
        okasha_distance = float(f.readlines()[-1])

    with open("C://Users//Anas computer//Desktop//IM Project//speed.txt", "r") as f:
        speed_lines = f.readlines()

    with open("C://Users//Anas computer//Desktop//IM Project//jawwad.txt", "r") as f:
        jawwad_distance = float(f.readlines()[-1])

    with open("C://Users//Anas computer//Desktop//IM Project//total.txt", "r") as f:
        total_distance = float(f.readlines()[-1])

    name = name_entry.get().lower().strip()
    time.sleep(1)
    log(f"Tracking user: {name}")

    if name == "jawwad":
        for line in speed_lines:
            if stop_event.is_set() or keyboard.is_pressed('k'):
                stop_event.set()
                break
            start = time.time()
            speed = float(line)
            if speed > 52:
                log("Moving Fast")
                speed = 45
                with open("C://Users//Anas computer//Desktop//IM Project//new_speed.txt", "a") as f:
                    f.write(str(speed) + '\n')
                interval = (time.time() - start)/3600
                distance = speed * interval
                jawwad_distance += distance
                total_distance += distance
            else:
                log("Moving Normal")
                interval = (time.time() - start)/3600
                distance = speed * interval
                jawwad_distance += distance
                total_distance += distance
        with open("C://Users//Anas computer//Desktop//IM Project//jawwad.txt", "a") as f:
            f.write(str(jawwad_distance) + '\n')
        with open("C://Users//Anas computer//Desktop//IM Project//total.txt", "a") as f:
            f.write(str(total_distance) + '\n')

    elif name == "okasha":
        for line in speed_lines:
            if stop_event.is_set() or keyboard.is_pressed('k'):
                stop_event.set()
                break
            start = time.time()
            speed = float(line)
            if speed > 45:
                log("Moving Fast")
                speed = 40
                with open("C://Users//Anas computer//Desktop//IM Project//new_speed.txt", "a") as f:
                    f.write(str(speed) + '\n')
                interval = (time.time() - start)/3600
                distance = speed * interval
                jawwad_distance += distance
                total_distance += distance
            else:
                log("Moving Normal")
                interval = (time.time() - start)/3600
                distance = speed * interval
                jawwad_distance += distance
                total_distance += distance
            time.sleep(0.1)
            interval = (time.time() - start)/3600
            distance = speed * interval
            okasha_distance += distance
            total_distance += distance
        with open("C://Users//Anas computer//Desktop//IM Project//okasha.txt", "a") as f:
            f.write(str(okasha_distance) + '\n')
        with open("C://Users//Anas computer//Desktop//IM Project//total.txt", "a") as f:
            f.write(str(total_distance) + '\n')
    log("User tracking complete.")

def tracking():
    log("Tracking thread started...")
    tracker = SORTTracker()
    model = YOLO("yolo11m.pt")
    annotator = sv.LabelAnnotator(text_position=sv.Position.CENTER)

    def callback(frame, _):
        if stop_event.is_set() or keyboard.is_pressed('k'):
            stop_event.set()
            return frame
        result = model(frame)[0]
        detections = sv.Detections.from_ultralytics(result)
        detections = tracker.update(detections)
        return annotator.annotate(frame, detections, labels=detections.tracker_id)

    sv.process_video(
        source_path="C://Users//Anas computer//Desktop//tracking.mp4",
        target_path="C://Users//Anas computer//Desktop//output.mp4",
        callback=callback,
    )
    log("Tracking thread stopped.")

def detection():
    log("Detection thread started...")
    cap = cv2.VideoCapture(0)
    model = YOLO("yolo11n.pt")
    while True:
        if stop_event.is_set() or keyboard.is_pressed('k'):
            stop_event.set()
            break
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        img = results[0].plot()
        cv2.imshow("Live YOLO Detection", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()
            break
    cap.release()
    cv2.destroyAllWindows()
    log("Detection thread stopped.")

def start_all():
    stop_event.clear()
    threading.Thread(target=user).start()
    threading.Thread(target=tracking).start()
    threading.Thread(target=detection).start()

def stop_all():
    stop_event.set()
    log("Stopping all threads...")

# GUI Layout
root = tk.Tk()
root.title("Multi-Thread Control Panel")

tk.Label(root, text="Enter Your Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Button(root, text="Start All", command=start_all, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Stop All (or press 'k')", command=stop_all, bg="red", fg="white").pack(pady=5)

log_box = scrolledtext.ScrolledText(root, width=60, height=15, state=tk.DISABLED)
log_box.pack(pady=10)

root.mainloop()
