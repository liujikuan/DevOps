const { Builder, By } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const options = new chrome.Options();
options.addArguments('--ignore-certificate-errors');

async function googleSearch() {
    let driver = await new Builder().forBrowser('chrome').build();

    try {
        await driver.get('http://app:8080');
        await driver.findElement(By.linkText('Sign In')).click();
        let title = await driver.getTitle();
        setTimeout(() => {
            console.log(title);
            driver.quit();
        }, 5000);
    } catch (error) {
        console.error('Error:', error);
        await driver.quit();
    }
}

googleSearch();
