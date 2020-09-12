from classes import *
import json
import paho.mqtt.client as mqtt

entities = {}

with open("config.json", "r") as json_data:
    config = json.loads(json_data.read(), strict=False)

house = HousePlan(config["HouseData"]["PlanIMG"])
#print(house.path)
#print(config)

for entity in config["IoTEntities"]:
    e = IoTEntity(entity, config["IoTEntities"][entity]["type"], 
                    config["IoTEntities"][entity]["xpos"], config["IoTEntities"][entity]["ypos"])
    entities[entity] = e
#
#for e in entities:
#    print(entities[e].name)

def handle_message(payload):
    #print(str(payload))
    payload = str(payload)
    payload = payload.replace("b'", "")
    payload = payload.replace("\\n'", "")
    entityname = payload.split(":")[0]
    entitymessage = payload.split(":")[1]
    #print(entityname)
    #print(entitymessage)
    if entityname in entities:
        entities[entityname].handle(entitymessage)
        


def on_connect(client, userdata, flags, rc):
    print("error = "+str(rc))
    client.subscribe(config["BrokerData"]["topic"])

def on_message(client, userdata, msg):
    print("msg!")
    print(msg.payload)
    handle_message(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(config["BrokerData"]["Host"], config["BrokerData"]["Port"], config["BrokerData"]["timeout"])
client.loop_forever()

