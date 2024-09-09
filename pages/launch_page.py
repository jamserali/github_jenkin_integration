import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By


class LaunchPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    origin_city_loc = (By.ID, 'BE_flight_origin_city')
    arrival_city_loc = (By.ID, 'BE_flight_arrival_city')
    search_btn_loc = (By.ID, 'BE_flight_flsearch_btn')
    origin_date_loc = (By.ID, 'BE_flight_origin_date')
    list_of_cities = (By.XPATH, "//p[@class='ac_cityname']")
    custom_auto_text = (By.XPATH, "//p[@class='custom-autoTxt'][1]")
    custom_dst_text = (By.XPATH, "(//p[@class='custom-autoTxt'][1])[2]")
    date_finder_loc = (By.XPATH, "//div[@id= 'monthWrapper']//tbody//td[@class!='inActiveTD']")
    custom_day_year = (By.XPATH, "//p[@class='cutom-day-year']")

    def depart_from(self, depart_location):
        element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-heading')))
        departfrom = self.driver.find_element(*self.origin_city_loc)
        departfrom.click()
        time.sleep(5)
        departfrom.send_keys(depart_location)
        time.sleep(5)

        cities = self.driver.find_elements(*self.list_of_cities)
        for city in cities:
            city_name, code = city.text.split(" (")
            code = code.replace(")", "")
            print("City: {} and Code: {}".format(city_name, code))
            if city_name == depart_location:
                city.click()
                break
        auto_text = self.driver.find_element(*self.custom_auto_text)
        assert auto_text.text == code, f"Depart location is not matching .actual: {auto_text.text} vs. expected: {code}."

    def going_to(self, destination_loc):
        destination = self.driver.find_element(*self.arrival_city_loc)
        destination.click()
        time.sleep(5)
        destination.send_keys(destination_loc)
        time.sleep(5)

        cities = self.driver.find_elements(*self.list_of_cities)
        for city in cities:
            city_name, code = city.text.split(" (")
            code = code.replace(")", "")
            print("City: {} and Code: {}".format(city_name, code))
            if city_name == destination_loc:
                city.click()
                break
        auto_text = self.driver.find_element(*self.custom_dst_text)
        assert auto_text.text == code, f"Destination location is not matching.actual: {auto_text.text} vs. expected: {code}"

    def date_select(self, date):
        date_field = self.driver.find_element(*self.origin_date_loc)
        date_field.click()
        time.sleep(5)
        dates = self.driver.find_elements(*self.date_finder_loc)
        for dt in dates:
            if dt.get_attribute('data-date') == date:
                dt.click()
                break
        cust_day = self.driver.find_element(*self.custom_day_year)
        expected = "10 Sep' 24"
        assert cust_day.text == expected, f"Date are not matching Actual: {cust_day.text}, Expected: {expected}"

    def search_flight(self):
        self.driver.find_element(*self.search_btn_loc).click()
