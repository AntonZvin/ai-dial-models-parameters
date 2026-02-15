from app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

# Test with different frequency_penalty values - compare repetitiveness

print("\n\n=== Testing frequency_penalty=0.0 (default) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=0.0,
)

print("\n\n=== Testing frequency_penalty=1.0 (reduce repetition) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=1.0,
)

print("\n\n=== Testing frequency_penalty=2.0 (strongly reduce repetition) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=2.0,
)

# Optional: Test negative values (increases repetition)
print("\n\n=== Testing frequency_penalty=-1.0 (increase repetition) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=-1.0,
)

# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored