import pytest
import Scheduler.scheduler as scheduler

"""
Test wrong scheduler parameters
"""
class EmptyClass():
    def __init__(self):
        pass

def test_scheduler_resources_not_objects():
    #Test to check if objects belong to Routes class
    with pytest.raises(TypeError, match="Wrong class parameters"):
        empty_obj = EmptyClass()
        scheduler.Scheduler(object, empty_obj, object)
        