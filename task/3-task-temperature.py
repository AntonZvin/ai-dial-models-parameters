from app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

# Test with different temperature values - uncomment one at a time to see differences

# Low temperature (deterministic)
print("\n\n=== Testing temperature=0.0 (deterministic) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=0.0,
)

# Medium temperature (balanced)
print("\n\n=== Testing temperature=0.7 (balanced) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=0.7,
)

# High temperature (creative)
print("\n\n=== Testing temperature=1.0 (creative) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=1.0,
)

# Very high temperature (very creative but potentially incoherent)
print("\n\n=== Testing temperature=2.0 (very creative) ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=2.0,
)