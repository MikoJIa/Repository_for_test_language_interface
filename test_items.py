import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_should_see_button_adding_in_basket_on_page(browser):
    browser.get(link)
    button_adding_to_basket = browser.find_element(By.XPATH, "//button[@value='Add to basket']").text
    assert button_adding_to_basket == "Add to basket"
