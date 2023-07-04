
from src.modules.shared.application.messenger import Query, Command, Event, \
    QueryBus as QueryBusInterface, CommandBus as CommandBusInterface, EventBus as EventBusInterface


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


class EventBus(EventBusInterface):
    handlers = {}

    def __init__(self, handlers: dict):
        self.handlers = handlers

    def dispatch(self, event: Event) -> None:
        return self.handlers[event.__class__].handle(event)
