from locators.alerts_pages_locators import AlertPageLocators
from pages.base_page import BasePage

class AlertsPage(BasePage):
    locators = AlertPageLocators()

    def click_to_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BTN).click()