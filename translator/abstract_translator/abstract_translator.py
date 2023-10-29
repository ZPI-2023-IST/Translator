from abc import ABC, abstractmethod

class AbstractTranslator(ABC):
    @staticmethod
    @abstractmethod
    def convert_game_output_to_model_input(game_output):
        pass

    @staticmethod
    @abstractmethod
    def convert_model_output_to_game_input(game_output, model_output):
        pass