import unittest
from src.data.make_dataset import load_data
from src.features.build_features import encode_categorical_variables

class TestDataFunctions(unittest.TestCase):
    def test_load_data(self):
        """Test that data loading returns a DataFrame."""
        df = load_data('path/to/test/data.csv')
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_encode_categorical_variables(self):
        """Test categorical variable encoding."""
        df = pd.DataFrame({'cat_var': ['A', 'B', 'C', 'A']})
        df_encoded = encode_categorical_variables(df, ['cat_var'])
        self.assertEqual(df_encoded.shape[1], 3)  # Check if 3 dummy columns are created

if __name__ == '__main__':
    unittest.main()
