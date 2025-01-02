#!/bin/bash

# Kafka 컨테이너 이름
KAFKA_CONTAINER=kafka

# Kafka 서비스의 기본 부트스트랩 서버 주소
BOOTSTRAP_SERVER=localhost:29092

# Kafka 컨테이너 내부에서 실행할 명령
KAFKA_COMMAND="kafka-topics"
if [ ! -z "$1" ]; then
  if [ "$1" == "topics" ]; then
    KAFKA_COMMAND="kafka-topics"
    shift
  elif [ "$1" == "console-producer" ]; then
    KAFKA_COMMAND="kafka-console-producer"
    shift
  elif [ "$1" == "console-consumer" ]; then
    KAFKA_COMMAND="kafka-console-consumer"
    shift
  elif [ "$1" == "consumer-groups" ]; then
    KAFKA_COMMAND="kafka-consumer-groups"
    shift
  else
    echo "알 수 없는 Kafka 명령어: $1"
    exit 1
  fi
fi

# 'docker-compose exec'를 사용하여 Kafka 컨테이너에서 명령 실행
docker-compose exec -T $KAFKA_CONTAINER $KAFKA_COMMAND --bootstrap-server $BOOTSTRAP_SERVER "$@"
