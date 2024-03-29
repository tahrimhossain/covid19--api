
# covid19--api

A REST api made using flask that returns covid data




### Get Summary


GET https://covid19-api.onrender.com/summary

### Response

```
{"_id": "summary", 
"Global": {
    "NewConfirmed": 288111, 
    "TotalConfirmed": 237809849, 
    "NewDeaths": 4491, 
    "TotalDeaths": 4853007, 
    "TotalRecovered": 214867625, 
    "NewRecovered": 253925
    }, 
    "Countries": 
    [
        {
            "Country": "USA",
            "Flag": "https://www.worldometers.info/img/flags/small/tn_us-flag.gif" 
            "NewConfirmed": 9428, 
            "TotalConfirmed": 45030695, 
            "NewDeaths": 207, 
            "TotalDeaths": 730413, 
            "TotalRecovered": 34480801, 
            "NewRecovered": 1670
        },

        ...
        ...
        ...

    ]    
```


### Get Global


GET https://covid19-api.onrender.com/global

### Response
```
{
    "NewConfirmed": 288111, 
    "TotalConfirmed": 237809849, 
    "NewDeaths": 4491, 
    "TotalDeaths": 4853007, 
    "TotalRecovered": 214867625, 
    "NewRecovered": 253925
}
```

### Get Country


GET https://covid19-api.onrender.com/country/{countryname}

### Response

```
{
    "Country": "USA",
    "Flag": "https://www.worldometers.info/img/flags/small/tn_us-flag.gif" 
    "NewConfirmed": 9428, 
    "TotalConfirmed": 45030695, 
    "NewDeaths": 207, 
    "TotalDeaths": 730413, 
    "TotalRecovered": 34480801, 
    "NewRecovered": 1670
}
```


### Get All Daily New Confirmed


GET https://covid19-api.onrender.com/all/confirmed/{countryname}

### Response

```
[
    {
        "Cases": 0, 
        "Date": "2020-02-15T00:00:00Z"
    }, 
    {
        "Cases": 0, 
        "Date": "2020-02-16T00:00:00Z"
    },

    ...
    ...
    ...

]

```  


### Get All Daily New Deaths

GET https://covid19-api.onrender.com/all/death/{countryname}

### Response

```
[
    {
        "Cases": 0, 
        "Date": "2020-02-15T00:00:00Z"
    }, 
    {
        "Cases": 0, 
        "Date": "2020-02-16T00:00:00Z"
    },

    ...
    ...
    ...

]

```  