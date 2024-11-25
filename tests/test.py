from mypackage import mymodule

def test_top_n():
    """Make sure top n works correctly    
    """
    assert mymodule.top_n([8,2,3,7,1,5,4],3) == [8,7,4], 'incorrect'
    assert mymodule.top_n([12,9,3,10,7,2],3) == [12,10,9], 'incorrect'
    assert mymodule.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'