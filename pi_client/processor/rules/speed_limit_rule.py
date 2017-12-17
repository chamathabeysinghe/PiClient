import threading
import time
from gps_sensor import GpsSensor

gpsSensor = GpsSensor()


class SpeedLimitRule(threading.Thread):
    currentSpeedLimit = 50
    highSpeedDurations = []
    executeFlag = True

    def run(self):
        while self.executeFlag:
            print "Checking speed  " + str(self.currentSpeedLimit)
            speed = gpsSensor.getCurrentSpeed()

            if speed > self.currentSpeedLimit:
                print "High Speed Detected"
                startTime = self.current_timestamp()
                while self.executeFlag and gpsSensor.getCurrentSpeed() > self.currentSpeedLimit:
                    time.sleep(1)
                    print "Done in while"
                print "record end time"
                endTime = self.current_timestamp()
                self.highSpeedDurations.append((startTime, endTime))
                print self.highSpeedDurations
            else:
                print "Not High Speed"
            time.sleep(1)

    def notify_change(self, newSpeedLimit):
        self.currentSpeedLimit = newSpeedLimit

    def current_timestamp(self):
        return 20171213

    def get_report(self):
        report = {'highSpeedDurations': self.highSpeedDurations}
        return report
