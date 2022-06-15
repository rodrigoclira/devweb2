FROM alpine:3.7

COPY boot.sh /boot.sh
RUN apk --no-cache add memcached && chmod +x /boot.sh

USER memcached
CMD ["/boot.sh"]