#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import AiNews

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
        'topic': 'Upcoming Events in bangalore',
        'current_year': str(datetime.now().year),
        'date': str(datetime.now().strftime('%y-%m-%d_%H-%M-%S')),
        'number_of_websites': 10,
    }
    
    inputs_array = [{
         'topic': 'Upcoming Events in bangalore',
        'current_year': str(datetime.now().year),
        'date': str(datetime.now().strftime('%y-%m-%d_%H-%M-%S')),
        'number_of_websites': 10,
    },
    {
        'topic': 'Multi party computing',
        'current_year': str(datetime.now().year),
        'date': str(datetime.now().strftime('%y-%m-%d_%H-%M-%S')),
        'number_of_websites': 10,
    },
    {
        'topic': 'ZK Proofs and AI',
        'current_year': str(datetime.now().year),
        'date': str(datetime.now().strftime('%y-%m-%d_%H-%M-%S')),
        'number_of_websites': 10,
    }]
    
    
    try:
        # AiNews().crew().kickoff(inputs=inputs)
        AiNews().crew().kickoff_for_each(inputs=inputs_array)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        AiNews().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiNews().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        AiNews().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


run()