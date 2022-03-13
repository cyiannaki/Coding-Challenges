import pytest
import Scheduler.scheduler as scheduler

"""
Test wrong scheduler parameters
"""
def test_scheduler_resources_not_objects():
    #Test to check if objects belong to Routes class
    with pytest.raises(TypeError, match="Wrong class parameters"):
        scheduler.Scheduler(object, object, object)
        