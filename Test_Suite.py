import pandas as pd
import os
from Analysis import plot_aqi_pie_chart  
from Analysis import analyze_average_aqi
from Analysis import create_boxplot_aqi_by_category

### All tests for pi chart ###


def test_equal_distribution():
    """Test for equal distribution of AQI categories."""
    ## Create a mock dataset with equal distribution
    test_data = pd.DataFrame({
        'aqi_category': ['Good', 'Moderate', 'Unhealthy', 'Very Unhealthy'] * 25
    })
    test_file = "test_equal_distribution.csv"
    test_data.to_csv(test_file, index=False)

    ## Verify that the function runs without error
    try:
        plot_aqi_pie_chart(test_file)
        assert True  ## If it runs successfully, pass the test
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

    ## Verify that the function runs without error
    try:
        plot_aqi_pie_chart(test_file)
        assert True  ## If it runs successfully, pass the test
    except Exception as e:
        assert False, f"Function failed with error: {e}"
    finally:
        os.remove(test_file)

### tests for pi chart finished


### Test for data validation for bar graph and for histagram
def test_analyze_average_aqi_runs():
    '''
    This test verifies that the analyze_average_aqi function can handle a valid dataset without raising errors.
    '''
    df = pd.DataFrame({
        'country_name': ['CountryA', 'CountryB', 'CountryC'],
        'city_name': ['CityX', 'CityY', 'CityZ'],
        'aqi_value': [50, 80, 120],
        'aqi_category': ['Moderate', 'Moderate', 'Unhealthy']
    })

    test_file_path = os.path.join(os.path.dirname(__file__), "temp_test_data.csv")
    df.to_csv(test_file_path, index=False)

    try:
        analyze_average_aqi(test_file_path)
    except Exception as e:
        assert False, f"analyze_average_aqi raised an exception: {e}"
    finally:
        if os.path.exists(test_file_path):
            os.remove(test_file_path)


def test_boxplot_aqi_by_category():
    """
    A simple check that create_boxplot_aqi_by_category runs without raising errors,
    using plain Python asserts.
    """
    df = pd.DataFrame({
        'country_name': ['CountryA', 'CountryB', 'CountryC'],
        'city_name': ['CityX', 'CityY', 'CityZ'],
        'aqi_value': [50, 80, 120],
        'aqi_category': ['Moderate', 'Moderate', 'Unhealthy']
    })


    test_file_path = os.path.join(os.path.dirname(__file__), "temp_test_data.csv")
    df.to_csv(test_file_path, index=False)

    try:
        create_boxplot_aqi_by_category(test_file_path)
    except Exception as e:
        assert False, f"create_boxplot_aqi_by_category raised an exception: {e}"
    finally:
        # 4. Clean up the temporary file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)