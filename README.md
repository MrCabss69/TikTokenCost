# TikTokenCost
TikCost module is designed to provide users with estimated costs for inference and training using OpenAI's public models. Leveraging a combination of tiktoken and a comprehensive dictionary that reflects the latest OpenAI API pricing, this module offers a simple solution for managing and forecasting your OpenAI-related expenses.


## Features
- **Tiktoken Based**: Use tiktoken for accurate token number calculation.
- **Exact Cost Estimation**: Calculate the estimated costs for using various OpenAI models for inference and training purposes, based on the model and the token number on the given text.
- **Updated Pricing Dictionary**: Access a fixed dictionary that is regularly updated to reflect the most current OpenAI API pricing.


## Installing

```bash
pip install tiktokencost
```

## Basic Use
First, you want to change the path on 'https://github.com/MrCabss69/TikTokenCost/blob/master/tiktokencost/models.py' to your own model_config.json path, on line @34 - load_models()

After that, you're ready to go. Here is a basic example of how to use TikTokenCost to estimate the cost of an input text with the GPT-3 model:


```python
from tiktokencost import CostCalculator

# Initialize the cost calculator with the desired model
cost_calculator = CostCalculator("gpt-3")

# Text for which to estimate the cost
input_text = "Example text to estimate the cost."

# Calculate cost
cost = cost_calculator.estimate_cost(text=input_text, request_type="input")
print(f"Estimated cost: ${cost:.2f}")
```