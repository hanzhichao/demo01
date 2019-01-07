
import pytest
@pytest.fixture
def firefox_options(firefox_options):
    # firefox_options.binary = '/path/to/firefox-bin'
    firefox_options.add_argument('-foreground')
    firefox_options.set_preference('browser.anchor_color', '#FF0000')
    return firefox_options




def test_example(selenium, firefox_options):
	selenium.get("http://www.baidu.com")