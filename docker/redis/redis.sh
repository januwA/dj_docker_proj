#!/bin/sh

redis-server /usr/local/etc/redis/redis.conf \
  --port "$REDIS_PORT" \
  --requirepass "$REDIS_PASS"
