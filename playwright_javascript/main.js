const { chromium, firefox } = require('playwright');
const fs = require('fs');

const zipcode = "10001";
const maxPagination = 2;
const proxyServer = "http://<host>:<port>";


/**
 * Save data as list of dict
   as json file
 * @param {object} data 
 */
function saveData(data) {
    let dataStr = JSON.stringify(data, null, 2)
    fs.writeFile("zillow_data_js.json", dataStr, 'utf8', function (err) {
        if (err) {
            console.log("An error occured while writing JSON Object to File.");
            return console.log(err);
        }
        console.log("JSON file has been saved.");
    });
  }


/**
 * The data extraction function used to extract
   necessary data from the element.
 * @param {HtmlElement} innerElement 
 * @returns 
 */
async function extractData(innerElement) {

    async function extractData (data) {
        let count = await data.count();
        if (count) {
            return await data.innerText()
        }
        return null
    };

    const xpathPrice = "//span[@class='srp__sc-16e8gqd-1 jLQjry']"
    const xpathBeds = "//abbr[text()='bds' or text() = 'bd']/../b"
    const xpathBath = "//abbr[text()='ba']/../b"
    const xpathSqft = "//abbr[text()='sqft']/../b"
    const xpathAddr = "//address"

    // Extracting necessary data
    let price = innerElement.locator(xpathPrice);
    price = await extractData(price);

    let beds = innerElement.locator(xpathBeds)
    beds = await extractData(beds);

    let bath = innerElement.locator(xpathBath)
    bath = await extractData(bath);

    let sqft = innerElement.locator(xpathSqft)
    sqft = await extractData(sqft);

    let addr = innerElement.locator(xpathAddr)
    addr = await extractData(addr);

    return {"price": price, "beds": beds, "bath": bath, "sqft": sqft, "addr": addr}
};


/**
 * The main function initiate a browser object and handle the navigation.
 */
async function run() {
  const browser = await firefox.launch({headless: false});
  
  const context = await browser.newContext();
  const page = await context.newPage();

  // Navigating to the home page
  await page.goto('https://www.zillow.com/', { waitUntil: 'load' });

  await page.locator("xpath=//input[contains(@placeholder, 'Enter an address')]").type(zipcode, {delay: 200});
  await page.locator("xpath=//button[@id='search-icon']").click();

  // Clearing popup
  await page.waitForSelector("xpath=//button[text()='Skip this question']", {timeout: 60000});
  await page.locator("xpath=//button[text()='Skip this question']").click()
  await page.waitForLoadState("load")

  // Checking the results count
  const noResultsFound = await page.locator("xpath=//h5[text()='No matching results']").count();
  if (noResultsFound) {
      console.log(f`No results for the zipcode : ${zipcode}`);
      return
  };

  const totalResultCount = await page.locator("xpath=//span[@class='result-count']").innerText();
  console.log(`Total results found - ${totalResultCount} for zipcode - ${zipcode}`);

  let data = [];

  for (let pageNum = 0; pageNum<maxPagination; pageNum++) {

      await page.waitForLoadState("load");
      await page.waitForTimeout(10);

      let allVisibleElements = page.locator("xpath=//div[@id='grid-search-results']//li[contains(@class, 'ListItem')]");
      allVisibleElementsCount = await allVisibleElements.count()

      for (let index= 0; index < allVisibleElementsCount; index++) {

          await page.waitForTimeout(2000);
          await page.waitForLoadState("load");
          let innerElement = await allVisibleElements.nth(index);
          await innerElement.hover();

          innerElement = await allVisibleElements.nth(index);
          let dataToSave = await extractData(innerElement);
          data.push(dataToSave);
      };

      let nextPage = page.locator(`//a[@title='Next page' and @aria-disabled="false"]`);
      await nextPage.hover();
      if (await nextPage.count()) {
          await nextPage.click();
      }
      else {break};
  };
  saveData(data);

  await context.close();
  await browser.close();
};

run();
