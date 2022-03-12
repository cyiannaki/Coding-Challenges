import pytest
import Scheduler.scheduler as scheduler

"""
Test wrong scheduler parameters
"""
def test_scheduler_incorrect_number_of_resources():
    #For this task there are only 2 resource objects but 3 will be given
    with pytest.raises(IndexError, match="Incorrect number of resources"):
        scheduler.Scheduler(object, object, object)