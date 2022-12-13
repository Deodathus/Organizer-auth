
from src.modules.shared.application.messanger import Query, Command, QueryHandler, \
    QueryBus as QueryBusInterface, CommandBus as CommandBusInterface


class CommandBus(CommandBusInterface):
    handlers = {}

    def add(self, command: str, handler: str) -> None:
        self.handlers[command] = handler

    def handle(self, command: Command):
        self.handlers.get(command).handle()


class QueryBus(QueryBusInterface):
    handlers = {}

    def __init__(self, handlers: dict):
        self.handlers = handlers

    def add(self, query: Query, handler: QueryHandler) -> None:
        self.handlers[query] = handler

    def handle(self, query: Query):
        return self.handlers[query.__class__].handle(query)

