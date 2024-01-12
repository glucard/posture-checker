import cv2
import threading
import numpy as np

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.lock = threading.Lock()
        self.t = threading.Thread(target=self._reader)
        self.t.daemon = True
        self.t.start()
        
    def unqueue(self):
        """ unqueue older frames from cv2 videocapture buffer """
        while True:
            with self.lock:
                ret = self.cap.grab()
            if not ret:
                break
        self.cap.release() ##

    def take_photo(self):
        with self.lock:
            _, frame = self.cap.retrieve()
        return frame
    
    def take_photo_eco():
        cap = cv2.VideoCapture(0)
        _, frame = cap.retrieve()
        cap.release() 
        return frame