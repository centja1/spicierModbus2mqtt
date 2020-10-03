import argparse
import paho.mqtt.client as mqtt
import time

parser = argparse.ArgumentParser(description='Configure PZEM DC Meter')
parser.add_argument('--highvoltage', default='1500', help='High Voltage Threshold')
parser.add_argument('--lowvoltage', default='1150', help='Low Voltage Threshold')
parser.add_argument('--address', default='1', help='Modbus SlaveID')
parser.add_argument('--shunt', default='0', help='0 = 100A; 1 = 50A; 2 = 200A; 3 = 300A')
args=parser.parse_args()

def connecthandler(mqc,userdata,flags,rc):
    if rc == 0:
        print("MQTT Broker connected succesfully")
        mqc.publish("DEV/PZEM/CONFIG/set/HighVoltageThreshold", args.highvoltage)
        print("Published HighVoltageThreshold = " + args.highvoltage)
        time.sleep(1)
        #mqc.publish("DEV/PZEM/CONFIG/set/LowVoltageThreshold", args.lowvoltage)
        #print("Published LowVoltageThreshold = " + args.lowvoltage)
        #time.sleep(1)
        #mqc.publish("DEV/PZEM/CONFIG/set/Address", args.address)
        #print("Published Address = " + args.address)
        #time.sleep(1)
        #mqc.publish("DEV/PZEM/CONFIG/set/CurrentShunt", args.shunt)
        #print("Published CurrentShunt = " + args.shunt)
        #time.sleep(1)
    elif rc == 1:
        print("MQTT Connection refused – incorrect protocol version")
    elif rc == 2:
        print("MQTT Connection refused – invalid client identifier")
    elif rc == 3:
        print("MQTT Connection refused – server unavailable")
    elif rc == 4:
        print("MQTT Connection refused – bad username or password")
    elif rc == 5:
        print("MQTT Connection refused – not authorised")

mqtt_client = mqtt.Client(client_id="pzem_config")
mqtt_client.on_connect=connecthandler
mqtt_client.connect("mqtt.centanniventures.com", 1883, 60)
mqtt_client.loop_start()
time.sleep(5)

mqtt_client.disconnect()
