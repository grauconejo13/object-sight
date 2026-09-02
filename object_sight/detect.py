from pathlib import Path

import cv2
from ultralytics import YOLO


def detect_image(
    input_path: str | Path,
    output_path: str | Path = "outputs/annotated.jpg",
    model_name: str = "yolov8n.pt",
) -> Path:
    """Detect objects in one image and save an annotated copy."""
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    model = YOLO(model_name)
    results = model(str(input_path))

    annotated = results[0].plot()
    cv2.imwrite(str(output_path), annotated)

    return output_path
