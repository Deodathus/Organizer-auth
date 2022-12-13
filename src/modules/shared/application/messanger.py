

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
