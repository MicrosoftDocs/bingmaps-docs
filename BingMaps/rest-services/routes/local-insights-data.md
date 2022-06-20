---
title: "Local Insights | Microsoft Docs"
ms.custom: ""
ms.date: "12/12/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 64c43775-3911-4c76-a0b4-32dc5824a258
caps.latest.revision: 4
author: "eriklindeman"
ms.author: "eriklind"
manager: "stevelom"
ms.service: "bing-maps"
---

# Local Insights Data

Description of a successful [Local Insights](local-insights.md) request. Please see [Type Identifiers](../common-parameters-and-types/type-identifiers/index.md) for a list of business types.

## `LocalInsightsResponse`

|JSON | XML | Field Description |
|-----|-----|-------------------|
|`typeResults`| `TypeResults`| List of business type resources.|
|`origin` | `Origin` | Latitude and longitude of the center of the isochrone.|

### Origin Field Example 

```json
"origin": {
   "latitude": 47.811091,
   "longitude": -122.369512
}
```

## Business Category Type Resource

|JSON | XML | Field Description |
|-----|-----|-------------------|
|`categoryTypeName`|`CategoryTypeName`| String name/ID for the specified category. |
|`categoryTypeSummary` | `CategoryTypeSummary`| Summary of how many entities fall under this type, given the specified time or driving limits.<br /><br />Example: `5 Department Stores in 30 Minutes by Driving`|
|`entities` | `Entities`| List of entity resources. |
   

## Entity Resource

|JSON | XML | Field Description |
|-----|-----|-------------------|
|`entityName` | `EntityName` | Name of entity. |
|`latitude`|`Latitude`| Latitude of entity. |
|`longitude`|`Longitude`| Longitude of entity.|

## Example

```json
{
   "__type": "LocalInsightsResponse:http://schemas.microsoft.com/search/local/ws/rest/v1",
   "categoryTypeResults": [
   {
      "categoryTypeName": "Parks",
      "categoryTypeSummary": "5 Parks in 10 Miles by Driving",
      "entities": [
         {
         "entityName": "Richmond Beach Center Park",
         "latitude": 47.77205339744016,
         "longitude": -122.38522949061662
         },
         {
         "entityName": "Meadowdale Playfields",
         "latitude": 47.84778315817534,
         "longitude": -122.32521969622377
         },
         {
         "entityName": "Drug Rehab Lake Forest Park",
         "latitude": 47.7546081542969,
         "longitude": -122.277923583984
         },
         {
         "entityName": "Lake Forest Park City Hall",
         "latitude": 47.75391081186926,
         "longitude": -122.27754771953607
         },
         {
         "entityName": "Dogwood Play Park",
         "latitude": 47.72104,
         "longitude": -122.29211
         }
      ]
   },
   {
      "categoryTypeName": "Parking",
      "categoryTypeSummary": "0 Parking in 10 Miles by Driving",
      "entities": []
   }
   ],
   "origin": {
   "latitude": 47.811091,
   "longitude": -122.369512
   }
}
```
