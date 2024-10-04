import pytest
from src.joer_ai import JoerAI

@pytest.fixture
def ai():
    return JoerAI()

def test_greeting(ai):
    response = ai.respond("hello")
    assert response in ["Hello!", "Hi there!", "Hey! How can I help you?"]

def test_name(ai):
    response = ai.respond("what is your name")
    assert response in ["My name is JoerAI.", "I'm JoerAI, nice to meet you!"]

def test_unknown_input(ai):
    response = ai.respond("xyzabc")
    assert response == "I'm not sure how to respond to that. Can you please rephrase or ask something else?"

def test_weather(ai):
    response = ai.respond("what's the weather in New York")
    assert response == "I'm sorry, I don't have access to real-time weather information."

def test_tell_me_about(ai):
    response = ai.respond("tell me about python")
    assert response == "I'm sorry, I don't have detailed information about python. Is there anything else I can help with?"
