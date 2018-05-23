import pytest

cmdopt = "sean"
result = [ ]

@pytest.fixture
def test_getTweetbyUser(cmdopt):
    api = cmdopt
    for cmdopts in api : 
        result.append(cmdopt) 
    print(result)

def executive(cmdopt):
    if cmdopt is not None :
        test_getTweetbyUser(cmdopt)
    else : 
        print("Error")

def test_executive():
    executive(cmdopt)




