# Stack Decisions

Object Sight intentionally uses a small stack. The goal is to learn the computer-vision pipeline clearly before adding frameworks, services, or infrastructure that are not yet necessary.

## Python

**Role:** application and experiment logic.

Python is used because it has one of the strongest ecosystems for computer vision and machine learning. It lets this project connect image processing, model inference, file handling, and experimentation with relatively little boilerplate.

Why it fits this project:

- Excellent support for computer-vision and ML libraries.
- Fast to prototype and easy to read while learning.
- Works well with OpenCV and Ultralytics YOLO.
- Makes it easy to move later into notebooks, data analysis, model training, or APIs if the project grows.

Why not another language yet:

Object Sight is not currently trying to prove frontend, mobile, or systems-programming skills. Python keeps the focus on computer vision itself.

## OpenCV

**Role:** image and video I/O plus frame-level processing.

OpenCV handles the traditional computer-vision side of the pipeline. It can load images, read video files, access cameras, manipulate frames, draw overlays, resize images, and save results.

Why it fits this project:

- Mature and widely used computer-vision library.
- Supports images, video, and live camera streams.
- Provides the bridge between raw visual input and model inference.
- Useful even when the ML model changes later.

OpenCV is not the object detector here. It is the tool that helps us acquire, prepare, display, annotate, and save visual data.

## YOLO via Ultralytics

**Role:** object detection.

YOLO is used as the first pretrained detector so the project can focus on understanding inference before attempting model training.

Why it fits this project:

- Can detect many common object classes out of the box.
- Fast enough for future real-time experiments.
- Produces exactly the concepts this project wants to study: bounding boxes, class labels, and confidence scores.
- Ultralytics provides a relatively approachable Python API for loading and running pretrained YOLO models.

Why pretrained first:

Training a detector introduces datasets, annotation, augmentation, evaluation, GPU concerns, and model tuning. Those are valuable topics, but they would hide the fundamentals during the first exercise.

## How the Pieces Fit Together

```text
Image / Video / Camera
        |
        v
     OpenCV
(load/read frames)
        |
        v
      YOLO
(object inference)
        |
        v
boxes + labels + confidence
        |
        v
     OpenCV
(draw/save/display)
        |
        v
     Python
controls the workflow
```

## Why This Stack Is Deliberately Small

For the first milestone, Object Sight does not need:

- A database
- A web framework
- A frontend framework
- Cloud infrastructure
- User accounts
- Custom model training
- Docker or Kubernetes

Those technologies may be useful later, but adding them now would increase setup and debugging without improving the core learning goal.

## When the Stack Might Change

Future experiments could justify additional tools:

- **NumPy** for explicit array manipulation and numerical experiments.
- **PyTorch** when studying model internals or training custom models directly.
- **FastAPI** if object detection becomes an HTTP service.
- **Docker** when reproducible deployment becomes important.
- **ONNX / TensorRT / Core ML / TFLite** when experimenting with optimized or edge/mobile inference.
- **A database** only if the project begins storing detection events, metadata, or analytics.

The rule for this repository is simple: add technology when there is a real problem for it to solve.