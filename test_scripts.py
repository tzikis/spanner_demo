from SpannerTestboard import SpannerTestboard
import time
import json
import requests
import pytest


TESTBOARD_NAME = "Testboard1"
IFTTT_ACCESS_TOKEN = "54c8df8cb04da38a34e26ec6da046abf92182de4"

testboard = SpannerTestboard(TESTBOARD_NAME)
# D7 -> Relay PIN
RELAY_PIN = "D7"

def set_request(endpoint):
    headers = {"Content-Type": "application/json"}
    r = requests.post(endpoint, data = '', headers=headers)
    return r.text

def send_command(command):
    endpoint = 'https://maker.ifttt.com/trigger/'+command+'/with/key/'+ IFTTT_ACCESS_TOKEN
    return set_request(endpoint)

# Cloud Functionality
def test_validate_network_cmd_on():
    send_command("turn_on")
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    assert value !=0

# Cloud Functionality
def test_validate_network_cmd_off():
    send_command("turn_off")
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    assert value == 0
