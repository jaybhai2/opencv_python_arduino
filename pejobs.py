# from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests
  
#my_url = 'http://a810-bisweb.nyc.gov/bisweb/JobsByLicenseNumberServlet?alljobtype=&passdocnumber=01&requestid=0&alljappproftitle=PE&alljapplicnumber=092097&allinquirytype=BXS1LI08'

# url_response = urlopen(my_url)
# page_html = url_response.read()
# url_response.close()

#html_page =requests.get(my_url)

#print (html_page.status_code)

jsonResponse = requests.get


html_page = open('C:\\Users\\jweif\\Desktop\\PyProject\\source_page.html') 

soup = BeautifulSoup(html_page,"html.parser")

tableElements = soup.find_all('table')  

tableElement = tableElements[3]
#table001 = center001.find_all('table')

result_rows = tableElement.find_all('tr')

result_rows_3to41 = result_rows[3:]

for eachRow in result_rows_3to41:
    rowCells = eachRow.find_all('td')
    
    fileDate = rowCells[0].get_text().strip()
    jobNumber = rowCells[1].get_text().strip()
    docNumber = rowCells[2].get_text().strip()
    note = rowCells[3].get_text().strip()
    jobType = rowCells[4].get_text().strip()
    proCert = rowCells[5].get_text().strip()
    address = rowCells[8].get_text().strip()
    jobStatus = rowCells[10].get_text().strip()

    print (fileDate + "," + jobNumber + "," + docNumber + "," + note + "," + jobType + "," + 
    proCert + "," + address + "," + jobStatus)



#print (result_rows[3:])

