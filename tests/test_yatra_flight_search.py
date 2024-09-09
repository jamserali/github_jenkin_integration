import time

import pytest

from pages.launch_page import LaunchPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestYatraFlightSearch:

    def test_flight_search(self):
        lp = LaunchPage(self.driver,self.wait)
        lp.depart_from("Bhubaneswar")
        lp.going_to("Srinagar")
        lp.date_select("10/09/2024")
        lp.search_flight()
