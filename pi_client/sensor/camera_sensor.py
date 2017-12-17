from picamera import PiCamera
import cv2
import picamera.array
import threading
import time

camera = PiCamera()
stream = picamera.array.PiRGBArray(camera)
camera.resolution = (320, 240)
speedCascade = cv2.CascadeClassifier('/home/pi/Projects/PiClient/pi_client/sensor/haarcascade_speed.xml')


class CameraInput(threading.Thread):
    cameraObserversList = []
    executeFlag = True

    def capture_image(self):
        camera.capture(stream, 'bgr', use_video_port=True)
        image = stream.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        stream.seek(0)
        stream.truncate()
        return gray

    # return true if speed limit is there in the image
    def detect_speed_limit_50(self, image):
        speedLimit = speedCascade.detectMultiScale(image, 1.3, 5)
        return len(speedLimit) != 0

    def detect_slow_speed_sign(self, image):
        return False

    def detect_pedestrian_crossing(self, image):
        return False

    def run(self):
        while (self.executeFlag):

            image = self.capture_image()
            detectSignFlag = False
            if self.detect_speed_limit_50(image):
                detectSignFlag = True
                speed = 50
                for observer in self.cameraObserversList:
                    observer.notify_change(speed)
                print "Detected a speed limit"

            if self.detect_slow_speed_sign(image):
                detectSignFlag = True

            if not detectSignFlag:
                print "CameraSensor:No Sign was detected for this frame"
                # randomSpeed = random.randint(1,100)
                # print "CameraSensor:No Sign was detected for this frame: "+str(randomSpeed)
                # for observer in self.cameraObserversList:
                #     observer.notifyChange(randomSpeed)

            time.sleep(5)


