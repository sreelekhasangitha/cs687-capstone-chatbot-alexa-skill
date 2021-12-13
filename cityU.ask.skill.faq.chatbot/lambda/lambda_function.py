from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "City University - " + title,
            'content': "CityU's Response - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_timings():
    session_attributes = {}
    card_title = "Timings"
    speech_output = "The university is open from Monday to Friday, 9 am to 5 pm Pacific standard time"
    reprompt_text = "Sorry if you did not understand my response. Based on your question, we are open from Monday to Friday, 9 am to 5 pm Pacific standard time"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_address(intent):
    session_attributes = {}
    card_title = "Address"
    level = intent['slots']['Location']['value']
    if level.lower() == 'seattle' or level.lower() == 'washington':
        speech_output = 'we are located at 521 Wall Street in Seattle washington'
    elif level.lower() == 'canada' or level.lower() == 'vancouver':
        speech_output = 'we are located at 789 West Pender Street in Vancouver British Columbia'
    else:
        speech_output = 'Please visit our website www.cityu.edu/about-cityu/locations-overview for all the locations'
    fulfillment_state = "Fulfilled"
    reprompt_text = "We are located in Seattle and Vancouver. You can visit our website cityu.edu/about-cityu/locations-overview for more details"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))   

def get_programs_offered(intent):
    session_attributes = {}
    card_title = "Programs"
    level = intent['slots']['DegreeLevel']['value']
    if level.lower() == 'masters':
        speech_output = 'We offer Master in Business Administration, Master in Program Management and Master in Computer Science'
    elif level.lower() == 'certificate':
        speech_output = 'We offer Certificate in English Langugage Proficiency, Certificate in Marketing and Certificate in Full-stack development'
    elif level.lower() == 'bachelors':
        speech_output = 'We offer Bachelors in Criminal Justice and Bachelors in Information Systems'
    else:
        speech_output = 'Please visit our website www.cityu.edu/programs-overview for more details related to programs we offer'
    fulfillment_state = "Fulfilled"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        

def get_housing_details():
    session_attributes = {}
    card_title = "Housing"
    speech_output = "City University of Seattle offers Cornish Commons, a 20-story residence hall building for housing in Seattle, You can visit www.cityu.edu/housing for more details"
    reprompt_text = "please visit www.cityu.edu/housing has all details about housing"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_advisor_details():
    session_attributes = {}
    card_title = "Advisor"
    speech_output = "You can get in touch with an admission advisor at 888-422-4898, or please email us at info@cityu.edu and we will reach out to you" 
    reprompt_text = "you can email us at info@cityu.edu and an advisor will be able to help you"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_scholarship_details():
    session_attributes = {}
    card_title = "Scholarship"
    speech_output = ("City University is dedicated to promoting your success in education and in your career by offering a variety of scholarships "
    "like need based, merit based and program based, just to name a few. "
    "Please visit www.cityu.edu/admissions-us/scholarships to look at all the different scholarship programs we offer.") 
    reprompt_text = "Please visit www.cityu.edu/admissions-us/scholarships for a variety of scholarhsip programs your have or email us at info@cityu.edu for more details on a specific scholarship"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_test_response():
    """ An example of a custom intent
    """
    session_attributes = {}
    card_title = "Test"
    speech_output = "I am trying to help with a test message"
    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hello, welcome to City University of Seattle Support! what can I help you with?"
    reprompt_text = "I don't know if you heard me, welcome to City University help. Do you have a question for me?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying city university support skill. " \
                    "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    pass

def on_launch(launch_request, session):
    # skill launch message
    return get_welcome_response()


def on_intent(intent_request, session):

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to skill intent handlers
    if intent_name == "Timings":
        return get_timings()
    elif intent_name == "Address":
        return get_address(intent)
    elif intent_name == "OfferedPrograms":
        return get_programs_offered(intent)
    elif intent_name == "Housing":
        return get_housing_details()
    elif intent_name == "Advisor":
        return get_advisor_details()
    elif intent_name == "Scholarship":
        return get_scholarship_details()
    elif intent_name == "AMAZON.HelpIntent":
        return get_test_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
    

# --------------- End of Lambda ------------------