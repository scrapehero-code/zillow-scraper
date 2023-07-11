# Zillow Scraper using Playwright Python

Step 1: Clone/download the repo to your local system.

Step 2: cd into the playwright_python directory.

Step 3: Install the requirements.txt using

     pip install -r requirements.txt

Step 4: Install the necessary browsers required for playwright

    playwright install

Step 5: Run the scraper code using

     python main.py

The results will be stored into a zillow_data.json in your project directory. Using the search_term as Texas homes in Zillow, we get the sample data shown below.


```json
     {
        "Address": "2604 Ruby Dr, Texas City, TX 77591",
        "Area": "2593.0 sqft",
        "Listing Type": "Foreclosure",
        "Price": "252000.0",
        "Zestimate": "184747",
        "Rent Zestimate": "1825",
        "Broker": "CCD Ventures",
        "Days On Zillow": "17",
        "Bathrooms": "3.0",
        "Bedrooms": "4.0",
        "Currency": "USD",
        "Image": "https://photos.zillowstatic.com/p_f/ISfgdluev823oh1000000000.jpg",
        "Is Zillow Owned": "False",
        "Latitude": "29.405673",
        "Longitude": "-95.000197",
        "Photo Count": "50",
        "Property ID": "188644546",
        "Property URL": "https://www.zillow.com/homedetails/2604-Ruby-Dr-Texas-City-TX-77591/188644546_zpid/",
        "Input": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Texas%20City%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-95.13022881103515%2C%22east%22%3A-94.72854118896484%2C%22south%22%3A29.28417825900559%2C%22north%22%3A29.524052498186528%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A47966%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22lot%22%3A%7B%22min%22%3A2000%7D%2C%22price%22%3A%7B%22min%22%3A200000%2C%22max%22%3A300000%7D%2C%22mp%22%3A%7B%22min%22%3A695%2C%22max%22%3A1043%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
        "Listing URL": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22:%7B%7D,%22usersSearchTerm%22:%22Texas%20City,%20TX%22,%22mapBounds%22:%7B%22west%22:-95.13022881103515,%22east%22:-94.72854118896484,%22south%22:29.28417825900559,%22north%22:29.524052498186528%7D,%22regionSelection%22:%5B%7B%22regionId%22:47966,%22regionType%22:6%7D%5D,%22isMapVisible%22:true,%22filterState%22:%7B%22lot%22:%7B%22min%22:2000%7D,%22price%22:%7B%22min%22:200000,%22max%22:300000%7D,%22mp%22:%7B%22min%22:695,%22max%22:1043%7D,%22beds%22:%7B%22min%22:2%7D%7D,%22isListVisible%22:true,%22mapZoom%22:12%7D"
    },
    {
        "Address": "8314 Quartz Ln, Texas City, TX 77591",
        "Area": "2301.0 sqft",
        "Listing Type": "House for sale",
        "Price": "224900.0",
        "Zestimate": "221213",
        "Rent Zestimate": "1800",
        "Broker": "RE/MAX Space Center",
        "Days On Zillow": "112",
        "Bathrooms": "3.0",
        "Bedrooms": "4.0",
        "Currency": "USD",
        "Image": "https://photos.zillowstatic.com/p_f/ISzzdmle6ii7w80000000000.jpg",
        "Is Zillow Owned": "False",
        "Latitude": "29.406514",
        "Longitude": "-95.002854",
        "Photo Count": "37",
        "Property ID": "247829973",
        "Property URL": "https://www.zillow.com/homedetails/8314-Quartz-Ln-Texas-City-TX-77591/247829973_zpid/",
        "Input": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Texas%20City%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-95.13022881103515%2C%22east%22%3A-94.72854118896484%2C%22south%22%3A29.28417825900559%2C%22north%22%3A29.524052498186528%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A47966%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22lot%22%3A%7B%22min%22%3A2000%7D%2C%22price%22%3A%7B%22min%22%3A200000%2C%22max%22%3A300000%7D%2C%22mp%22%3A%7B%22min%22%3A695%2C%22max%22%3A1043%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
        "Listing URL": "https://www.zillow.com/homes/for_sale/Texas-City,-TX_rb/2_p/?searchQueryState=%7B%22pagination%22:%7B%22currentPage%22:2%7D,%22usersSearchTerm%22:%22Texas%20City,%20TX%22,%22mapBounds%22:%7B%22west%22:-95.13022881103515,%22east%22:-94.72854118896484,%22south%22:29.28417825900559,%22north%22:29.524052498186528%7D,%22regionSelection%22:%5B%7B%22regionId%22:47966,%22regionType%22:6%7D%5D,%22isMapVisible%22:true,%22filterState%22:%7B%22lot%22:%7B%22min%22:2000%7D,%22price%22:%7B%22min%22:200000,%22max%22:300000%7D,%22mp%22:%7B%22min%22:695,%22max%22:1043%7D,%22beds%22:%7B%22min%22:2%7D%7D,%22isListVisible%22:true,%22mapZoom%22:12%7D"
    },
    {
        "Address": "1236 Hunter Dr, Texas City, TX",
        "Area": "1835.0 sqft",
        "Listing Type": "New construction",
        "Price": "230000.0",
        "Zestimate": "220020",
        "Rent Zestimate": "1725",
        "Broker": "Keller Williams Realty",
        "Days On Zillow": "68",
        "Bathrooms": "3.0",
        "Bedrooms": "4.0",
        "Currency": "USD",
        "Image": "https://photos.zillowstatic.com/p_f/ISfsuylyrquhts0000000000.jpg",
        "Is Zillow Owned": "False",
        "Latitude": "29.385228",
        "Longitude": "-94.913031",
        "Photo Count": "1",
        "Property ID": "27641931",
        "Property URL": "https://www.zillow.com/homedetails/1236-Hunter-Dr-Texas-City-TX-77590/27641931_zpid/",
        "Input": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Texas%20City%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-95.13022881103515%2C%22east%22%3A-94.72854118896484%2C%22south%22%3A29.28417825900559%2C%22north%22%3A29.524052498186528%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A47966%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22lot%22%3A%7B%22min%22%3A2000%7D%2C%22price%22%3A%7B%22min%22%3A200000%2C%22max%22%3A300000%7D%2C%22mp%22%3A%7B%22min%22%3A695%2C%22max%22%3A1043%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
        "Listing URL": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22:%7B%7D,%22usersSearchTerm%22:%22Texas%20City,%20TX%22,%22mapBounds%22:%7B%22west%22:-95.13022881103515,%22east%22:-94.72854118896484,%22south%22:29.28417825900559,%22north%22:29.524052498186528%7D,%22regionSelection%22:%5B%7B%22regionId%22:47966,%22regionType%22:6%7D%5D,%22isMapVisible%22:true,%22filterState%22:%7B%22lot%22:%7B%22min%22:2000%7D,%22price%22:%7B%22min%22:200000,%22max%22:300000%7D,%22mp%22:%7B%22min%22:695,%22max%22:1043%7D,%22beds%22:%7B%22min%22:2%7D%7D,%22isListVisible%22:true,%22mapZoom%22:12%7D"
    },
    {
        "Address": "3415 Hollow Mist Dr, Texas City, TX 77591",
        "Area": "1814.0 sqft",
        "Listing Type": "House for sale",
        "Price": "215000.0",
        "Zestimate": "220000",
        "Rent Zestimate": "1699",
        "Broker": "UTR TEXAS, REALTORS",
        "Days On Zillow": "62",
        "Bathrooms": "2.0",
        "Bedrooms": "3.0",
        "Currency": "USD",
        "Image": "https://photos.zillowstatic.com/p_f/ISbpphhgnoxj1v1000000000.jpg",
        "Is Zillow Owned": "False",
        "Latitude": "29.417289",
        "Longitude": "-95.034828",
        "Photo Count": "38",
        "Property ID": "251542134",
        "Property URL": "https://www.zillow.com/homedetails/3415-Hollow-Mist-Dr-Texas-City-TX-77591/251542134_zpid/",
        "Input": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Texas%20City%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-95.13022881103515%2C%22east%22%3A-94.72854118896484%2C%22south%22%3A29.28417825900559%2C%22north%22%3A29.524052498186528%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A47966%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22lot%22%3A%7B%22min%22%3A2000%7D%2C%22price%22%3A%7B%22min%22%3A200000%2C%22max%22%3A300000%7D%2C%22mp%22%3A%7B%22min%22%3A695%2C%22max%22%3A1043%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
        "Listing URL": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22:%7B%7D,%22usersSearchTerm%22:%22Texas%20City,%20TX%22,%22mapBounds%22:%7B%22west%22:-95.13022881103515,%22east%22:-94.72854118896484,%22south%22:29.28417825900559,%22north%22:29.524052498186528%7D,%22regionSelection%22:%5B%7B%22regionId%22:47966,%22regionType%22:6%7D%5D,%22isMapVisible%22:true,%22filterState%22:%7B%22lot%22:%7B%22min%22:2000%7D,%22price%22:%7B%22min%22:200000,%22max%22:300000%7D,%22mp%22:%7B%22min%22:695,%22max%22:1043%7D,%22beds%22:%7B%22min%22:2%7D%7D,%22isListVisible%22:true,%22mapZoom%22:12%7D"
    },
    {
        "Address": "2316 Emerald Ln, Texas City, TX",
        "Area": "1915.0 sqft",
        "Listing Type": "New construction",
        "Price": "243663.0",
        "Zestimate": "239047",
        "Rent Zestimate": "1825",
        "Broker": "RE/MAX Synergy",
        "Days On Zillow": "159",
        "Bathrooms": "2.0",
        "Bedrooms": "3.0",
        "Currency": "USD",
        "Image": "https://photos.zillowstatic.com/p_f/ISv0c2k4jex5zp1000000000.jpg",
        "Is Zillow Owned": "False",
        "Latitude": "29.406189",
        "Longitude": "-94.996304",
        "Photo Count": "13",
        "Property ID": "250327286",
        "Property URL": "https://www.zillow.com/homedetails/2316-Emerald-Ln-Texas-City-TX-77591/250327286_zpid/",
        "Input": "https://www.zillow.com/homes/Texas-City,-TX_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Texas%20City%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-95.13022881103515%2C%22east%22%3A-94.72854118896484%2C%22south%22%3A29.28417825900559%2C%22north%22%3A29.524052498186528%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A47966%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22lot%22%3A%7B%22min%22%3A2000%7D%2C%22price%22%3A%7B%22min%22%3A200000%2C%22max%22%3A300000%7D%2C%22mp%22%3A%7B%22min%22%3A695%2C%22max%22%3A1043%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
        "Listing URL": "https://www.zillow.com/homes/for_sale/Texas-City,-TX_rb/2_p/?searchQueryState=%7B%22pagination%22:%7B%22currentPage%22:2%7D,%22usersSearchTerm%22:%22Texas%20City,%20TX%22,%22mapBounds%22:%7B%22west%22:-95.13022881103515,%22east%22:-94.72854118896484,%22south%22:29.28417825900559,%22north%22:29.524052498186528%7D,%22regionSelection%22:%5B%7B%22regionId%22:47966,%22regionType%22:6%7D%5D,%22isMapVisible%22:true,%22filterState%22:%7B%22lot%22:%7B%22min%22:2000%7D,%22price%22:%7B%22min%22:200000,%22max%22:300000%7D,%22mp%22:%7B%22min%22:695,%22max%22:1043%7D,%22beds%22:%7B%22min%22:2%7D%7D,%22isListVisible%22:true,%22mapZoom%22:12%7D"
    },

```



<br>

### To collect property listing data from Zillow on scale and without code visit [Scrapehero Cloud](https://www.scrapehero.com/marketplace/zillow-scraper/).

<br>

### More resources on scraping and other related topics can be found [here](https://www.scrapehero.com/articles/).
