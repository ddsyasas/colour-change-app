import cv2
import numpy as np
# import os

# Load image
image_path = "/Users/ddsyasas/Downloads/Pest control 01.png"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found. Check the file path!")
    exit()

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define blue color range in HSV
lower_blue = np.array([90, 30, 30])  # Lower bound of blue shades (more inclusive)
upper_blue = np.array([140, 255, 255])  # Upper bound of blue shades

# Create mask for blue color
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Create a copy of the original image for modification
result = image.copy()

# Get the pixels where blue is detected
blue_pixels = cv2.bitwise_and(hsv, hsv, mask=blue_mask)

# Convert target brown color from hex (#653900) to HSV
# Brown in HSV has a hue around 20-30
target_brown_hsv = np.array([20, 150, 101])  # HSV values for brown

# For each pixel in the blue mask
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if blue_mask[i, j] > 0:
            # Get the original pixel's HSV values
            original_hsv = hsv[i, j]
            
            # Keep the original value (brightness), but change hue and adjust saturation
            new_hsv = np.array([
                target_brown_hsv[0],  # New hue (brown)
                min(original_hsv[1] * 1.2, 255),  # Adjust saturation while keeping proportion
                original_hsv[2]  # Keep original brightness
            ])
            
            hsv[i, j] = new_hsv

# Convert back to BGR
result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Save output image
output_path = "/Users/ddsyasas/Downloads/output.jpg"
success = cv2.imwrite(output_path, result)

if success:
    print(f"✅ Image saved successfully at {output_path}")
else:
    print("❌ Failed to save image. Check file permissions.") 