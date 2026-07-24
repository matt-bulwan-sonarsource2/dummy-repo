import os

# Dummy credentials formatted for secret scanner testing
ANTHROPIC_API_KEY = "sk-ant-api03-EXAMPLE_KEY_FOR_TESTING_PURPOSES_ONLY_0123456789abcdefghijklmnopqrstuvwxyz-AA"
OPENAI_API_KEY = "sk-proj-EXAMPLE1234567890abcdefghijklmnopqrstuvwxyz01234567890abcdef"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def initialize_clients():
    """Simulates initializing API clients with hardcoded secrets."""
    print("Testing secret detection capabilities...")
    if ANTHROPIC_API_KEY and OPENAI_API_KEY and AWS_SECRET_ACCESS_KEY:
        print("Credentials loaded successfully.")


if __name__ == "__main__":
    initialize_clients()
