import pytest
import logging
logger=logging.getLogger("Test_test_sample1")

class Test:  
    @pytest.mark.api
    @pytest.mark.dependency(name="class_Test_Test1", scope="class")
    def test_test1(self):
        assert (2 + 3) == 6
        logger.info("Result1 is published")
        
    @pytest.mark.smoke
    @pytest.mark.dependency( depends=["class_Test_Test1"], scope="class")
    def test_test2(self):
        assert [1, 2, 3] == [1, 2, 3]
        assert 1 in [1, 2, 3], "Item not present in the list"
        logger.info("Result2")

    def test_exception_message(self):
        with pytest.raises(ZeroDivisionError) as e1:
            10 / 0  # type: ignore

        assert (str(e1.value)) == "division by zero"
        logger.info("Result3")
