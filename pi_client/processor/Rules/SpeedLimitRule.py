gpsSensor = GpsSensor()

class SpeedLimitRule(Thread):
    currentSpeedLimit = 50;
    highSpeedDurations = []
    def __init__(self):
        pass

    def checkSpeedLimit(self):
        while(True):
            speed = gpsSensor.getCurrentSpeed()

            if (speed > currentSpeedLimit):
                startTime = currentTimeStamp()
                while(gpsSensor.getCurrentSpeed() > currentSpeedLimit):
                    Thread.sleep(1ms)
                endTime = currentTimeStamp()
                highSpeedDurations.append((startTime,endTime))

            Thread.sleep(10ms)

    def notifyChange(self,newSpeedLimit):
        self.currentSpeedLimit = newSpeedLimit
