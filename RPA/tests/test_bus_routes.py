import pytest
from unittest.mock import patch, MagicMock
from app.scraper.bus_routes import BusRoutesScraper

@pytest.fixture
def scraper():
    return BusRoutesScraper("start", "destination")

@patch('app.scraper.bus_routes.webdriver.Chrome')
@patch('app.scraper.bus_routes.ChromeDriverManager')
def test_setup_driver(mock_chrome_driver_manager, mock_chrome, scraper):
    mock_service = MagicMock()
    mock_chrome_driver_manager().install.return_value = mock_service
    driver = scraper.setup_driver()
    mock_chrome.assert_called_once()
    assert driver == mock_chrome()

@patch('app.scraper.bus_routes.WebDriverWait')
def test_accept_cookies(mock_webdriver_wait, scraper):
    mock_driver = MagicMock()
    mock_button = MagicMock()
    mock_webdriver_wait().until.return_value = mock_button
    scraper._driver = mock_driver
    scraper.accept_cookies()
    mock_button.click.assert_called_once()
    assert mock_webdriver_wait.call_count == 2

@patch('app.scraper.bus_routes.WebDriverWait')
def test_click_location_result(mock_webdriver_wait, scraper):
    mock_driver = MagicMock()
    mock_location_result = MagicMock()
    mock_webdriver_wait().until.return_value = mock_location_result
    scraper._driver = mock_driver
    scraper.click_location_result()
    mock_location_result.click.assert_called_once()
    assert mock_webdriver_wait.call_count == 2

@patch('app.scraper.bus_routes.WebDriverWait')
def test_enter_text(mock_webdriver_wait, scraper):
    mock_driver = MagicMock()
    mock_text_field_start = MagicMock()
    mock_text_field_destination = MagicMock()
    mock_location_result = MagicMock()
    mock_webdriver_wait().until.side_effect = [mock_text_field_start, mock_location_result, mock_text_field_destination, mock_location_result, mock_location_result]
    scraper._driver = mock_driver
    scraper.enter_text()
    assert mock_text_field_start.send_keys.call_count == len(scraper.start_text)
    assert mock_text_field_destination.send_keys.call_count == len(scraper.destination_text)
    assert mock_webdriver_wait.call_count == 5
    assert mock_location_result.click.call_count == 2

@patch('app.scraper.bus_routes.WebDriverWait')
def test_click_search(mock_webdriver_wait, scraper):
    mock_driver = MagicMock()
    mock_search_button = MagicMock()
    mock_webdriver_wait().until.return_value = mock_search_button
    scraper._driver = mock_driver
    scraper.click_search()
    mock_search_button.click.assert_called_once()
    assert mock_webdriver_wait.call_count == 2

@patch('app.scraper.bus_routes.WebDriverWait')
def test_click_inner_element(mock_webdriver_wait, scraper):
    mock_driver = MagicMock()
    mock_minimize_button = MagicMock()
    mock_agency_span = MagicMock()
    mock_webdriver_wait().until.side_effect = [mock_minimize_button, mock_agency_span, mock_agency_span]
    scraper._driver = mock_driver
    scraper.click_inner_element()
    mock_minimize_button.click.assert_called_once()
    mock_agency_span.click.assert_called_once()
    assert mock_webdriver_wait.call_count == 3

@patch('app.scraper.bus_routes.WebDriverWait')
def test_click_result(mock_webdriver_wait, scraper):
    mock_driver = MagicMock()
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "type ng-star-inserted"
    mock_element.text = "Sample Text"
    mock_webdriver_wait().until.return_value = True
    mock_driver.find_elements.return_value = [mock_element]
    scraper._driver = mock_driver
    result = scraper.click_result()
    assert result == ["Sample Text"]
    assert mock_webdriver_wait.call_count == 2
    assert mock_driver.find_elements.call_count == 1