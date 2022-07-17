from queue import Queue


class CommandA:
    def execute(self):
        raise Exception('Command A error!')


class CommandB:
    def execute(self):
        raise Exception('Command B error!')


class CommandC:
    def execute(self):
        raise Exception('Command C error!')


class ExceptionHandler:
    def __init__(self, q):
        self.q = q
        self.map = {
            'CommandA'+'Exception': lambda c, ex: self.q.put(LogWriter('Write log...'+ex.__str__())),
            'CommandB'+'Exception': lambda c, ex: self.q.put(Repeat(c)),
            'CommandC'+'Exception': lambda c, ex: self.q.put(RepeatTwice(c)),
            'Repeat'+'Exception': lambda c, ex: self.q.put(LogWriter('Write log...'+ex.__str__())),
            'RepeatTwice'+'Exception': lambda c, ex: self.q.put(LogWriter('Write log...'+ex.__str__()))
        }

    def handler(self, command, ex):
        key = type(command).__name__ + type(ex).__name__
        self.map[key](command, ex)


class LogWriter:
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(self.message)


class Repeat:
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.execute()


class RepeatTwice:
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.execute()


if __name__ == '__main__':
    q = Queue()
    exceptionHandler = ExceptionHandler(q)

    q.put(CommandA())
    q.put(CommandB())
    q.put(CommandC())

    while q.qsize() > 0:
        command = q.get()
        try:
            command.execute()
        except Exception as ex:
            exceptionHandler.handler(command, ex)
