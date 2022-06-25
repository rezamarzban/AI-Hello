# AI-Hello
Simple code to reading a handwritten digit number from any image by using Python AI libraries

First run below command to building neuronal network for this model ONCE TIME:

"python3 neurones-model.py"

Then EVERYTIME that you want to read a digit from any image run below command:

"python3 predict.py"

Also "neurons-model" Linux executable file for arm64 devices is available at Releases section, After download simply run:

"./neurons-model"

In this case you do not need to installing Python compiler and its modules especially heavy AI "tensorflow" module.

Before downloading and running above command, Do these:
1- Check if your device disk and RAM size will be high as necessary, Otherwise program will be encouraged an error and closed.
2- Update system certificates by running "sudo apt-get install ca-certificates" command.

Unfortunately, Because of some solutions single binary executable file is not available for "predict.py" currently. We will solve it at future!
