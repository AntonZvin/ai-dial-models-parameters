from app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

# Test with max_tokens parameter - response will be cut short

print("\n\n=== Testing with max_tokens=10 (very short response) ===")
run(
    deployment_name='gpt-4o',
    max_tokens=10,
)

# Optional: Test with different max_tokens values
print("\n\n=== Testing with max_tokens=50 (short response) ===")
run(
    deployment_name='gpt-4o',
    max_tokens=50,
)

print("\n\n=== Testing with max_tokens=200 (medium response) ===")
run(
    deployment_name='gpt-4o',
    max_tokens=200,
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.