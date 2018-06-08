from Tester import Tester
from Spannerpi import Spannerpi
from Ifttt import Ifttt
import time
import json

BINARY_FROM = "SPANNER"
DEVICE_ID = "340040000f51353532343635"
ACCESS_TOKEN = "9e4c2afdbe47d87956ac7795e7287aa8c85e697b"

tester = Tester('340040000f51353532343635')
spannerpi = Spannerpi()
ifttt = Ifttt()

# D5 -> green led
# D1 -> blue led
# D3 -> button

# Basic Functionality
def B1_validate_button_press():
    # button pres    
    tester.digitalWrite("OUTPUT", "D3", "LOW")
    tester.setPinMode("D1", "INPUT")

    # check blue led state
    result = tester.digitalRead("D1")
    if (tester.assert_spanner(result) == 0):
        return 0
    else:
        return 1

# Network Tests
def N1_validate_wifi_connect():
    result = spannerpi.connect()
    print (result)

    time.sleep(4)    
    
    # check green led state
    tester.setPinMode("D5", "INPUT")
    value = tester.digitalRead("D5")
    if (tester.assert_spanner(value) == 0):
        return 0
    else:
        return 1

# Network Tests
def N3_validate_wifi_reconnect():
    result = spannerpi.disconnect()
    time.sleep(2)    
    result = spannerpi.connect() 
    time.sleep(4)    
    # check green led state
    value = tester.digitalRead("D5")
    if (tester.assert_spanner(value) == 0):
        return 0
    else:
        return 1

# Network Tests
def N2_validate_wifi_disconnect():
    result = spannerpi.disconnect()
    time.sleep(4)    
    # check green led blinking state
    for i in range(0, 10):
        value = tester.digitalRead("D5")
        time.sleep(0.2)
        if tester.assert_spanner(value) == 1:
            return 0     
        else:
            return 1

# Cloud Functionality
def C1_validate_ifttt_buttonOn():
    ifttt.buttonOn()
    time.sleep(2) 
    # check blue led state
    value = tester.digitalRead("D1")
    if (tester.assert_spanner(value) == 0):
        return 0
    else:
        return 1


if __name__ == "__main__":
    EXEC_TEST_CASE(B1_validate_button_press())
    time.sleep(2)
    EXEC_TEST_CASE(C2_validate_ifttt_buttonOff())
    EXEC_TEST_CASE(C1_validate_ifttt_buttonOn())
    EXEC_TEST_CASE(N1_validate_wifi_connect())
    time.sleep(2)
    EXEC_TEST_CASE(N2_validate_wifi_disconnect())
    time.sleep(2)
    EXEC_TEST_CASE(N3_validate_wifi_reconnect())

