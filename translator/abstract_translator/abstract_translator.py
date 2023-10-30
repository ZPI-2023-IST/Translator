from abc import ABC, abstractmethod

class AbstractTranslator(ABC):
    def __init__(self, game=None):
        self.game = game

    @abstractmethod
    def make_move(self, *args, **kwargs):
        """
        Make a move in a game
        """
        pass

    @abstractmethod
    def get_moves(self, *args, **kwargs):
        """
        Get list of possible moves from the game and convert them to model input
        """
        pass

    @abstractmethod
    def get_board(self, *args, **kwargs):
        """
        Get board from the game and convert it to model input
        """
        pass

    @abstractmethod
    def get_state(self, *args, **kwargs):
        """
        Get from the game its current status
        """
        pass
    
    @abstractmethod
    def start_game(self, *args, **kwargs):
        """
        Start game
        """
        pass
