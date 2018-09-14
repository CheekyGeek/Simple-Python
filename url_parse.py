import sys
from urlparse import urlparse

def url_parser(param_url,filename):
    url_parsed = urlparse(param_url)
	# parse the url using urlparse from the standard Python library
	# you can obtain the following attributes from url_parsed
    # e.g param_url = 'http://www.eller.arizona.edu:2016/index.html'
    # url_parsed.hostname: Hostname = 'www.eller.arizona.edu'
    # url_parsed.port: port number = 2016
    # url_parsed.path: path of the file = '/index.html'
    # check out the full document of the urlparse module at https://docs.python.org/2/library/urlparse.html
    # My Code - Varsha
    host = str(url_parsed.netloc).partition(":")[0]
    path = url_parsed.path
    if (str(url_parsed.port) == "None"):
        port = 80
    else:
        port = url_parsed.port
    # Write your code here
    # Open the file (filename from function parameter)
    # opening file - Varsha
    filepath = open(str(filename), "a+")
    # write the url, host, port and path to file
    # writing to file - Varsha
    filepath.write("url: %s\nhost: %s\npath: %s\nport: %s\n" %(param_url,host,path,port))
    # return filename
    return filename

url = sys.argv[1]
filetosave = sys.argv[2]
    
# url = raw_input ("enter url to be parsed: ")
# filetosave = raw_input ("enter file name: ")
stored_file = url_parser(url, filetosave)

#display the filename which contains th eparsed attributes of the url
print("The parsed attributes are stored in: %s" %stored_file)