from app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

# Test with different models and n parameter values - uncomment one at a time

# Test with GPT-4o and n=3
print("\n\n=== Testing GPT-4o with n=3 ===")
run(
    deployment_name='gpt-4o',
    n=3,
)

# Test with Claude and n=2
print("\n\n=== Testing Claude-3-7-Sonnet with n=2 ===")
run(
    deployment_name='claude-3-7-sonnet@20250219',
    n=2,
)

# Test with Gemini and n=4
print("\n\n=== Testing Gemini-2.5-Pro with n=4 ===")
run(
    deployment_name='gemini-2.5-pro',
    n=4,
)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
