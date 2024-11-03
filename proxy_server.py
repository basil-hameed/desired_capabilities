from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ERROR_URL

# create the class proxy server
class ProxyServer:

    # define constructor
    def __init__(self, web_url, proxy_server_url):
        self.url = web_url
        self.proxy_server = proxy_server_url

    
    # method to launch without a proxy server
    def without_proxy_server(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            print(driver.page_source)
        except ERROR_URL as error:
            print('Error', error)
    
    # method to launch with proxy server
    def with_proxy_server(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument(f"--proxy-server={self.proxy_server}")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            print(driver.page_source)
        except ERROR_URL as error:
            print(" Error", error)

# create an object and call the methods
url = "https://httpbin.io/ip"
proxy_server = "182.93.85.225:8080"
myProxy = ProxyServer(url, proxy_server)
myProxy.without_proxy_server()
myProxy.with_proxy_server()

"""
OUTPUT:
<html><head><meta name="color-scheme" content="light dark"><meta charset="utf-8"></head><body><pre>{
  "origin": "110.224.90.51:38674"
}
</pre><div class="json-formatter-container"></div></body></html>

and deselect \"Use a proxy server for your LAN\".","header":"If you use a proxy server…","proxyTitle":"Change proxy settings…","settingsTitle":"Settings"}],"suggestionsSummaryList":[{"summary":"Checking the connection"},{"summary":"\u003Ca href=\"#buttons\" onclick=\"toggleHelpBox()\">Checking the proxy and the firewall\u003C/a>"},{"summary":"\u003Ca href=\"javascript:diagnoseErrors()\" id=\"diagnose-link\">Running Windows Network Diagnostics\u003C/a>"}],"suggestionsSummaryListHeader":"Try:","summary":{"failedUrl":"https://httpbin.io/ip","hostName":"httpbin.io","msg":"\u003Cstrong jscontent=\"hostName\">\u003C/strong> took too long to respond."},"textdirection":"ltr","title":"httpbin.io"};</script></body></html>
"""