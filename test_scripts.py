from Testboard import Testboard
from Ifttt import Ifttt
import time
import json


TESTBOARD_ID = "340040000f51353532343635"
IFTTT_ACCESS_TOKEN = "54c8df8cb04da38a34e26ec6da046abf92182de4"

testboard = Testboard(TESTBOARD_ID)
ifttt = Ifttt(IFTTT_ACCESS_TOKEN)

# D7 -> Relay PIN
RELAY_PIN = "D7"

# Cloud Functionality
def validate_network_cmd_on():
    ifttt.buttonOn()

    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    if (testboard.assert_spanner(value) == 1):
        return 0 # Success
    else:
        return 1 # Failure

# Cloud Functionality
def validate_network_cmd_off():
    ifttt.buttonOff()

    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    if (testboard.assert_spanner(value) == 0):
        return 0 # Success
    else:
        return 1 # Failure

if __name__ == "__main__":

    run_test(validate_network_cmd_on())

    time.sleep(2)

    run_test(validate_network_cmd_off())
