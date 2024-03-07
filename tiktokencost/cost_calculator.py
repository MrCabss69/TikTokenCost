
# CostCalculator 
# This module provides functionality to estimate the cost of using OpenAI's API models based on the input text.
# It uses tiktoken for token calculation and a model registry for pricing information.
# Creado por: [@MrCaabs69]
# Fecha de creación: Thu Mar 07 2024

from tiktokencost.models import model_registry
from tiktokencost.exceptions import ModelNotFoundException, OptionNotFoundException
import tiktoken

class CostCalculator:
    def __init__(self, model_name):
        """
        Initializes the CostCalculator with the specified model.

        :param model_name: Name of the model to be used for cost calculation.
        :raises ModelNotFoundException: If the model is not found in the registry.
        """
        self.model = model_registry.get_model(model_name)
        if not self.model:
            raise ModelNotFoundException(f"Model '{model_name}' not found in the registry.")

    def estimate_cost(self, text, request_type):
        """
        Estimates the cost of a request based on the number of tokens in the input text and the model's pricing.

        :param text: The input text for which the cost is to be estimated.
        :param request_type: The type of request (e.g., 'input', 'output', 'training').
        :return: Estimated cost in USD.
        :raises OptionNotFoundException: If the request type option is not available for the model.
        """
        encoding = tiktoken.encoding_for_model(self.model.name)
        num_tokens = len(encoding.encode(text))
        option = self.model.options.get(request_type)
        if not option:
            raise OptionNotFoundException(f"Option '{request_type}' not available for the model '{self.model.name}'.")

        return (num_tokens / 1_000_000) * option.price