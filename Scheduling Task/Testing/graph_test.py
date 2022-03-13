import Graph.graph as graph
import pytest

"""
Test wrong parameters 
"""
def test_update_edges_wrong_data_type_parameter():    
    #A wrong data type is passed as a parameter to update_edges()
    with pytest.raises(TypeError, match="Invalid 'route' param data type not iterable"):
        graph_obj = graph.Graph()
        routes = object
        graph_obj.update_edges(routes)
        
def test_update_edges_wrong_data_in_list():   
    #The correct parameter type is used but the contents have the wrong data type
    with pytest.raises(ValueError, match="Route value not an int"):
        graph_obj = graph.Graph()
        routes = [1, '2']
        graph_obj.update_edges(routes)

"""
Test class functionality
"""
def test_update_edges():
    #Test to check if the new edge values replace the previous 0 values
    graph_obj = graph.Graph()
    graph_obj.update_edges([1,2,3,4,5,6,7,8,9,10])
    a1_edge = graph_obj.edges['A1'][0]
    a2_edge = graph_obj.edges['A2'][1]
    assert (a1_edge == 1 and a2_edge == 2)