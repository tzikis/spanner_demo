from Tester import Tester
from Ifttt import Ifttt
import time
import json

DEVICE_ID = "340040000f51353532343635"
ACCESS_TOKEN = "54c8df8cb04da38a34e26ec6da046abf92182de4"
tester = Tester('340040000f51353532343635')

testboard = Tester(DEVICE_ID)
ifttt = Ifttt()

# D7 -> Relay PIN
RELAY_PIN = "D7"

# Cloud Functionality
def validate_network_cmd_on():
    ifttt.buttonOn()

    time.sleep(2)

    # check PIN state
    value = tester.digitalRead(RELAY_PIN)
    if (tester.assert_spanner(value) == 1):
        return 0
    else:
        return 1

# Cloud Functionality
def validate_network_cmd_offf():
    ifttt.buttonOff()

    time.sleep(2)

    # check PIN state
    value = tester.digitalRead(RELAY_PIN)
    if (tester.assert_spanner(value) == 0):
        return 0
    else:
        return 1

if __name__ == "__main__":

    EXEC_TEST_CASE(validate_network_cmd_on())

    time.sleep(2)

    EXEC_TEST_CASE(validate_network_cmd_off())
