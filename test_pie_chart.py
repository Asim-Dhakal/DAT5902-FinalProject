import pandas as pd
import os
from First import plot_aqi_pie_chart  

def test_equal_distribution():
    """Test for equal distribution of AQI categories."""
    # Create a mock dataset with equal distribution
    test_data = pd.DataFrame({
        'aqi_category': ['Good', 'Moderate', 'Unhealthy', 'Very Unhealthy'] * 25
    })
    test_file = "test_equal_distribution.csv"
    test_data.to_csv(test_file, index=False)

    # Verify that the function runs without error
    try:
        plot_aqi_pie_chart(test_file)
        print("Success: test_equal_distribution passed.")
        assert True  # If it runs successfully, pass the test
    except Exception as e:
        assert False, f"Function failed with error: {e}"
    finally:
        os.remove(test_file)

def test_missing_column():
    """Test for missing 'aqi_category' column."""
    test_data = pd.DataFrame({'random_column': [1, 2, 3]})
    test_file = "test_missing_column.csv"
    test_data.to_csv(test_file, index=False)

    try:
        plot_aqi_pie_chart(test_file)
        assert False, "Function should raise an error for missing 'aqi_category' column."
    except KeyError as e:
        print("Success: test_missing_column passed.")
        assert "'aqi_category'" in str(e), f"Unexpected error: {e}"
    finally:
        os.remove(test_file)

def test_unequal_distribution():
    """Test for unequal distribution of AQI categories."""
    test_data = pd.DataFrame({
        'aqi_category': ['Good'] * 50 + ['Moderate'] * 30 + ['Unhealthy'] * 15 + ['Very Unhealthy'] * 5
    })
    test_file = "test_unequal_distribution.csv"
    test_data.to_csv(test_file, index=False)

    # Verify that the function runs without error
    try:
        plot_aqi_pie_chart(test_file)
        print("Success: test_unequal_distribution passed.")
        assert True  # If it runs successfully, pass the test
    except Exception as e:
        assert False, f"Function failed with error: {e}"
    finally:
        os.remove(test_file)
