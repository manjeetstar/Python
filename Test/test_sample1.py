import pytest
import logging
logger=logging.getLogger("Test_test_sample1")

class Test:    
    def test_test1(self):
        assert (2 + 3) == 5
        logger.info("Both numbers are equal and hence passed")
        
    def test_test2(self):
        assert [1, 2, 3] == [1, 2, 3]
        assert 1 in [1, 2, 3], "Item not present in the list"
        logger.info("Both validations are matching")

    def test_exception_message(self):
        with pytest.raises(ZeroDivisionError) as e1:
            10 / 0  # type: ignore

        assert (str(e1.value)) == "division by zero"
        logger.info("Avoid division by zero")
