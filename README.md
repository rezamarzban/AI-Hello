# AI-Hello
Simple code to reading a handwritten digit number from any image by using Python AI libraries and neural network.

# Requirements

-System with strong CPU and high RAM hardwares

-Python3

-tensorflow library

-OpenCV library

-Numpy library

-pillow library

# Quick run
Run below commands in Colab
```
!git clone https://github.com/marzban2030/AI-Hello
%cd AI-Hello
!python neurons-model.py
```

Then run
```
!echo "Five.png" | python predict.py
```

For local running, Firstly run below command to building neural network with 99% accuracy for this model ONCE TIME:

"python3 neurones-model.py"

Then EVERYTIME that you want to read a digit from any existing image in the project directory run below command and input image file name with its extension when ask:

"python3 predict.py"

Or:

"python3 predict-PIL.py"

The "predict.py" and "predict-PIL.py" do same work, But the first one use OpenCV library to processing images and the second one use pillow library to processing images.

Also Linux executable binary files has been built by pyinstaller for arm64 devices and are available in Releases section, After download simply run:

"./neurons-model"

"./predict-PIL"

In this case you do not need to installing anything such as Python compiler and its modules especially heavy AI "tensorflow" module.

Before downloading and running above command, Do these:

1- Check if your device disk and RAM size will be high as necessary, Otherwise program will be encouraged an error and closed.

2- Update system certificates by running "sudo apt-get install ca-certificates" command if needed.

3- Download "mnist.npz" dataset file from Google to working directory if you want to load mnist datasets locally.

4- Run "chmod -c 755 ..." to changing access permission of files if needed.
