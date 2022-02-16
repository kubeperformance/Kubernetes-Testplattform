
from apps.test_service.models import TestEvent, Test
from django.core import serializers
import json


class TestEventService:
    """
    A class responsible for creating and managing test event objects.

    """

    
    @staticmethod
    def create_test_event(test, timestamp, message, state):              
        '''
        Creates a new event object in the database for a given test.

            Parameters:
                        test (Test): Test model object
                        timestamp (DateTime):
                        message (str):
                        state (TestEvent.EventStates): String describing the event state 
            Returns:
                        test_event (TestEvent): The created test event object
        '''

        test_event = TestEvent(test = test, timestamp=timestamp, message=message, state=state)        
        test_event.save()
        return test_event


    @staticmethod
    def get_events_for_test(test_id):
        '''
        Return all events for a given test as a Django QuerySet.

            Parameters:
                        test_id (int): id of the test
            Returns:
                        events (QuerySet): All events associated with the test
        '''
        
        test = Test.objects.get(pk=test_id)    
        events = test.events.all()
        return events

    @staticmethod
    def get_events_for_test_as_json(test_id):
        '''
        Return all events for a given test as a string encoded as a json array.

            Parameters:
                        test_id (int): id of the test
            Returns:
                        json_response (str): All events associated with the test as JSON String
        '''
        test = Test.objects.get(pk=test_id)      
        events = test.events.all()
        json_response = serializers.serialize('json', events)

        return json_response


