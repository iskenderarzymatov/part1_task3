#Make sure to un-comment the function line below when you are
#done.

def is_odd(isken): return isken % 2 == 1
 
def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(101) == True
print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_is_odd()