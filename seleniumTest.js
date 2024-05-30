var webdriver = require('selenium-webdriver');

function googleSearch() {

    var driver = new webdriver.Builder().forBrowser('chrome').build();

    driver.get('http://localhost:8080').then(function () {
        driver.findElement(webdriver.By.linkText('Sign In')).click().then(function () {
            driver.getTitle().then(function (title) {
                setTimeout(function () {
                    console.log(title);
                    driver.quit();
                }, 5000);
            });
        });
    });
}
googleSearch();