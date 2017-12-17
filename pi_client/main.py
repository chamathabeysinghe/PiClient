import __init__
import camera_sensor
import speed_limit_rule
import time
import json

camera = camera_sensor.CameraInput()
speedLimitRule = speed_limit_rule.SpeedLimitRule()


camera.cameraObserversList.append(speedLimitRule)

camera.start()
speedLimitRule.start()

time.sleep(15)

camera.executeFlag = False
speedLimitRule.executeFlag = False

camera.join()
speedLimitRule.join()


speedReport = speedLimitRule.get_report()

reports = {'speedLimitReport': speedReport}

transferReport = json.dumps(reports)

print transferReport


