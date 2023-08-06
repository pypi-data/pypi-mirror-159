import traceback

from sys import exit
from time import sleep
from ast import literal_eval
from typing import Any, Dict
from cosecurity_amqp_lib.logger import logger
from cosecurity_amqp_lib.client import BaseClient


class Consumer(BaseClient):
    """
    queue consumer with a general handler to handle posted messages
    """
    def __init__(self, name:str, on_error_restart_consumer:bool=True, wait_time_to_restart:int=20) -> None:
        super().__init__()
        self.queue = self.get_service_queue(name)
        self.name = name
        self.on_error_restart_consumer = on_error_restart_consumer
        self.wait_time_to_restart = wait_time_to_restart
        self.restart_count = 0
        self.handlers = {}

    def register(self, handler:Any) -> bool:
        if not hasattr(handler, '__name__') or handler.__name__ in self.handlers:
            return False

        self.handlers[handler.__name__] = handler
        return True

    def start(self, arguments:Dict[str, Any]=None) -> None:
        try:
            self.channel.queue_declare(
                queue=self.queue, 
                durable=True,
                auto_delete=True,
                arguments=arguments
            )

            self.channel.basic_consume(
                queue=self.queue,
                on_message_callback=self._callback_method,
                auto_ack=True
            )

            logger.info(f'{self.name} initialized')
            self.channel.start_consuming()
        except:
            logger.error(traceback.print_exc())
            self.stop(arguments)

    def stop(self, arguments:Dict[str, Any]=None):
        try:
            self.channel.close()
            self.connection.close()
        finally:
            if self.on_error_restart_consumer:
                self.restart(arguments)
            else:
                logger.info(f'{self.name} finished')
                exit()

    def restart(self, arguments:Dict[str, Any]=None):
        self.restart_count += 1
        logger.info(f'{self.name} restarted - {self.restart_count}')
        sleep(self.wait_time_to_restart)
        self.to_connect()
        self.start(arguments)

    def _callback_method(self, ch:str, method:str, properties:Dict[str, Any], body:str) -> None:
        try:
            message = self._binary_to_dict(body)
            if not (('primitive' in message and 'content' in message) and (isinstance(message['primitive'], str) and isinstance(message['content'], dict))):
                raise Exception("""
                    It is necessary to include in the message the key 'primitive' that contains the name of the action and 'content' 
                    that has the parameters for the action
                """)

            self._handle_message(message)
        except:
            logger.error(traceback.print_exc())

    def _binary_to_dict(self, binary_json:str) -> Dict[str, Any]:
        return literal_eval(binary_json.decode('utf-8'))

    def _handle_message(self, message:Dict[str, Any]) -> None:
        if self.handlers and message['primitive'] in self.handlers:
            self.handlers[message['primitive']](message['content'])
        else:
            logger.info(f'No implementation for {message} found!')
