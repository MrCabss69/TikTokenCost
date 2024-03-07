from tiktokencost import CostCalculator

# Initialize the cost calculator with the GPT-4 model
cost_calculator = CostCalculator("gpt-4")

# Input text for inference
input_text = "What are the main implications of artificial intelligence in modern society?"

# Calculate inference cost
cost = cost_calculator.estimate_cost(text=input_text, request_type="input")
print(f"The estimated cost of inference with GPT-4 is: ${cost:.4f}")