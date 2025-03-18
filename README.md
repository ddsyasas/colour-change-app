# Image Color Transformer

A Python script that intelligently transforms blue colors in an image to natural-looking brown shades while preserving the original intensity and opacity patterns.

## Features

- Converts blue colors to brown shades while maintaining natural appearance
- Preserves original intensity patterns (dark blue → dark brown, light blue → light brown)
- Maintains opacity and brightness of the original image
- Processes images pixel by pixel for precise color transformation

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/image-color-transformer.git
cd image-color-transformer
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your input image in a known location
2. Update the `image_path` variable in `color_change.py` with your image path
3. Run the script:
```bash
python color_change.py
```

The transformed image will be saved as 'output.jpg' in the specified output directory.

## How it Works

The script uses the HSV (Hue, Saturation, Value) color space to perform the color transformation:

1. Converts the image from BGR to HSV color space
2. Detects blue pixels using HSV color ranges
3. Transforms detected blue pixels to brown while preserving:
   - Original brightness (Value)
   - Relative intensity patterns
   - Natural color transitions
4. Converts the image back to BGR and saves the result

## License

MIT License - feel free to use this code for any purpose.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements! 