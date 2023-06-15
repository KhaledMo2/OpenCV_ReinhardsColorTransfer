# OpenCV_ReinhardsColorTransfer
Ein OpenCV Projekt von Visual Computing Praktikum. Thema: Color Transfer und OpenCV Introduction  In this Praktikum Exercise, there are two separate Exercises
## 4.1 Installation of OpenCV

A detailed installation guide for C++ can be found in the Moodle platform.

For a good documentation, refer to the book "Learning OpenCV" by Gary Bradski and Adrian Kaehler, or visit the official documentation here: [OpenCV Documentation](https://docs.opencv.org/4.7.0/d1/dfb/intro.html).

An alternative (recommended) approach is to integrate OpenCV into a Python project, which is significantly easier. Follow these steps:

a) Install a Python IDE of your choice, such as PyCharm Community by JetBrains. You can get it for free as a student license from [here](https://www.jetbrains.com/pycharm/download/#section=windows).

b) Install the latest version of Python from [here](https://www.python.org/downloads/). Make sure to set the PATH variable correctly during the installation process.

c) Create a test Python project in the IDE. In PyCharm, you can use the terminal and execute the command `python --version` to check the installed Python version. If this doesn't work, it means your Python environment is not found.

d) Install additional packages: Python comes with a built-in package manager called PIP (Package Installer for Python). If you want to manage different projects with different Python versions, you can use the package manager Anaconda (not needed for this practical).

e) Install the latest version of OpenCV by running the command `pip install opencv-python`. More information can be found at [https://pypi.org/project/opencv-python/](https://pypi.org/project/opencv-python/).

f) Optional: To simplify image manipulation, you can install the math library Numpy. Use the command `pip install numpy` to install the library.

Copy the image "yoshi.png" to your project folder and test your installation using the following code:

## 4.2 Getting Started

In this section, we will explore basic image manipulation and display using OpenCV functions. Use familiar functionalities or refer to online resources such as the OpenCV documentation to:

- Load the attached "yoshi.png" image.
- Print the width, height, and number of color channels to the console.
- Change the image data format to float.
- Display the image until a key is pressed (both as uint8 and float).
- Draw a red square of 10x10 pixels in the center of the image.
- Replace every 5th row with black pixels.
- Save the image to disk.

## 4.3 Color Spaces

In this task, we will work with color space conversions.

1. In addition to Yoshi, load the corresponding mask "mask.png" into your program.
2. Convert the Yoshi image to the HSV color space.
3. For all white pixels in the mask image, modify the H-value in the Yoshi image.
4. Display the new image on the screen (note that `imshow()` can only handle BGR images correctly). The result should resemble the provided image.
5. Optional: Create a slider to manually adjust the H-value to any desired value and update the displayed image.

## 4.4 Reinhards Color Transfer

In this exercise, you will implement a variant of the Reinhard color transfer algorithm (source: "Color Transfer between images" by Reinhard, Ashikmin, Gooch, and Shirley, available in Moodle). The idea of color transfer is to adjust the

 general color scheme of an input image to match a specific target color scheme. An example is shown in Figure 1.

Follow these steps:

1. Load two images as "Input" and "Target" and convert them to floating-point values in the range of 0 to 1.
2. Convert both images to the Lab color space.
3. For each color channel (separately):
   - Subtract the mean value of the input from the input (the new mean value of the input will be 0).
   - Divide the input by its standard deviation (the new standard deviation will be 1).
   - Multiply the input by the standard deviation of the target.
   - Add the mean value of the target to the input.
4. Convert the input back to BGR.
5. Test the algorithm with other color spaces such as RGB and HSV, as well as different images. Which color spaces are suitable for the algorithm, and which are not? Which images produce good color transformations? Can you explain why?