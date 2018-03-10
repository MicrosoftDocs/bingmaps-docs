---
title: "2010 US Census Data Sources | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 97ba5265-3fd8-48cd-b606-741478e9eea2
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# 2010 US Census Data Sources
These data sources contain a subset of 2010 US Census data sourced from the [US Census Bureau](http://census.gov/). The United States collects census data once every ten years. The last US Census was in 2010 and the next one is scheduled for 2020. These data sources provide Census data based on 4 types of geographical boundaries; states, counties, ZTCA5 (Zip Code Tabulation Area), and the 111<sup>th</sup> Congressional Districts.

## Query URLs ##


The following are the Query URL’s that can be used to access the US Census data separated by each of the 4 types of geographical boundary types.

**State Census Data Query URL**

| https://spatial.virtualearth.net/REST/v1/data/755aa60032b24cb1bfb54e8a6d59c229/USCensus2010\_States/States |
|------------------------------------------------------------------------------------------------------------|

**County Census Data Query URL**

| https://spatial.virtualearth.net/REST/v1/data/6c39d83e5812459f914832970618048e/USCensus2010\_Counties/Counties |
|----------------------------------------------------------------------------------------------------------------|

**111<sup>th</sup> Congressional District Query URL**

| https://spatial.virtualearth.net/REST/v1/data/04566e63b0d74e45aa5fa19a2f8bb8bc/USCensus2010\_CD/CongressionalDistrict111th |
|----------------------------------------------------------------------------------------------------------------------------|

**ZCTA5 Census Data Query URL**

| https://spatial.virtualearth.net/REST/v1/data/f42cab32d0ee41738d90856badd638d3/USCensus2010\_ZCTA5/ZCTA5 |
|----------------------------------------------------------------------------------------------------------|

## Entity Properties ##

The following table describes the properties that are available in the 4 different US Census geographical boundary data sources.

| Property                  | Data type     | State | County | 111th Congressional District | ZTCA5 | Description                                             |
|---------------------------|---------------|-------|--------|------------------------------|-------|---------------------------------------------------------|
| Area\_Land                | Edm.Int64     | x     | x      |                              | x     | Area of land within this area                           |
| Area\_Water               | Edm.Int64     | x     | x      |                              | x     | Area of water in this area                              |
| Boundary                  | Edm.Geography | x     | x      | x                            | x     | The polygon boundary of this area                       |
| cdsessn                   | Edm.String    |       |        | x                            |       | Congressional District Session                          |
| countyns                  | Edm.String    |       | x      |                              |       | County National Standard Code                           |
| EntityID                  | Edm.String    | x     | x      | x                            |       | A unique idenifier for the boundary                     |
| GeoID                     | Edm.String    |       | x      |                              |       | Geographic Identifier                                   |
| HousingUnits              | Edm.Int64     |       |        |                              | x     | Number of housing units within this boundary            |
| Latitude                  | Edm.Double    | x     | x      | x                            | x     | Latitude coordinate for the center of the boundary      |
| Longitude                 | Edm.Double    | x     | x      | x                            | x     | Longitude coordinate for the center of the boundary     |
| Name                      | Edm.String    | x     | x      | x                            | x     | The name of the boundary                                |
| Pop\_10\_to\_14\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 10 and 14 years of age               |
| Pop\_15\_to\_19\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 15 and 19 years of age               |
| Pop\_20\_to\_24\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 20 and 24 years of age               |
| Pop\_25\_to\_29\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 25 and 29 years of age               |
| Pop\_30\_to\_34\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 30 and 34 years of age               |
| Pop\_35\_to\_39\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 35 and 39 years of age               |
| Pop\_40\_to\_44\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 40 and 44 years of age               |
| Pop\_45\_to\_49\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 45 and 49 years of age               |
| Pop\_5\_to\_9\_years      | Edm.Int64     | x     | x      | x                            | x     | Population between 5 and 9 years of age                 |
| Pop\_50\_to\_54\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 50 and 54 years of age               |
| Pop\_55\_to\_59\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 55 and 59 years of age               |
| Pop\_60\_to\_64\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 60 and 64 years of age               |
| Pop\_65\_to\_69\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 65 and 69 years of age               |
| Pop\_70\_to\_74\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 70 and 74 years of age               |
| Pop\_75\_to\_79\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 75 and 79 years of age               |
| Pop\_80\_to\_84\_years    | Edm.Int64     | x     | x      | x                            | x     | Population between 80 and 84 years of age               |
| Pop\_85\_years\_and\_over | Edm.Int64     | x     | x      | x                            | x     | Population 85 years of age and over                     |
| Pop\_Female\_Over16       | Edm.Int64     | x     | x      | x                            | x     | Population of females over the age of 16                |
| Pop\_Female\_Over21       | Edm.Int64     | x     | x      | x                            | x     | Population of females over the age of 21                |
| Pop\_Female\_Over65       | Edm.Int64     | x     | x      | x                            | x     | Population of females over the age of 65                |
| Pop\_Male\_Over16         | Edm.Int64     | x     | x      | x                            | x     | Population of males over the age of 16                  |
| Pop\_Male\_Over21         | Edm.Int64     | x     | x      | x                            | x     | Population of males over the age of 21                  |
| Pop\_Male\_Over65         | Edm.Int64     | x     | x      | x                            | x     | Population of males over the age of 65                  |
| Pop\_Over16               | Edm.Int64     | x     | x      | x                            | x     | Population over the age of 16                           |
| Pop\_Over21               | Edm.Int64     | x     | x      | x                            | x     | Population over the age of 21                           |
| Pop\_Over65               | Edm.Int64     | x     | x      | x                            | x     | Population over the age of 65                           |
| Pop\_Under\_5\_years      | Edm.Int64     | x     | x      | x                            | x     | Population below the age of 5 years old                 |
| Population                | Edm.Int64     | x     | x      | x                            | x     | Total population                                        |
| StateCode                 | Edm.String    | x     | x      | x                            |       | 2 letter state code                                     |
| statefp                   | Edm.String    |       | x      |                              |       | 2-character state FIPS code                             |
| StateName                 | Edm.String    |       | x      | x                            |       | The name of the US state in which this boundary resides |

## See Also ##

[Bing Maps V8 - Choropleth Map Example](../v8-web-control/choropleth-map-example.md)
