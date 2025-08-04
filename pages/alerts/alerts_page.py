from locators.alerts_pages_locators import AlertPageLocators
from pages.base_page import BasePage

class AlertsPage(BasePage):
    locators = AlertPageLocators()

    def click_to_see_alert(self):
        alert = self.element_is_visible(self.locators.ALERT_BTN)
        self.go_to_element(alert)
        alert.click()
