#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import BusinessDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'product_name': 'web3 tokenization platform',
        'description': 'A web3 tokenization platform that allows users to tokenize their funds and create tokens to be a part of web3 ecosystem.',
        'date': datetime.now().strftime("%Y-%m-%d"),
    }
    
    try:
        BusinessDevelopment().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()