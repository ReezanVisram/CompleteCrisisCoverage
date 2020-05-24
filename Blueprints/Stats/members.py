import requests
import datetime
import json

def getCovidNumbers(countryToGet):

    countryToGet.replace(' ', '-')

    baseUrl = 'https://api.covid19api.com/country/'
    timeToGet = '?from=2020-03-01T00:00:00Z&to=' + str(datetime.datetime)

    return requests.get(baseUrl + countryToGet + timeToGet).json()

def organizeCovidNumbers(covidJson):
    confirmedCases = []
    dayTotalConfirmed = 0

    deaths = []
    dayTotalDeaths = 0

    recoveredCases = []
    dayTotalRecovered = 0

    for entry in range(len(covidJson)):
        if (entry > 0):
            if (covidJson[entry]["Date"] == covidJson[entry - 1]["Date"]):
                dayTotalConfirmed += int(covidJson[entry]["Confirmed"])
                dayTotalDeaths += int(covidJson[entry]["Deaths"])
                dayTotalRecovered += int(covidJson[entry]["Recovered"])

            else:
                confirmedCases.append(dayTotalConfirmed)
                deaths.append(dayTotalDeaths)
                recoveredCases.append(dayTotalRecovered)

                dayTotalConfirmed = 0
                dayTotalDeaths = 0
                dayTotalRecovered = 0

                dayTotalConfirmed += int(covidJson[entry]["Confirmed"])
                dayTotalDeaths += int(covidJson[entry]["Deaths"])
                dayTotalRecovered += int(covidJson[entry]["Recovered"])


    return [confirmedCases, deaths, recoveredCases]