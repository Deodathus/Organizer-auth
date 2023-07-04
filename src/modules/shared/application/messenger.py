

class Query(object):
    pass


class QueryHandler(object):
    def handle(self, query: Query):
        pass


class Command(object):
    pass


class CommandHandler(object):
    def handle(self, command: Command):
        pass


class Event(object):
    pass


class EventHandler(object):
    def handle(self, event: Event):
        pass


class CommandBus(object):
    def add(self, command: str, handler: str) -> None:
        pass

    def handle(self, command: Command):
        pass


class QueryBus(object):
    def add(self, query: Query, handler: str) -> None:
        pass

    def handle(self, query: Query):
        pass


class EventBus(object):
    def add(self, event: Event, handler: str) -> None:
        pass

    def dispatch(self, event: Event):
        pass

