# just some links to get the webdriver executable files to add into the $PATH
# DONT NEED THIS IN 2024!!!

mkdir -p ./browsers
cd ./browsers

# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#installation
wget --quiet https://msedgedriver.azureedge.net/126.0.2592.81/edgedriver_linux64.zip

# https://developer.chrome.com/docs/chromedriver/downloads
wget --quiet https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip

# https://github.com/mozilla/geckodriver/releases
# https://firefox-source-docs.mozilla.org/testing/geckodriver/Usage.html
# wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz

# move files about and cleanup
unzip -qq edgedriver_linux64.zip
unzip -qq chromedriver-linux64.zip

mv chromedriver-linux64/chromedriver . 
rm -rf chromedriver-linux64 Driver_Notes/ chromedriver-linux64.zip edgedriver_linux64.zip

if [ -f "./chromedriver" ] && [ -f "msedgedriver" ]; then
    echo "Drivers exist."
    echo "Run: 'export PATH=\$PATH:\$PWD/browsers'"
else
    echo "Failed to unpack drivers."
fi

