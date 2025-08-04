import time

from pages.alerts.alerts_page import AlertsPage

class TestAlerts:
    def test_click_to_see_alert(self, driver):
        alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
        alerts_page.open()
        alerts_page.click_to_see_alert()
        alert = driver.switch_to.alert
        assert alert.text in "You clicked a button"
        alert.accept()
        time.sleep(5)
