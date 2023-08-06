# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import asyncio
import aio_pika

from ...extend.base import Utils
from ...extend.asyncio.pool import ObjectPool


class RabbitMQProducer(aio_pika.RobustConnection):
    """RabbitMQ发布者
    """

    def __init__(self, url, **kwargs):

        super().__init__(url, **kwargs)

        self._channel = None

        self._lock = asyncio.Lock()

    @property
    def current_channel(self):

        return self._channel

    async def connect(self, *args, **kwargs):

        await super().connect(*args, **kwargs)

        await self.ready()

        if self._channel is None:
            self._channel = await self.channel()

    async def close(self):

        await self._channel.close()
        await super().close()

    async def publish(self, message, routing_key, **kwargs):

        async with self._lock:
            await self._channel.default_exchange.publish(aio_pika.Message(message), routing_key, **kwargs)

    async def batch_publish(self, messages, routing_key, **kwargs):

        async with self._lock:
            for message in messages:
                await self._channel.default_exchange.publish(aio_pika.Message(message), routing_key, **kwargs)


class RabbitMQProducerForExchange(RabbitMQProducer):
    """RabbitMQ交换机发布者
    """

    def __init__(self, url, exchange_name, **kwargs):

        super().__init__(url, **kwargs)

        self._exchange = None

        self._exchange_name = exchange_name

    @property
    def current_exchange(self):

        return self._exchange

    async def connect(self, *args, **kwargs):

        await super().connect(*args, **kwargs)

        if self._exchange is None:
            self._exchange = await self._channel.get_exchange(self._exchange_name)

    async def publish(self, message, routing_key=r'', **kwargs):

        async with self._lock:
            await self._exchange.publish(aio_pika.Message(message), routing_key, **kwargs)

    async def batch_publish(self, messages, routing_key=r'', **kwargs):

        async with self._lock:
            for message in messages:
                await self._exchange.publish(aio_pika.Message(message), routing_key, **kwargs)


class RabbitMQProducerPool(ObjectPool):
    """RabbitMQ发布者连接池
    """

    def __init__(self, url, *, pool_size=10, connection_cls=RabbitMQProducer, connection_config=None):

        self._mq_url = url

        self._connection_cls = connection_cls
        self._connection_config = connection_config if connection_config is not None else {}

        self._connections = []

        super().__init__(pool_size)

    def _create_obj(self):

        connection = self._connection_cls(self._mq_url, **self._connection_config)

        self._connections.append(connection)

        return connection

    async def connect(self):

        for connection in self._connections:
            await connection.connect()

        Utils.log.info(f'rabbitmq producer pool connected: {self._queue.qsize()}')

    async def close(self):

        for connection in self._connections:
            await connection.close()

    async def publish(self, message, routing_key=r'', **kwargs):

        async with self.get() as connection:
            await connection.publish(aio_pika.Message(message), routing_key, **kwargs)

    async def batch_publish(self, messages, routing_key=r'', **kwargs):

        async with self.get() as connection:
            for message in messages:
                await connection.publish(aio_pika.Message(message), routing_key, **kwargs)
