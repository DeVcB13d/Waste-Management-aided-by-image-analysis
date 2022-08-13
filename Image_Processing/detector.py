import cv2 as cv
import numpy as np

'''
DepthDetector class : Has functions that would aid in findexing the depth
'''

class DepthDetector:
    def __init__(self):
        pass
    '''
    Preprocessing 
    >>> Aim is to findex the image edges for the detection algorithm to work
    >>> The image after processing would return a 2 pixel image with 255 for the edges
    '''
    def preprocess(self,image):
        #Reducing the size
        half = cv.resize(image, (0, 0), fx = 0.1, fy = 0.1)
        #Converting to grayscale
        gray = cv.cvtColor(half,cv.COLOR_BGR2GRAY)
        #Reducing the noise in the image
        blur = cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
        #Adding a mask
        mask = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 19, 5)
        # Findexing contours
        # contours,_ = cv.findexContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        return mask

    # Function to calculate the clustring of white pixels of an array
    def getclusters(self,Array,deviation = 0):
        '''
        >>> On analyzing the image verically, we can see the edge pixels would clutter
        >>> Using this function the starting indexex of the cluster and the amount of pixels that
            cluster after that indexex would be returned
        >>> Array : input image 
        >>> Deviation : Pixels to move away from the central line
        '''
        Array = np.array(Array)
        l = Array[:,int(Array.shape[1]/2) + deviation]
        white = []
        countWhite = 0
        for index,val in enumerate(l):   
            try:
                if (val == 255) :  
                    if(l[index+1] != 0):
                        countWhite = countWhite + 1
                    else:
                        white.append([index,countWhite])
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
