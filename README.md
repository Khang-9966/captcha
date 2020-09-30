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
http://localhost:1232/getcaptcha?image=iVBORw0KGgoAAAANSUhEUgAAAIIAAAAkCAYAAABFRuIOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAT9SURBVHhe7Zo%2FSyRBEMXlDsGv4sV3cCaK2aWayoGcghiJ2WIsgigsonCpyCKyYCKCG6mwIoqBgYHiBQYGoh%2FBpK9qenqnurrmn9uz67AT%2FDjYrp1g%2B82rV%2BUNPf97VxUVlRAqAiohlJiJ4Zr68lUzsfYi1mSlEkJZOT8NBDA0fyef56QSQom4WtvqOAAi1XyUSgglwgjAlwtQKiGUgju1EOaBhYZ03j1dCuFJbc78UCM%2FvwtnFV0DOYAGQrHGE14c4WpnNhADRaqryIdxAaTbqSANT62h7QghYGxVNfH8cFX4TkUydx0RDA0f6N%2BxQLxlhMUx3SIMkztP1jk9o59XyNAJwYRDLgyfeaEYRxibdWqk9mHgtYNNFAyTQBH4dInCHGHzgtdEwdJgXGPxkNcOLpYTDG%2BpjfPo843xSAjoCp%2FQEUCdteTWEABZgdaM1NpuTWkmkVe1N7WpppcfhLOP05y3Lzt661%2BsM8RngPQmhOeLhpqkrjDTUFdOXdt2DmghrnOEwPN03S%2F1%2B8%2B2%2Bju3Ldf1i%2Baxmv4GQhg9Vi3p%2FINYb%2F34qfUb8s3ipxQCt33J7jO5BoKiAiGZZ9w39gMhcJzv9YjWMggARQAs1V%2FFmvy89E0EiDchOGHQsX3mBojoGvpZKJLo7FEdMRE0Gm%2Fwb0vd4PlJyzrjz%2FNK%2B1ItjUZCmJ66VLdSXW7skMiF8Nw4sITge8PorzU4th%2FuEALgUlEoIA7uCq5z4HPodzWOK9QfrXOxhnB0Qmvf1NkKq1m5VvfkWXHc1ncjEYSsN%2BXafLhCsH4DIoQi9goehZBg%2FWD1mzNhHkgLjHguhshH%2B%2BLm9oUa94LROdy6kOtr1YAaWyTJrI%2FuqiUMiVQMEBj32nJ9dlhrgMs2E0MAEUIRW0avQnAuObR%2BFAj2fG11fOdAt47aMeLGSd4ezq6FOtYmJOfogELI6ASaB50JTFA0oDg8ZAV7YtiyLtxkhCL%2B8oj4FQLfFQRTgbZ6erk8K3RsDoQktQXDTZ1cMCC%2F7a5ziIIBsJUkOgYHBKDf%2FAdwBiKEQAwepgd46%2BXxUbcNyyE841UI0vbQmQw6Y2EIOAV%2B3qwljJIBb4GN00uW3uSsYjkyQTMTuDPY7di%2FkxNABD5yAorAtAcUQSSIaLFUFJ4dIcue4MneN0DNVTguShMEhfd%2Ft7e704UYArF9JLUMDrYCujjikwPiZXoIW0GYB9zz4vAsBBYYxdAn7BzADWJ3CoS0ySE4h8%2BsGoALBl0jT0DEvQF%2F4%2BkuIQByQveBsX94FwINjHGhz2khSRtGC%2F7GU3vHiUHnAd4ebMHkbAv49ktvOw%2BMiOd1cy%2FxLwQTGJOsHlsBbQ8Z2oIhNgPQCYBPDvTic7YFzAN0InAun%2BJ53dxLChCCJtnqyXTBJopU%2BCWHl2%2FbvZsVzNlNPX6KcHGnA3ouLZf8rZx7S2FCSKPTHnDbKJzHw5dGeLGu3TvtAQWTd2%2FAQyJHCo2hK%2FhZO%2FeOvgnBTBi53CBEWiU7Y2K4NYxq9tURuEH2vYE9MsbhhEYEMkXZwmMfhdAN3Poluxf%2BnpCwXOIEtp9lJJRCIyDWfmJKKgRm%2FTHhz3GOrG3BXG5C%2BOP5QKopE6UVAg2NsTsB1h7Sdwfh%2FzoiFxxQ8h1BFsorBLD%2B9Lectoc8K%2BXBo8RC0CvntPDXaQ85dgeDSKmFkA0dLPOslAeRARBCRTrv6j%2FycxDvXH6c%2BQAAAABJRU5ErkJggg%3D%3D

image field is base64 image
