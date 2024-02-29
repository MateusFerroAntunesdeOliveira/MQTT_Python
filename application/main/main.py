import time

from application.configs.broker_configs import mqtt_broker_configs
from .mqtt_client_connection import MqttClientConnection

def start():
    mqtt_client_connection = MqttClientConnection(
        broker_ip = mqtt_broker_configs["HOST"],
        broker_port = mqtt_broker_configs["PORT"],
        client_name = mqtt_broker_configs["CLIENT_NAME"],
        keep_alive = mqtt_broker_configs["KEEP_ALIVE"]
    )
    mqtt_client_connection.start_connection()
    
    # Keep the firmware running
    # Calls callback functions from interruptions
    while True:
        time.sleep(0.01)
