# **VisionLab**

![Version](https://img.shields.io/badge/version-v1.2.2-blue)
![Status](https://img.shields.io/badge/status-active%20development-orange)

### Real-Time Computer Vision & Gesture-Based Interaction

VisionLab is a real-time computer vision experiment with the intention of exploring the possibility of new ways to interact with and control computer vision through a camera.

The current version features real-time camera processing with multiple vision modes while the future versions intend on implementing gesture-based controls for the computer vision system

---

# 📦 Installation

## Method-1

STEP 1: Install .zip file from <a href="https://github.com/aaravshrivastava4129/VisonLab/releases/tag/v1.2.2">Releases</a>.

STEP 2: Extract it.

STEP 3: Go to VisionLab -> dist -> main

STEP 4: Double click main.exe

---

## Method-2

STEP 1: Clone the repository

```bash

git clone https://github.com/aaravshrivastava4129/VisonLab.git

```

STEP 2: Go to the project folder

```bash

cd VisionLab

```

STEP 3: Install the required packages

```bash

pip install -r requirements.txt

```

STEP 4: Run the project

```bash

python main.py

```

---

## 🎬 Demo Video
*This project is in active development, so the videos provided in the README may vary from the actual product.

<video src="https://github.com/user-attachments/assets/02eafeff-86f2-48e6-ae98-640dbd39c3d2" width="100%" controls></video>

---

## 📸 Screenshots
*This project is in active development, so the screenshots provided in the README may vary from the actual product.

### Main Interface

![VisionLab Main Interface](screenshots/MainInterface.png)

### Main Interface With Mode Menu

![VisionLab Main Interface With Mode Menu](screenshots/MainInterfaceWithModeMenu.png)

### Normal Vision Mode

![Normal Vision Mode](screenshots/NormalMode.png)

### Grayscale Vision Mode

![Grayscale Vision Mode](screenshots/GrayscaleMode.png)

### Edge Detection Mode

![Edge Detection Mode](screenshots/EdgeMode.png)

> More screenshots will be added as more features are added

---

## ✨ Current Features

### 🎥 Real-Time Camera Feed

A real-time camera feed can be viewed inside of VisionLab with its own dedicated visual interface.

The camera is mirrored so that it can be used as a natural control input

### 🖼️ Multiple Vision Modes

VisionLab houses multiple vision modes, with the intention of expanding upon them in future versions.

The following vision modes are available in the current version:

Normal — The camera view is displayed normally

Grayscale — The camera view is converted to grayscale

Edges — The camera view has its edges extracted

### 🎛️ Vision Mode Control

The vision modes can be changed inside of VisionLab by utilzing the dedicated vision mode controls.

The current vision mode is displayed in the side pannel of the application window

### 📊 Live System Information

The current status of the computer vision system is displayed alongside the camera feed in VisionLab.

Some of the information that can be viewed includes:

System status

Camera status

Camera resolution

FPS counter

Current vision mode

### ⚡ Real-Time Performance Display

The current performance of the computer vision system is displayed in real-time by showing how many frames are being processed per second (FPS counter).

### 🖥️ Dedicated Computer Vision Interface

VisionLab has its own dedicated interface that is built around the computer vision system, which includes the camera feed, system information, vision mode controls, and application status.

### ▶️ Start / Stop System

The computer vision system can be started and stopped by utilizing the dedicated start/stop button.

---

# 🚀 Upcoming Features

The future versions of VisionLab intend on implementing gesture-based interactions.

## 🖐️ Four-Finger Gesture Control

The next major feature to be implemented is hand gesture control.

The four fingers of the hand will be utilized to form a rectangular interaction area.

```

Finger ●──────────────────────● Finger
       │                      │

       │     GESTURE AREA     │

       │                      │
Finger ●──────────────────────● Finger

```

The four fingers will be utilized to form the corners of the rectangular interaction area.

---

## 🔲 Gesture-Based Mode Switching

The rectangular interaction area will be utilized to change vision modes.

By detecting hand gestures inside of this area, VisionLab will be able to switch vision modes by solely utilizing gestures.

---

## 👆 Natural Camera Interaction

The ultimate goal of VisionLab is to evolve beyond a camera-based computer vision system and become a computer vision system that utilizes the camera as an input device.

VisionLab will gradually transition towards making the camera more interactive by implementing different levels of gesture-based control

---

## 🧠 Future Vision Modes

The future versions of VisionLab will implement additional computer vision modes.

Some of the following are just a few examples of what computer vision modes will be possible in the future:

Hand tracking

Object detection

Motion detection

Face/feature tracking

Gesture detection

Real-time effects

Interactive vision experiments

---

# 🎯 Project Roadmap

This roadmap highlights the current progress, future updates, and future goals that VisionLab intends to achieve.

### ✅ Completed

Real-time camera feed

Normal vision mode

Grayscale vision mode

Edges vision mode

FPS counter

Camera status

Resolution information

Vision mode status

Start/stop controls

Dedicated computer-vision interface

### 🔄 Next

🖐️ Four-finger detection

🔲 Four-finger rectangle formation

👆 Gesture interaction inside of the rectangle

🎛️ Switch vision modes by utilizing gestures

### 🔮 Future

More hand gestures

More computer-vision modes

More gesture interaction

Object and motion recognition

More camera-based controls

More natural human-computer interaction

---

# 🌐 VisionLab's Direction

VisionLab is being developed towards a simple idea of

making computer vision not only capable of seeing the world, but also being able to interact with the computer.

The project is transitioning from being a regular computer vision application towards a novel interface that will enable human-computer interaction through gestures.

---

## 📌 Current Version

VisionLab v1.2.2

Status: 🚧 Active Development

Next Major Update: 🖐️ Four-Finger Gesture-Based Interaction