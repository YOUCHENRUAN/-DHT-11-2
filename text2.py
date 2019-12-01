#!usrbinpython3
import time
import sys
import http.client as http
import urllib
import json
import Adafruit_DHT
deviceId = DdzxEAhw
deviceKey = WRSRoEAx1U0wxgbD

def post_to_mcs(payload)
    headers = {Content-type applicationjson, deviceKey deviceKey}
    not_connected = 1
    while (not_connected)
        try
            conn = http.HTTPConnection(api.mediatek.com80)
            conn.connect()
            not_connected = 0
        except (http.HTTPException, socket.error) as ex
            print (Error %s % ex)
            time.sleep(10)
    conn.request(POST, mcsv2devices + deviceId + datapoints, json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime(%c))
    data = response.read()
    conn.close()

sensor_args = { '11' Adafruit_DHT.DHT11,
                '22' Adafruit_DHT.DHT22,
                '2302' Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else
    print('Usage sudo .Adafruit_DHT.py [11222302] GPIO pin number')
    print('Example sudo .Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)
while True
    h0, t0= Adafruit_DHT.read_retry(sensor, pin)
    if h0 is not None and t0 is not None
        print('Temp={00.1f}  Humidity={10.1f}%'.format(t0, h0))

        payload = {datapoints[{dataChnIdHumidity,values{valueh0}},
            {dataChnIdTemperature,values{valuet0}}]}
        post_to_mcs(payload)
        time.sleep(10)

else
    print('Failed to get reading. Try again!')
    sys.exit(1)