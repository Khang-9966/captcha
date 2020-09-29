### Before you get started

To run these scripts, you need the following installed:

1. Python 3
2. OpenCV 3 w/ Python extensions
 - I highly recommend these OpenCV installation guides: 
   https://www.pyimagesearch.com/opencv-tutorials-resources-guides/ 
3. The python libraries listed in requirements.txt
 - Try running "pip3 install -r requirements.txt"

### Step 1: Extract single letters from CAPTCHA images

Run:

python3 extract_single_letters_from_captchas.py

The results will be stored in the "extracted_letter_images" folder.


### Step 2: Train the neural network to recognize single letters

Run:

python3 train_model.py

This will write out "captcha_model.hdf5" and "model_labels.dat"


### Step 3: Use the model to solve CAPTCHAs!

Run: 

python3 solve_captchas_with_model.py

### Step 4: Build docker and Run!
cd buildocker
docker build -t captcha_api -f Dockerfile-captcha-api .

docker run --rm \
-p 1232:80 \
--name captcha-api \
captcha_api

API: 
http://172.50.1.81:1232/getcaptcha?image=iVBORw0KGgoAAAANSUhEUgAAAIIAAAAkCAYAAABFRuIOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAT9SURBVHhe7Zo/SyRBEMXlDsGv4sV3cCaK2aWayoGcghiJ2WIsgigsonCpyCKyYCKCG6mwIoqBgYHiBQYGoh/BpK9qenqnurrmn9uz67AT/DjYrp1g+82rV+UNPf97VxUVlRAqAiohlJiJ4Zr68lUzsfYi1mSlEkJZOT8NBDA0fyef56QSQom4WtvqOAAi1XyUSgglwgjAlwtQKiGUgju1EOaBhYZ03j1dCuFJbc78UCM/vwtnFV0DOYAGQrHGE14c4WpnNhADRaqryIdxAaTbqSANT62h7QghYGxVNfH8cFX4TkUydx0RDA0f6N+xQLxlhMUx3SIMkztP1jk9o59XyNAJwYRDLgyfeaEYRxibdWqk9mHgtYNNFAyTQBH4dInCHGHzgtdEwdJgXGPxkNcOLpYTDG+pjfPo843xSAjoCp/QEUCdteTWEABZgdaM1NpuTWkmkVe1N7WpppcfhLOP05y3Lzt661+sM8RngPQmhOeLhpqkrjDTUFdOXdt2DmghrnOEwPN03S/1+8+2+ju3Ldf1i+axmv4GQhg9Vi3p/INYb/34qfUb8s3ipxQCt33J7jO5BoKiAiGZZ9w39gMhcJzv9YjWMggARQAs1V/Fmvy89E0EiDchOGHQsX3mBojoGvpZKJLo7FEdMRE0Gm/wb0vd4PlJyzrjz/NK+1ItjUZCmJ66VLdSXW7skMiF8Nw4sITge8PorzU4th/uEALgUlEoIA7uCq5z4HPodzWOK9QfrXOxhnB0Qmvf1NkKq1m5VvfkWXHc1ncjEYSsN+XafLhCsH4DIoQi9goehZBg/WD1mzNhHkgLjHguhshH++Lm9oUa94LROdy6kOtr1YAaWyTJrI/uqiUMiVQMEBj32nJ9dlhrgMs2E0MAEUIRW0avQnAuObR+FAj2fG11fOdAt47aMeLGSd4ezq6FOtYmJOfogELI6ASaB50JTFA0oDg8ZAV7YtiyLtxkhCL+8oj4FQLfFQRTgbZ6erk8K3RsDoQktQXDTZ1cMCC/7a5ziIIBsJUkOgYHBKDf/AdwBiKEQAwepgd46+XxUbcNyyE841UI0vbQmQw6Y2EIOAV+3qwljJIBb4GN00uW3uSsYjkyQTMTuDPY7di/kxNABD5yAorAtAcUQSSIaLFUFJ4dIcue4MneN0DNVTguShMEhfd/t7e704UYArF9JLUMDrYCujjikwPiZXoIW0GYB9zz4vAsBBYYxdAn7BzADWJ3CoS0ySE4h8+sGoALBl0jT0DEvQF/4+kuIQByQveBsX94FwINjHGhz2khSRtGC/7GU3vHiUHnAd4ebMHkbAv49ktvOw+MiOd1cy/xLwQTGJOsHlsBbQ8Z2oIhNgPQCYBPDvTic7YFzAN0InAun+J53dxLChCCJtnqyXTBJopU+CWHl2/bvZsVzNlNPX6KcHGnA3ouLZf8rZx7S2FCSKPTHnDbKJzHw5dGeLGu3TvtAQWTd2/AQyJHCo2hK/hZO/eOvgnBTBi53CBEWiU7Y2K4NYxq9tURuEH2vYE9MsbhhEYEMkXZwmMfhdAN3Poluxf+npCwXOIEtp9lJJRCIyDWfmJKKgRm/THhz3GOrG3BXG5C+OP5QKopE6UVAg2NsTsB1h7Sdwfh/zoiFxxQ8h1BFsorBLD+9Lectoc8K+XBo8RC0CvntPDXaQ85dgeDSKmFkA0dLPOslAeRARBCRTrv6j/ycxDvXH6c+QAAAABJRU5ErkJggg== 

image field is base64 image
