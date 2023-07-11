import asyncio
import json
import logging

from playwright.async_api import Playwright, async_playwright

ZIPCODE = "10001"
MAX_PAGINATION = 2
PROXY_SERVER = "http://<host>:<port>"


def save_as_json(data: list):
    """
    Save data as list of dict
    as json file
    :param data: List of dict
    :return: None
    """
    with open("zillow_data.json", "w") as file:
        json.dump(data, file, indent=4)


async def extract_data(inner_element) -> dict:
    """
    The data extraction function used to extract
    necessary data from the element.
    :param inner_element: inner listing element
    :return: data as dict
    """
    # initializing x-paths
    xpath_price = "//span[@class='srp__sc-16e8gqd-1 jLQjry']"
    xpath_beds = "//abbr[text()='bds' or text() = 'bd']/../b"
    xpath_bath = "//abbr[text()='ba']/../b"
    xpath_sqft = "//abbr[text()='sqft']/../b"
    xpath_addr = "//address"

    # Extracting necessary data
    price = inner_element.locator(xpath_price)
    price = await price.inner_text() if await price.count() else None

    beds = inner_element.locator(xpath_beds)
    beds = await beds.inner_text() if await beds.count() else None

    bath = inner_element.locator(xpath_bath)
    bath = await bath.inner_text() if await bath.count() else None

    sqft = inner_element.locator(xpath_sqft)
    sqft = await sqft.inner_text() if await sqft.count() else None

    addr = inner_element.locator(xpath_addr)
    addr = await addr.inner_text() if await addr.count() else None

    return {"price": price, "beds": beds, "bath": bath, "sqft": sqft, "addr": addr}


async def run(playwright: Playwright) -> None:
    """
    The main function initiate a browser object and handle the
    navigation.
    :param playwright: Playwright object
    :return: None
    """

    # initializing x-paths
    xpath_no_results = "//h5[text()='No matching results']"
    xpath_total_results = "//span[@class='result-count']"
    xpath_next_page = """//a[@title='Next page' and @aria-disabled="false"]"""
    xpath_text_box = "//input[contains(@placeholder, 'Enter an address')]"
    xpath_search_button = "//button[@id='search-icon']"
    xpath_popup = "//button[text()='Skip this question']"
    xpath_results_elements = (
        "//div[@id='grid-search-results']//li[contains(@class, 'ListItem')]"
    )

    # Initializing browser and creating new page.
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    # Navigating to home page
    await page.goto("https://www.zillow.com/", wait_until="domcontentloaded")
    await page.wait_for_load_state(timeout=60000)

    # Entering zipcode and hitting search button
    await page.locator(xpath_text_box).type(ZIPCODE, delay=200)
    await page.locator(xpath_search_button).click()

    # Clearing the POPUP
    await page.wait_for_selector(xpath_popup, timeout=60000)
    await page.locator(xpath_popup).click()
    await page.wait_for_load_state(timeout=60000)

    # Checking if no results
    no_results_found = await page.locator(xpath_no_results).count()
    if no_results_found:
        logging.warning(f"No results for the zipcode : {ZIPCODE}")
        return

    total_results_count = await page.locator(xpath_total_results).inner_text()
    logging.warning(
        f"Total results found - {total_results_count} for zipcode - {ZIPCODE}"
    )

    # List for saving data
    data = []

    # Paginating through each page
    for page_number in range(MAX_PAGINATION):
        # Waiting to finish the loading
        await page.wait_for_load_state("load")

        # Extracting the elements
        all_visible_elements = page.locator(xpath_results_elements)
        all_visible_elements_count = await all_visible_elements.count()

        for element_index in range(all_visible_elements_count):
            # Hovering the element to load the price
            inner_element = all_visible_elements.nth(index=element_index)
            await inner_element.hover()

            inner_element = all_visible_elements.nth(index=element_index)
            data_to_save = await extract_data(inner_element)
            data.append(data_to_save)

        next_page = page.locator(xpath_next_page)
        await next_page.hover()
        if not await next_page.count():
            break

        # Clicking the next page button
        await next_page.click()

    save_as_json(data)


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
