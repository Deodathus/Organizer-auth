
from src.modules.shared.application.messenger import Query, Command, QueryHandler, \
    QueryBus as QueryBusInterface, CommandBus as CommandBusInterface


class CommandBus(CommandBusInterface):
    handlers = {}

    def __init__(self, handlers: dict):
        self.handlers = handlers

    def handle(self, command: Command):
        self.handlers[command.__class__].handle(command)


class QueryBus(QueryBusInterface):
    handlers = {}

    def __init__(self, handlers: dict):
        self.handlers = handlers

    def handle(self, query: Query):
        return self.handlers[query.__class__].handle(query)

