from google.cloud import dialogflowcx_v3beta1 as dialogflow
import os

project_id = os.getenv("project_id")
location_id = os.getenv("location_id")
agent_id = os.getenv("agent_id")
environment = os.getenv("environment")
language_code = os.getenv("language_code")


def detect_intent(session_id, text):
    session_path = (
        f"projects/{project_id}/locations/{location_id}/agents/{agent_id}/"
        f"environments/{environment}/sessions/{session_id}"
    )
    
    session_client = dialogflow.SessionsClient()
    text_input = dialogflow.TextInput(text=text)
    query_input = dialogflow.QueryInput(text=text_input, language_code=language_code)
    request = dialogflow.DetectIntentRequest(
        session=session_path, query_input=query_input
    )
    response = session_client.detect_intent(request=request)
    return response.query_result.response_messages[0].text.text[0]
