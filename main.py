import argparse

from object_sight.detect import detect_image


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Detect objects in an image and save an annotated result."
    )
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument(
        "--output",
        default="outputs/annotated.jpg",
        help="Where to save the annotated image",
    )
    args = parser.parse_args()

    output_path = detect_image(args.image, args.output)
    print(f"Annotated image saved to: {output_path}")


if __name__ == "__main__":
    main()
