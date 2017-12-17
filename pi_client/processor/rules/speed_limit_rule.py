import threading
import time
from gps_sensor import GpsSensor

gpsSensor = GpsSensor()


class SpeedLimitRule(threading.Thread):
    currentSpeedLimit = 50
    highSpeedDurations = []

    def check_speed_limit(self):
        while (True):
            speed = gpsSensor.getCurrentSpeed()

            if (speed > self.currentSpeedLimit):
                startTime = self.currentTimeStamp()
                while (gpsSensor.getCurrentSpeed() > self.currentSpeedLimit):
                    time.sleep(1)
                endTime = self.currentTimeStamp()
                self.highSpeedDurations.append((startTime, endTime))

            time.sleep(10)

    def notifyChange(self, newSpeedLimit):
        self.currentSpeedLimit = newSpeedLimit

    def currentTimeStamp(self):
        return 20171213
