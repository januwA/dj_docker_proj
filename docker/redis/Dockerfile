FROM redis:6.2.6-alpine
COPY ./conf/redis.conf /usr/local/etc/redis/redis.conf
COPY ./redis.sh /usr/local/redis.sh
RUN chmod 777 /usr/local/redis.sh
ENTRYPOINT ["/usr/local/redis.sh"]