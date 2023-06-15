import cv2
import numpy as np

def reinhard_color_transfer(input_img, target_img):
    # Convert images to 8-bit unsigned integer
    input_img = cv2.convertScaleAbs(input_img)
    target_img = cv2.convertScaleAbs(target_img)

    # Convert images to Lab color space
    input_lab = cv2.cvtColor(input_img, cv2.COLOR_BGR2Lab)
    target_lab = cv2.cvtColor(target_img, cv2.COLOR_BGR2Lab)

    # Split Lab images into channels
    input_l, input_a, input_b = cv2.split(input_lab)
    target_l, target_a, target_b = cv2.split(target_lab)

    # Perform color transfer on each channel
    transfer_l = apply_color_transfer(input_l, target_l)
    transfer_a = apply_color_transfer(input_a, target_a)
    transfer_b = apply_color_transfer(input_b, target_b)

    # Merge channels back into Lab image
    transfer_lab = cv2.merge([transfer_l, transfer_a, transfer_b])

    # Convert Lab image back to BGR color space
    transfer_bgr = cv2.cvtColor(transfer_lab, cv2.COLOR_Lab2BGR)

    # Convert image to RGB format for display
    transfer_rgb = cv2.cvtColor(transfer_bgr, cv2.COLOR_BGR2RGB)

    return transfer_bgr

def apply_color_transfer(input_channel, target_channel):
    # Compute mean and standard deviation of input and target channels
    input_mean, input_std = cv2.meanStdDev(input_channel)
    target_mean, target_std = cv2.meanStdDev(target_channel)

    # Normalize input channel
    normalized_channel = (input_channel - input_mean) / input_std

    # Scale normalized channel with target standard deviation and add target mean
    transferred_channel = (normalized_channel * target_std) + target_mean

    # Clip channel values to the valid range
    transferred_channel = np.clip(transferred_channel, 0, 255)

    return transferred_channel.astype(np.uint8)

# Load input and target images
input_img = cv2.imread("FigSource.png").astype(np.float32)
target_img = cv2.imread("FigTarget.png").astype(np.float32)

# Apply Reinhardschen Farbtransfer
output_img = reinhard_color_transfer(input_img, target_img)

# Display images
cv2.imshow("Input", input_img.astype(np.uint8))
cv2.imshow("Target", target_img.astype(np.uint8))
cv2.imshow("Output", output_img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
