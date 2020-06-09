import cv2
class facecheck:
    def facevalidate(image):
            try:
                face_cascade = cv2.CascadeClassifier('frontface.xml')
                img = cv2.imread(image)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                if len(faces)!=0:
                    return True
                else:
                    return False
                    
            except:
                return False
               