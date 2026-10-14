# 🤖 AI Smart Object Detection System

A real-time object detection application built with **Python, OpenCV, and YOLOv8n**. The system uses a webcam to detect objects, display their confidence scores, estimate their relative distance based on bounding-box size, and count detected objects.

## ✨ Features

* **Real-Time Object Detection:** Detects objects through a webcam using YOLOv8n.
* **Bounding Boxes:** Draws rectangles around detected objects.
* **Confidence Scores:** Displays the model's confidence score for each detection.
* **Relative Distance Estimation:** Categorizes objects as Very Close, Close, Medium, or Far based on their bounding-box area.
* **Object Counter:** Displays the total number of detections in each frame.
* **Live Visualization:** Shows detection results in an OpenCV window titled `AI Smart Radar`.
* **Simple Controls:** Press `Q` to exit the application.

## 🛠️ Technologies Used

* **Python** — Main programming language.
* **OpenCV** — Webcam access, image processing, and visualization.
* **Ultralytics YOLOv8n** — Pretrained deep learning model for object detection.

## 📁 Project Structure

```text
AI-Smart-Object-Detection-System/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** The `yolov8n.pt` model weights are downloaded automatically by Ultralytics when they are not available locally, provided the application has internet access and the model can be retrieved successfully.

## ⚙️ Requirements

* Python 3.10 or another Python version supported by your installed Ultralytics and PyTorch dependencies.
* A working webcam.
* An internet connection for installing dependencies and downloading model weights when needed.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-smart-object-detection-system.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd ai-smart-object-detection-system
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows — Command Prompt:**

```cmd
.venv\Scripts\activate
```

**Windows — PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install the Required Libraries

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The requirements file installs the libraries needed for object detection and image processing.

### 6. Run the Application

```bash
python main.py
```

The application opens your webcam and displays detected objects with their labels, confidence scores, estimated relative distances, and the total detection count.

Press **Q** to close the application.

## 📦 Dependencies

The project uses the following Python packages:

| Library         | Purpose                                                |
| --------------- | ------------------------------------------------------ |
| `ultralytics`   | Loads and runs the YOLOv8n object detection model.     |
| `opencv-python` | Captures webcam frames and displays detection results. |

These packages are installed automatically using `requirements.txt`.

## 📏 Distance Estimation

The application estimates relative distance using the area of each detected object's bounding box.

| Bounding-Box Area            | Estimated Category |
| ---------------------------- | ------------------ |
| Greater than 150,000 pixels² | Very Close         |
| Greater than 70,000 pixels²  | Close              |
| Greater than 30,000 pixels²  | Medium             |
| 30,000 pixels² or less       | Far                |

**Important:** These categories are rough visual estimates, not actual physical distance measurements. Bounding-box size also depends on the object's real size, camera resolution, and viewing angle.

## ⚠️ Limitations

* Requires a working webcam for the current implementation.
* Detection performance depends on hardware, lighting, and camera quality.
* The application uses a pretrained model and does not train a new model.
* The distance categories are based on bounding-box area and are not calibrated measurements.
* The current object counter counts detections in each frame, not unique objects tracked across time.

## 👨‍💻 Author

**Mohammad Zubair Safi**

Software Engineering Student | Web Developer | AI & Machine Learning Enthusiast

## 📄 License

No license has been selected for this project yet. Please contact the author for permission before redistributing or reusing the code.
