# Object Sight

A small computer-vision learning experiment focused on teaching a computer to detect and label objects in images, prerecorded video, and eventually a live camera feed.

This repository is intentionally scoped as a hands-on self-education lab rather than a production application.

## Goal

Build a simple object-detection pipeline that can:

1. Read an image or video frame.
2. Pass it through a pretrained object-detection model.
3. Detect common objects such as people, chairs, cups, phones, cars, and animals.
4. Draw bounding boxes around detected objects.
5. Display labels and confidence scores.
6. Eventually run the same pipeline on a live camera feed.

## Planned Stack

- **Python** — experiment and application logic
- **OpenCV** — image/video capture and frame processing
- **YOLO** — pretrained object detection

## Learning Goals

This project is an introduction to:

- Computer vision fundamentals
- Image and video frame processing
- Pretrained machine-learning models
- Object detection
- Bounding boxes
- Confidence scores
- Real-time inference
- Basic computer-vision performance considerations

## First Milestone

Keep the first version deliberately small:

> Load one image, detect the objects in it, and output an annotated image containing bounding boxes, labels, and confidence scores.

Once that works, move to prerecorded video and then a live camera feed.

## Scope

Object Sight is initially about **object detection**, not identifying specific people. The goal is for the system to recognize categories such as `person`, `chair`, or `cup`, rather than determine a person's identity.

## Status

🧪 Early experiment / learning project

---

Built as a self-directed computer-vision exercise with AI-assisted learning.