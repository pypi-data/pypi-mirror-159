"""
Everything concerning the upload process.
"""
import time
from typing import Any, Union
from pathlib import Path
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from webdriver_manager.chrome import ChromeDriverManager
import browser_cookie3


C_SLEEP_COEFFICIENT = 1
C_XPATH_UPLOAD_STATUS = (
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/"
    "ytcp-animatable[2]/div/div[1]/ytcp-video-upload-progress/span"
)


class Uploader:
    """Uploads a video to YouTube. Uses a selenium browser instance to do this.
    For authentication, cookies are extracted from the user's browser of choice.
    The currently logged in account in that browser will be used for upload.
    Make sure have gone to 'studio.youtube.com' with the account you wish to use, before
    using this. It will not traverse dialogue popups that you might encounter while going
    there for the first time, such as the one that asks for a channel name.
    Make sure there are no popups about anything when you go to 'studio.youtube.com'
    on the account in question.
    """

    def __init__(
        self, browser: str, headless: bool = True, suppress: bool = True
    ) -> None:
        """Initiliazes the selenium webdriver and injects it with the proper cookies.

        :param browser: The browser to extract YouTube cookies from. The currently logged in
            account will be used for upload. Supported arguments are 'chrome', 'firefox',
            'opera', 'edge', 'chromium', and 'brave'.
        :type browser: str
        :param headless: Hide the browser windows, defaults to True
        :type headless: bool, optional
        :param suppress: Suppress selenium stdout, defaults to True
        :type suppress: bool, optional
        :raises ValueError: If the passed 'browser' argument is not recognized.
        """
        options: Any = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        if suppress:
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if headless:
            options.add_argument("--headless")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            )
        logging.getLogger("WDM").setLevel(
            logging.NOTSET
        )  # Turns off the webdriver_manager logging
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=options)

        supported = {
            "chrome": browser_cookie3.chrome,
            "firefox": browser_cookie3.firefox,
            "opera": browser_cookie3.opera,
            "edge": browser_cookie3.edge,
            "chromium": browser_cookie3.chromium,
            "brave": browser_cookie3.brave,
        }
        if (x := supported.get(browser.lower())):
            cookiejar = x()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.browser.get("https://www.youtube.com")
        for cookie in cookiejar:
            if cookie.domain == ".youtube.com":
                self.browser.add_cookie(
                    {
                        "name": cookie.name,
                        "value": cookie.value,
                        "domain": cookie.domain,
                    }
                )
        self.browser.add_cookie(
            {
                "name": "CONSENT",
                "value": "YES+yt.453767233.en+FX+299",
                "domain": ".youtube.com",
            }
        )

    def upload(
        self,
        filepath: Union[str, Path],
        desc: str,
        title: str,
    ) -> str:
        """Uploads a video to YouTube.

        :param filepath: The file to upload.
        :type filepath: str or Path
        :param desc: The video description to use.
        :type desc: str
        :param title: The title to use for the video.
        :type title: str, optional
        :return: The url of the video.
        :rtype: str
        """
        self.browser.get("https://studio.youtube.com/")
        time.sleep(1*C_SLEEP_COEFFICIENT)
        self.browser.find_element(By.ID, "upload-icon").click()
        self.browser.find_element(By.CSS_SELECTOR, 'input[name="Filedata"]').send_keys(
            str(filepath)
        )
        title_element = WebDriverWait(self.browser, timeout=10).until(
            lambda d: d.find_element(By.ID, "textbox")
        )
        time.sleep(0.5*C_SLEEP_COEFFICIENT)
        title_element.send_keys(Keys.RETURN)
        title_element.send_keys(title)

        # Using two tab's to get to the description textbox is probably
        # a more reliable way than by convoluted CSS selector.
        ActionChains(self.browser).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(
            desc
        ).perform()

        not_for_kids = self.browser.find_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")
        not_for_kids.find_element(By.ID, "radioLabel").click()

        self.browser.find_element(By.ID, "next-button").click()
        self.browser.find_element(By.ID, "next-button").click()
        self.browser.find_element(By.ID, "next-button").click()

        time.sleep(0.1*C_SLEEP_COEFFICIENT)
        self.browser.find_element(By.NAME, "UNLISTED").find_element(
            By.ID, "radioLabel"
        ).click()

        def url_not_empty(driver):
            return driver.find_element(
                By.CSS_SELECTOR, ".video-url-fadeable > .ytcp-video-info"
            ).text
        video_url = WebDriverWait(self.browser, timeout=20).until(url_not_empty)

        status = self.browser.find_element(By.XPATH, C_XPATH_UPLOAD_STATUS)
        while "Uploading" in status.text:
            time.sleep(0.5*C_SLEEP_COEFFICIENT)

        done_btn = self.browser.find_element(By.ID, "done-button")
        WebDriverWait(self.browser, timeout=20).until(element_to_be_clickable(done_btn))
        done_btn.click()

        def last_dialog_available(driver):
            return driver.find_elements(
                By.CSS_SELECTOR, 'tp-yt-paper-dialog > .header > .header-content > #dialog-title'
            )
        WebDriverWait(self.browser, timeout=20).until(last_dialog_available)
        
        time.sleep(0.5*C_SLEEP_COEFFICIENT)
        self.browser.quit()
        return video_url
