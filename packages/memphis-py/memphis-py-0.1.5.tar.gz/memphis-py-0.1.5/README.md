<div align="center">
  
  ![Memphis light logo](https://github.com/memphisdev/memphis-broker/blob/staging/logo-white.png?raw=true#gh-dark-mode-only)
  
</div>

<div align="center">
  
  ![Memphis light logo](https://github.com/memphisdev/memphis-broker/blob/staging/logo-black.png?raw=true#gh-light-mode-only)
  
</div>

<div align="center">
<h1>A powerful message broker for developers</h1>
<a target="_blank" href="https://twitter.com/intent/tweet?text=Probably+The+Easiest+Message+Broker+In+The+World%21+%0D%0Ahttps%3A%2F%2Fgithub.com%2Fmemphisdev%2Fmemphis-broker+%0D%0A%0D%0A%23MemphisDev"><img src="https://user-images.githubusercontent.com/70286779/174467733-e7656c1e-cfeb-4877-a5f3-1bd4fccc8cf1.png" width="60"></a> 
</div>
 
 <p align="center">
  <a href="https://memphis.dev/docs/">Docs</a> - <a href="https://twitter.com/Memphis_Dev">Twitter</a> - <a href="https://www.youtube.com/channel/UCVdMDLCSxXOqtgrBaRUHKKg">YouTube</a>
</p>

<p align="center">
<a href="https://discord.gg/WZpysvAeTf"><img src="https://img.shields.io/discord/963333392844328961?color=6557ff&label=discord" alt="Discord"></a> <a href=""><img src="https://img.shields.io/github/issues-closed/memphisdev/memphis-broker?color=6557ff"></a> <a href="https://github.com/memphisdev/memphis-broker/blob/master/CODE_OF_CONDUCT.md"><img src="https://img.shields.io/badge/Code%20of%20Conduct-v1.0-ff69b4.svg?color=ffc633" alt="Code Of Conduct"></a> <a href="https://github.com/memphisdev/memphis-broker/blob/master/LICENSE"><img src="https://img.shields.io/github/license/memphisdev/memphis-broker?color=ffc633" alt="License"></a> <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/memphisdev/memphis-broker?color=61dfc6"> <img src="https://img.shields.io/github/last-commit/memphisdev/memphis-broker?color=61dfc6&label=last%20commit">
</p>

**[Memphis{dev}](https://memphis.dev)** is a message broker for developers made out of devs' struggles develop around message brokers.<br>Enables devs to achieve all other message brokers' benefits in a fraction of the time.<br>
Focusing on automatic optimization, schema management, inline processing, and troubleshooting abilities. All under the same hood.
Utilizing NATS core.

## ⭐️ Why

Working with data streaming is HARD.<br>
As a developer, you need to build a dedicated pipeline per data source,<br>change the schema, individual analysis, enrich the data with other sources, it constantly crashes, it requires adaptation to different rate limits, constantly change APIs, and scale for better performance 🥵 .<br>
**It takes time and resources that you don't have.**<br><br>
Message broker is the answer. In short - It's an event-store.<br>
Message broker acts as the middleman and supports streaming architecture,<br>but then you encounter Apache Kafka and its documentation and run back to the monolith and batch jobs.<br>
Give memphis{dev} a spin before.

## 👉 Use-cases

- Async task management
- Real-time streaming pipelines
- Data ingestion
- Cloud Messaging
  - Services (microservices, service mesh)
  - Event/Data Streaming (observability, analytics, ML/AI)
- Queuing
- N:N communication patterns

## ✨ Features

**v0.2.2**

- 🚀 Fully optimized message broker in under 3 minutes
- 💻 Easy-to-use UI, CLI, and SDKs
- 📺 Data-level observability
- 🐳☸Runs on your Docker or Kubernetes
- 👨‍💻 Community driven

**Coming soon v0.2.5-1.0.0**

- Embedded schema registry using dbt
- Message Journey - Real-time messages tracing
- More SDKs (GoLang, Python, Kafka compatible)
- Inline processing
- Ready-to-use connectors and analysis functions

## 📸 Screenshots

|                                                                  Dashboard                                                                   |                                                               Station overview                                                               |                                                                     CLI                                                                      |
| :------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://user-images.githubusercontent.com/70286779/175805888-f08e2078-79e1-43f1-a841-1d7115bf15a8.png" alt="drawing" width="300"/> | <img src="https://user-images.githubusercontent.com/70286779/175805897-349dde51-427f-4c9b-95cd-12876a846f1a.png" alt="drawing" width="300"/> | <img src="https://user-images.githubusercontent.com/70286779/175806007-9a37e130-3e5a-4606-bdda-a71a89efae7f.png" alt="drawing" width="300"/> |

## 🚀 Getting Started

[Installation videos](https://www.youtube.com/playlist?list=PL_7iYjqhtXpWpZT2U0zDYo2eGOoGmg2mm)<br><br>
Helm for Kubernetes

```shell
helm repo add memphis https://k8s.memphis.dev/charts/ && \
helm install my-memphis memphis/memphis --create-namespace --namespace memphis
```

Docker Compose

```shell
curl -s https://memphisdev.github.io/memphis-docker/docker-compose.yml -o docker-compose.yml && \
docker compose -f docker-compose.yml -p memphis up
```

[![Connect your first app](https://img.youtube.com/vi/-5YmxYRQsdw/0.jpg)](https://youtu.be/-5YmxYRQsdw)<br>
[Tutorial: Build an event-driven food delivery app](https://medium.com/memphis-dev/how-to-build-your-own-wolt-app-b220d738bb71)

## High-Level Architecture

<img alt="memphis.dev-logo" height="500" alt="memphis.dev Architecture" src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/graphics+for+github/Architecture.png">

## Local access

### Via Kubernetes

```shell
To access Memphis UI from localhost, run the below commands:
  1. kubectl port-forward service/memphis-ui 9000:80 --namespace memphis > /dev/null &

To access Memphis using CLI or SDK from localhost, run the below commands:
  2. kubectl port-forward service/memphis-cluster 7766:7766 6666:6666 5555:5555 --namespace memphis > /dev/null &

Dashboard: http://localhost:9000
Memphis broker: localhost:5555 (Management Port) / 7766 (Data Port) / 6666 (TCP Port)
```

**For Production Environments**
Please expose the UI, Cluster, and Control-plane via k8s ingress / load balancer / nodeport

### Via Docker

Dashboard - http://localhost:9000<br>
Broker - localhost:7766<br>
Control-Plane - localhost:5555/6666<br>

## Beta

Memphis{dev} is currently in Beta version. This means that we are still working on essential features like real-time messages tracing,<br>
Schema registry, and inline processing, as well as making more SDKs and supporting materials.

How does it affect you? Well... mostly it doesn't.<br>
(a) The core of memphis broker is highly stable<br>
(b) We learn&fix fast<br><br>
But we need your love, and any help we can get by stars, PR, feedback, issues, and enhancments.<br>
Read more on https://memphis.dev/docs

## Support

### Ask a question about Memphis{dev} or related

You can ask questions, and participate in discussions about Memphis{dev}-related topics in the Memphis Discord channel.

<a href="https://discord.gg/WZpysvAeTf"><img src="https://amplication.com/images/discord_banner_purple.svg" /></a>

### Create a bug report

If you see an error message or run into an issue, please [create bug report](https://github.com/memphisdev/memphis-broker/issues/new?assignees=&labels=type%3A%20bug&template=bug_report.md&title=). This effort is valued and it will help all Memphis{dev} users.

### Submit a feature request

If you have an idea, or you're missing a capability that would make development easier and more robust, please [Submit feature request](https://github.com/memphisdev/memphis-broker/issues/new?assignees=&labels=type%3A%20feature%20request).

If a similar feature request already exists, don't forget to leave a "+1".
If you add some more information such as your thoughts and vision about the feature, your comments will be embraced warmly :)

## Contributing

Memphis{dev} is an open-source project.<br>
We are committed to a fully transparent development process and appreciate highly any contributions.<br>
Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - <br>we would love to have you as part of the Memphis{dev} community.

Please refer to our [Contribution Guidelines](./CONTRIBUTING.md) and [Code of Conduct](./code_of_conduct.md).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):<br><br>
<img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Alon+Avrahami.jpg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Ariel+Bar.jpeg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Arjun+Anjaria.jpeg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Carlos+Gasperi.jpeg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Daniel+Eliyahu.jpeg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Itay+Katz.jpeg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Jim+Doty.jpeg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Nikita+Aizenberg.jpg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Rado+Marina.jpg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"><img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Raghav+Ramesh.jpg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Tal+Goldberg.jpg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;"> <img src="https://memphis-public-files.s3.eu-central-1.amazonaws.com/contributors-images/Yehuda+Mizrahi.jpeg" width="60" height="60" style="border-radius: 25px; border: 2px solid #61DFC6;">

## Installation

```sh
$ pip install memphis
```

## Importing

```python
from memphis import Memphis
from memphis import retention_types, storage_types
```

### Connecting to Memphis

First, we need to create Memphis `object` and then connect with Memphis by using `memphis.connect`.

```python
async def main():
  try:
    memphis = Memphis()
    await memphis.connect(
      host="<memphis-host>",
      username="<application-type username>",
      connection_token="<broker-token>",
      management_port="<management-port>", # defaults to 5555
      tcp_port="<tcp-port>", # defaults to 6666
      data_port="<data-port>", # defaults to 7766
      reconnect=True, # defaults to False
      max_reconnect=10, # defaults to 10
      reconnect_interval_ms=1500, # defaults to 1500
      timeout_ms=1500 # defaults to 1500
      )
    ...
  except Exception as e:
    print(e)
  finally:
    await memphis.close()

if __name__ == '__main__':
  asyncio.run(main())
```

Once connected, the entire functionalities offered by Memphis are available.

### Disconnecting from Memphis

To disconnect from Memphis, call `close()` on the memphis object.

```python
await memphis.close()
```

### Creating a Factory

```python
factory = await memphis.factory(name="<factory-name>", description="")
```

### Destroying a Factory

Destroying a factory will remove all its resources (stations/producers/consumers)

```python
await factory.destroy()
```

### Creating a Station

```python
station = await memphis.station(
  name="<station-name>",
  factory_name="<factory-name>",
  retention_type=retention_types.MAX_MESSAGE_AGE_SECONDS, # MAX_MESSAGE_AGE_SECONDS/MESSAGES/BYTES. Defaults to MAX_MESSAGE_AGE_SECONDS
  retention_value=604800, # defaults to 604800
  storage_type=storage_types.FILE, # torage_types.FILE/torage_types.MEMORY. Defaults to MEMORY
  replicas=1, # defaults to 1
  dedup_enabled=False, # defaults to false
  dedup_window_ms: 0, # defaults to 0
)
```

### Retention types

Memphis currently supports the following types of retention:

```python
memphis.retention_types.MAX_MESSAGE_AGE_SECONDS
```

Means that every message persists for the value set in retention value field (in seconds)

```python
memphis.retention_types.MESSAGES
```

Means that after max amount of saved messages (set in retention value), the oldest messages will be deleted

```python
memphis.retention_types.BYTES
```

Means that after max amount of saved bytes (set in retention value), the oldest messages will be deleted

### Storage types

Memphis currently supports the following types of messages storage:

```python
memphis.storage_types.FILE
```

Means that messages persist on the file system

```python
memphis.storage_types.MEMORY
```

Means that messages persist on the main memory

### Destroying a Station

Destroying a station will remove all its resources (producers/consumers)

```python
await station.destroy()
```

### Produce and Consume messages

The most common client operations are `produce` to send messages and `consume` to
receive messages.

Messages are published to a station and consumed from it by creating a consumer.
Consumers are pull based and consume all the messages in a station unless you are using a consumers group, in this case messages are spread across all members in this group.

Memphis messages are payload agnostic. Payloads are `Uint8Arrays`.

In order to stop getting messages, you have to call `consumer.destroy()`. Destroy will terminate regardless
of whether there are messages in flight for the client.

### Creating a Producer

```python
producer = await memphis.producer(station_name="<station-name>", producer_name="<producer-name>")
```

### Producing a message

```python
await prod.produce(
  message=bytearray(msg, 'utf-8')), # Uint8Arrays
  ack_wait_sec=15, # defaults to 15
```

### Destroying a Producer

```python
await producer.destroy()
```

### Creating a Consumer

```python
consumer = await memphis.consumer(
  station_name="<station-name>",
  consumer_name="<consumer-name>",
  consumer_group="<group-name>", # defaults to the consumer name
  pull_interval_ms=1000, # defaults to 1000
  batch_size=10, # defaults to 10
  batch_max_time_to_wait_ms=5000, # defaults to 5000
  max_ack_time_ms=30000, # defaults to 30000
  max_msg_deliveries=10, # defaults to 10
)
```

### Processing messages

```python
async def msg_handler(msg):
  print("message: ", msg.get_data())
  await msg.ack()

consumer.consume(msg_handler)
```

### Acknowledge a message

Acknowledge a message indicates the Memphis server to not re-send the same message again to the same consumer / consumers group

```python
await message.ack()
```

### Destroying a Consumer

```python
await consumer.destroy()
```
