import unittest

from unittest.mock import Mock, MagicMock
from main import LogWriter, ExceptionHandler, Repeat, RepeatTwice, CommandA, CommandB, CommandC


class TestExceptionHandler(unittest.TestCase):
    def test_handler_log_writer(self):
        ''' проверка обработчика, ставящего команду записи лога в очередь команд '''

        q = Mock()
        command = CommandA()
        exceptionHandler = ExceptionHandler(q)
        exceptionHandler.handler(command, Exception())
        assert isinstance(q.put.call_args.args[0], LogWriter)

    def test_handler_repeat_command(self):
        ''' проверка обработчика, ставящего команду повторения в очередь команд '''

        q = Mock()
        command = CommandB()
        exceptionHandler = ExceptionHandler(q)
        exceptionHandler.handler(command, Exception())
        assert isinstance(q.put.call_args.args[0], Repeat)

    def test_handler_repeat_and_log(self):
        ''' проверка обработчика двойной попытки выполнить команду '''
        q = Mock()
        command = CommandC()
        exceptionHandler = ExceptionHandler(q)
        exceptionHandler.handler(command, Exception())
        assert isinstance(q.put.call_args.args[0], RepeatTwice)



class TestRepeat(unittest.TestCase):
    def test_repeat_once(self):
        ''' проверка команды повторяющей команду выбросившую исключение '''

        c = Mock()
        command = Repeat(c)
        command.execute()
        c.execute.assert_called()


class TestLogWriter(unittest.TestCase):
    def test_stdout_log(self):
        ''' проверка записи лога  '''
        message = MagicMock()
        command = LogWriter(message)
        command.execute()
        message.__str__.assert_called()


if __name__ == '__main__':
    unittest.main()