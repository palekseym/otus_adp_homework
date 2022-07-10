import unittest
from unittest.mock import Mock, patch
from main import CheckFuel, BurnFuel, Macro, Move, ChangeVelocity

class TestMove(unittest.TestCase):

    @patch('main.Movable')
    def test_move(self, mock):
        mock_movable = mock()
        mock_movable.get_position.return_value = (12, 5)
        mock_movable.get_velocity.return_value = (-7, 3)

        move = Move(mock_movable)
        move.execute()

        mock_movable.set_position.assert_called_with((12, 5), (-7, 3))

    @patch('main.Movable')
    def test_move_no_position(self, mock):
        mock_movable = mock()
        mock_movable.get_position.side_effect = Exception('Error get position')
        mock_movable.get_velocity.return_value = (-7, 3)

        move = Move(mock_movable)
        with self.assertRaises(Exception):
            move.execute()

    @patch('main.Movable')
    def test_move_no_velocity(self, mock):
        mock_movable = mock()
        mock_movable.get_position.return_value = (12, 5)
        mock_movable.get_velocity.side_effect = Exception('Error get velocity')

        move = Move(mock_movable)
        with self.assertRaises(Exception):
            move.execute()

    @patch('main.Movable')
    def test_move_no_set_position(self, mock):
        mock_movable = mock()
        mock_movable.get_position.return_value = (12, 5)
        mock_movable.get_velocity.return_value = (-7, 3)
        mock_movable.set_position.side_effect = Exception('Error set position')

        move = Move(mock_movable)
        with self.assertRaises(Exception):
            move.execute()


class TestCheckFuel(unittest.TestCase):
    def test_sufficiently_fuel(self):
        """Проверка что топлива достаточно"""

        o = Mock()
        command = CheckFuel(o)
        command.execute()
        o.check.assert_called()

    def test_no_sufficiently_fuel(self):
        """Проверка что топлива недостаточно"""

        o = Mock()
        o.check.side_effect = Exception()
        command = CheckFuel(o)
        self.assertRaises(Exception, command.execute)


class TestBurnFuel(unittest.TestCase):
    def test_burn_fuel(self):
        """Проверка сжигания топлива"""

        o = Mock()
        command = BurnFuel(o)
        command.execute()
        o.burn.assert_called()

class TestChangeVelocity(unittest.TestCase):
    def test_change_velocity(self):
        """ проверка смены мнговенной скорости """

        o = Mock()
        command = ChangeVelocity(o)
        command.execute()
        o.change_velocity.assert_called_with()

class TestMacro(unittest.TestCase):
    def test_successful_execute(self):
        """проверка выполнения успешной цепочки команд"""

        o = Mock()

        command = Macro([BurnFuel(o), CheckFuel(o)])
        command.execute()

    def test_unsuccessful_execute(self):
        """проверка выполнения неуспешной цепочки команд"""

        burn = Mock()
        check = Mock()
        check.check.side_effect = Exception()

        command = Macro([BurnFuel(burn), CheckFuel(check)])
        self.assertRaises(Exception, command.execute)

    def test_straight_ahead_with_burn_fuel(self):
        """ проверка с движением по прямой с сжиганием топлива """

        o = Mock()

        macro = Macro([BurnFuel(o), Move(o)])
        macro.execute()

        o.burn.assert_called()
        o.set_position.assert_called()


if __name__ == '__main__':
    unittest.main()
