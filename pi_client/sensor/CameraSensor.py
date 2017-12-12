from picamera import PiCamera
import cv2
import picamera.array

camera = PiCamera()
stream = picamera.array.PiRGBArray(camera)
speedCascade = cv2.CascadeClassifier('haarcascade_speed.xml')

class CameraInput:

    cameraObserversList = []

    def __init__(self):
        pass

    def queryForInput(self):
        timestampAddition = str(int(time.time() * 1000))
        filePath = DATA_PATH + FILE_BASE_NAME + timestampAddition + EXTENSION_TYPE
        camera.capture(filePath)
        return filePath

    def captureImage(self):
        image = camera.capture(stream, 'bgr' , use_video_port = True).array
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray

    #return true if speed limit is there in the image
    def detectSpeedLimit50(self,image):
        speedLimit = speedCascade.detectMultiScale(image,1.3,5)
        return len(speedLimit) != 0

    def detectSlowSpeedSign(self,image):
        pass

    def detectPedestrianCrossSign(self,image):
        pass

    def run(self):
        while(True):
            image = captureImage()
            if detectSpeedLimit50(image):
                for observer in cameraObserversList:
                    observer.notifyChange(speed)

            if detectSlowSpeedSign(image):
                pass
