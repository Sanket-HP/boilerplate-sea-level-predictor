import unittest
import sea_level_predictor

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot(self):
        # Test to ensure that the plot is generated without errors
        sea_level_predictor.draw_plot()

if __name__ == "__main__":
    unittest.main()
