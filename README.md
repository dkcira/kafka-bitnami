# kafka-bitnami
kafka, the bitnami dockerized version

- https://hub.docker.com/r/bitnami/kafka
- https://hub.docker.com/r/bitnami/zookeeper
- https://github.com/bitnami/bitnami-docker-kafka
- https://github.com/bitnami/bitnami-docker-zookeeper

Notes:

simple/

- when using an external volume for persistifying kafka, one needs to take care of the ownership and protections of the folder that is bound inside the docker


cluster/

# start cluster
docker-compose up -d

# get inside one of the kafka brokers
docker-compose exec kafka1 bash

# create a tpoic with 3 partitions
I have no name!@8d721303d76c:/$ /opt/bitnami/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --topic mytopic --partitions 3 --replication-factor 3
Created topic mytopic.

# describe a topic
I have no name!@8d721303d76c:/$ /opt/bitnami/kafka/bin/kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic mytopic
Topic:mytopic	PartitionCount:3	ReplicationFactor:3	Configs:
	Topic: mytopic	Partition: 0	Leader: 1003	Replicas: 1003,1002,1001	Isr: 1003,1002,1001
	Topic: mytopic	Partition: 1	Leader: 1001	Replicas: 1001,1003,1002	Isr: 1001,1003,1002
	Topic: mytopic	Partition: 2	Leader: 1002	Replicas: 1002,1001,1003	Isr: 1002,1001,1003


