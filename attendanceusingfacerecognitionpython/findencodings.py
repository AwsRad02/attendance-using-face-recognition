import cv2
import os
import face_recognition
import numpy






class findEncodingsImage:
    def __init__(self):
        #self.path1=path1

        self.path = 'ImagesAttendance'
        self.images = []
        self.classNames = []

        self.myList = os.listdir(self.path)


        self.readimgs()

    def readimgs(self):
        for cl in self.myList:
            curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
            print(self.classNames)



    def find_encodings(self,images):
        encodeList = []
        encodeddata=numpy.array([0.0])
        for img in images:

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)

        return encodeList

    def get_encoded(self):
        encodeded=self.find_encodings(self.images)
        return encodeded

    def get_classNames(self):
        return self.classNames






