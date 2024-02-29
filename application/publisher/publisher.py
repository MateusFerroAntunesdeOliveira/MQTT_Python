import paho.mqtt.client as mqtt

topic = "topics/message"
payload = "Publisher Python File Sending Message"

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "publisher")

mqtt_client.connect(host = "localhost", port = 1883)
mqtt_client.publish(topic = topic, payload = payload)
print(f"\nMessage published to topic '{topic}' with payload: {payload}\n")
