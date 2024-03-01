## MQTT / Python Project

<p align="justify">
    Projeto de um MQTT Broker, com subscriber e publisher, utilizando a linguagem de programação Python.
</p>

<p align="justify">
    O projeto consiste em um broker MQTT, com um subscriber e um publisher, que se comunicam entre si. O subscriber se inscreve em um tópico e o publisher publica mensagens nesse tópico. O broker é responsável por intermediar a comunicação entre os dois.
</p>

<p align="justify">
    Desenvolvido para fins de estudo e aprendizado, tem como objetivo aprimorar os conhecimentos no protocolo MQTT e a biblioteca paho-mqtt, que é uma implementação do MQTT para Python.
</p>

## Tecnologias utilizadas:
- Python
- MQTT (mosquitto)
- paho-mqtt

## Pré-requisitos:
- Python 3.x
- mosquitto (broker MQTT)
- paho-mqtt instalado (pip install paho-mqtt)
- Conhecimentos básicos em Python e em protocolos de comunicação

## Como executar:
1. Instale o mosquitto (broker MQTT) em sua máquina.
2. Instale a biblioteca paho-mqtt (pip install paho-mqtt).
3. Abra um terminal, navegue até a pasta de instalação do mosquitto e execute "`mosquitto -v`" para iniciar o broker MQTT.
4. Abra outro terminal e execute o arquivo "`run.py`" para iniciar o subscriber no tópico configurado (por default, está como "`topics/messages`").
5. Abra outro terminal e execute o arquivo "`publisher.py`" para publicar uma mensagem no tópico configurado.

## Para alterar o tópico:
- Abra o arquivo "`broker_configs.py`" e altere o valor da variável "`TOPIC`" para o tópico desejado.

## Para fazer de forma manual, sem uso deste projeto:
- Abra um terminal e execute "`mosquitto -v`" para iniciar o broker MQTT.
- Abra outro terminal e execute "`mosquitto_sub -h localhost -p 1883 -t "topics/message"`" para iniciar o subscriber
- Abra outro terminal e execute "`mosquitto_pub -h localhost -p 1883 -t "topics/message" -m "Hello, World!"`" para publicar uma mensagem no tópico. 

## Autor:
<a href="https://github.com/mateusferroantunesdeoliveira"><img src="https://avatars.githubusercontent.com/u/53230135?v=4" width="100px;" alt=""/><br /><sub><b>Mateus Ferro Antunes de Oliveira</b></sub></a>

## 
Projeto desenvolvido e finalizado em 03/2024
