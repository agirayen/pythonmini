import speedtest

wifi=speedtest.Speedtest()
print("download speed : ",wifi.download())
print("upload spped : ",wifi.upload())

# pip install speedtest-cli
