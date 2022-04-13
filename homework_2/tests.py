import unittest
from unittest.mock import patch, Mock
from main import Move, Rotate


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


class TestRotate(unittest.TestCase):
    @patch('main.Rotable')
    def test_rotate(self, mock):
        mock_rotable = mock()

        mock_next = Mock()
        mock_next.next.return_value = 2

        mock_rotable.get_direction.return_value = mock_next
        mock_rotable.get_angular_velocity.return_value = 2

        rotate = Rotate(mock_rotable)
        rotate.execute()

        mock_rotable.set_direction.assert_called_with(2)


if __name__ == '__main__':
    unittest.main()
