from abc import ABC, abstractmethod

class AbstractTranslator(ABC):
    def __init__(self, game=None):
        self.game = game

    @staticmethod
    @abstractmethod
    def convert_game_output_to_model_input(*args, **kwargs):
        pass

    
    @staticmethod
    @abstractmethod
    def make_move(*args, **kwargs):
        """
        Make move in a game
        """
        pass