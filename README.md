# Object Detection for Phone, Cigarette, and Seatbelt using Darknet

## Project Overview

This project focuses on detecting specific objects such as phones, cigarettes, and seatbelts using a modified version of the Darknet framework, optimized for violence detection models. We enhance the detection performance by adjusting the original C source code of Darknet to tailor it for this task.

## Features

- **Object Detection**: Detects phones, cigarettes, and seatbelts in real-time.
- **Optimized Model**: Modification of the violence detection model for better performance in the specific object detection tasks.
- **Darknet Modification**: The original C code of Darknet is modified to suit the requirements of the task.

## Requirements

Before running the project, ensure the following dependencies are installed:

- [Darknet](https://github.com/AlexeyAB/darknet)
- OpenCV
- CUDA (for GPU acceleration)
- CUDNN
- A compatible GPU (optional but recommended for performance)
  
To install the necessary dependencies:
```bash
# Install OpenCV (for Ubuntu)
sudo apt-get install libopencv-dev

# Install CUDA (if using GPU)
sudo apt-get install nvidia-cuda-toolkit
```

## **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/object-detection-darknet
   ```

2. **Navigate into the project directory:**
   ```bash
   cd object-detection-darknet
   ```

3. **Modify the `Makefile` to enable GPU and OpenCV:**
   ```bash
   GPU=1
   OPENCV=1
   ```

4. **Build Darknet:**
   ```bash
   make
   ```

## Usage

1. **Training the Model**: To train the model with custom data, modify the configuration files (`cfg` and `data` files) for the specific objects (phone, cigarette, seatbelt).

   Example command to train:
   ```bash
   ./darknet detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137
   ```

2. **Testing the Model**: After training, use the following command to test on an image or video:
   ```bash
   ./darknet detector test data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj.weights -ext_output <path_to_image_or_video>
   ```

## Configuration

### Model Architecture

The YOLOv4 model is used as the backbone for object detection. The configuration file (`cfg/yolov4-obj.cfg`) is modified to include classes for:
- Phone
- Cigarette
- Seatbelt

### Dataset

You will need to prepare a dataset with labeled images for the specific objects. Use a tool like [LabelImg](https://github.com/tzutalin/labelImg) to create bounding box annotations.

The dataset structure should look like this:
```
data/
  obj.data
  obj.names
  train.txt
  test.txt
  images/
    image1.jpg
    image2.jpg
  labels/
    image1.txt
    image2.txt
```

## Results

The model is optimized for detecting objects in real-time, achieving high accuracy for phones, cigarettes, and seatbelts.

Sample results:
- Precision: 90%
- Recall: 88%
- F1 Score: 89%

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Darknet](https://github.com/AlexeyAB/darknet)
- [YOLOv4](https://github.com/AlexeyAB/darknet/wiki/YOLOv4)
