# Learning Path

Object Sight should grow in small experiments. Each stage introduces one new idea without changing everything at once.

## Stage 1 — Single Image Detection

Goal: prove the basic pipeline works.

- Load one local image.
- Run the pretrained detector.
- Inspect detected classes and confidence scores.
- Draw bounding boxes and labels.
- Save the annotated image.

Concepts: inference, classes, confidence, bounding boxes.

## Stage 2 — Detection Filtering

Goal: learn how model output becomes application logic.

- Set a minimum confidence threshold.
- Show only selected classes.
- Count detected objects.
- Compare results on several images.

Concepts: thresholds, false positives, application-level filtering.

## Stage 3 — Prerecorded Video

Goal: understand that video is a sequence of frames.

- Open a local video with OpenCV.
- Run detection frame by frame.
- Draw annotations.
- Write an annotated output video.

Concepts: frames, frame rate, processing loops, inference cost.

## Stage 4 — Live Camera

Goal: move from offline files to real-time input.

- Read from a webcam or supported camera.
- Detect objects continuously.
- Display the annotated feed.
- Measure approximate FPS.

Concepts: latency, real-time inference, performance tradeoffs.

## Stage 5 — Small Experiments

Only after the core pipeline is understood, try focused extensions such as:

- Object counting
- Region-of-interest detection
- Tracking an object across frames
- Comparing model sizes and speed
- Logging anonymous detection categories and timestamps

## Later, Not Now

Possible future subjects include custom datasets, model training, edge deployment, APIs, and mobile inference. They should remain separate milestones rather than being folded into the first version.

The learning rule is: **make one concept visible, understand it, then add the next one.**