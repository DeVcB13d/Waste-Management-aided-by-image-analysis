import os
from detector import *
import cv2 as cv
import numpy as np
import time
import random


detector = DepthDetector()

empty = cv.imread("Image_Processing\Test\empty.jpg")
p_empty = detector.preprocess(empty)
# cv.imshow("empty",p_empty)

images = os.listdir(r"C:\Users\USER\Waste-Management-aided-by-image-analysis\Image_Processing\Test")
DIR = r"C:\Users\USER\Waste-Management-aided-by-image-analysis\Image_Processing\Test"
data = []
for i in images:
    img_path = os.path.join(DIR,i)
    img = cv.imread(img_path)
    p_img = detector.preprocess(img)
    
    # print(p_img)
    perc = detector.get_depth_perc(p_empty,p_img)
    perc2 = detector.get_depth_perc_approx(p_empty,p_img,20)
    data.append(round(perc2,2))
    print(i," ",perc,"%")
    print(i," ",perc2,"%")
    # cv.imshow("process",p_img)
    # cv.waitKey(0)

import webbrowser
import time

final_value = perc2

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>helloworld</title>
    <link rel="shortcut icon" type="image/jpg" href="bin-logo.png"/>
</head>
<body>
    <h1>Find the nearest place for waste disposal</h1>
    <div id="main">
      
    <div id="map">
          <img src="map.png" alt="Google Regional Map">
        <h3>Cochin University of Science and Technology</h3>
      
    </div>

   <div id="list">
        <h2>Waste Bins</h2>
        <table class="table">
          <tr>
            <td>Sarovar Mens Hostel</td>
            <td>{data[1]}%</td>
          </tr>
          <tr>
            <td>Department of Biotechnology</td>
            <td>{data[2]}%</td>
          </tr>
          <tr>
            <td>Cafe CUSAT</td>
            <td>{data[3]}%</td>
          </tr>
          <tr>
            <td>Advanced Centre for Atmospheric Radar</td>
            <td>{data[4]}%</td>
          </tr>
          <tr>
            <td>CUSAT Restaurent</td>
            <td>{data[5]}%</td>
          </tr>
          <tr>
            <td>Kochi Chaatwala</td>
            <td>{data[6]}%</td>
          </tr>
        </table><br>
      
      </div>
    </div>
       
  

  <footer>
    <h4>FOOTER</h4>
    <p>Powered by <a href="https://github.com/DeVcB13d/Waste-Management-aided-by-image-analysis" target="_blank">helloworld</a></p>
  </footer>
</body>
</html>'''

with open("index.html","w") as html_file:
    html_file.write(html_content)
    print("SUCCESSFUL")
