from core.intent_classifier import predict_intent
from core.llm_handler import get_llm_response


def get_response(user_input):
    if not user_input.strip():
        return "Please type a question to get started!"

    intent = predict_intent(user_input)
    response = get_llm_response(user_input, intent)
    return response