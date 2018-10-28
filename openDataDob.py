import requests
import json


url='https://data.cityofnewyork.us/resource/rvhx-8trz.json'

filter_parameters = {'$limit':'500', 'applicant_license__':'092097'}

response =  requests.get(url,filter_parameters)

#f = open('api_response.txt','r')

#response = f.read()
r = response.json()

for job in r:
    jobNumber= job['job__']
    jobType = job['job_type']
    applicantLicenseNumber = job['applicant_license__']
    applicantTitle = job['applicant_professional_title']
    applicantFirstName = job['applicant_s_first_name']
    applicantLastName = job['applicant_s_last_name']


