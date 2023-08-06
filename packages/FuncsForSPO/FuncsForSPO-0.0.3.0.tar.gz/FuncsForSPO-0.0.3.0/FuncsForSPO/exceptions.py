from selenium.common.exceptions import *


class TimeoutException(TimeoutException):
    pass

class WebDriverException(WebDriverException):
    pass


class ElementClickInterceptedException(ElementClickInterceptedException):
    pass

class EmailOuLoginIncorretoElawException(Exception):
    pass
