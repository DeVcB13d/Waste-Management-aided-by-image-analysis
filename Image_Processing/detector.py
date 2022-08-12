import cv2 as cv
import numpy as np
# Loading the image

# empty_cup = cv.imread('Image_Processing\Trainset\canEmp.jpg')
# filled_cup = cv.imread('Image_Processing\Trainset\canFill.jpg')


class DepthDetector:
    def __init__(self):
        pass

    def preprocess(self,image):
        #Reducing the size
        half = cv.resize(image, (0, 0), fx = 0.1, fy = 0.1)
        #Converting to grayscale
        gray = cv.cvtColor(half,cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
        #Adding a mask
        mask = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 19, 5)
        #Finding contours
        contours,_ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        return mask

    # Function to calculate the clustring of white pixels of an array
    def getclusters(self,Array,deviation = 0):
        Array = np.array(Array)
        l = Array[:,int(Array.shape[1]/2) + deviation]
        white = []
        countWhite = 0
        for ind,val in enumerate(l):   
            try:
                if (val == 255) :  
                    if(l[ind+1] != 0):
                        countWhite = countWhite + 1
                    else:
                        white.append([ind,countWhite])
                        countWhite = 0
            except:
                pass
        return(white)

    def get_depth_perc(self,empty,filled):
        w1 = self.getclusters(empty)
        w2 = self.getclusters(filled)
        print(w1)
        print(w2)
        len1 = (w1[1][0]) - (w1[0][0] + w1[0][1]) 
        len2 = (w2[1][0]) - (w2[0][0] + w2[0][1])  
        return(100 - ((len2/len1)*100))
    
    def get_depth_perc_approx(self,empty,filled,size):
        vals = []
        for i in range(-1*size,1*size):
            w1 = self.getclusters(empty,i)
            w2 = self.getclusters(filled,i)
            #print(w1)
            #print(w2)
            len1 = (w1[1][0]) - (w1[0][0] + w1[0][1]) 
            len2 = (w2[1][0]) - (w2[0][0] + w2[0][1])  
            vals.append((100 - ((len2/len1)*100)))
        return (sum(vals)/len(vals))
