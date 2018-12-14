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
author: "v-chrfr"
ms.author: "v-chrfr"
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

## Business Type Resource

|JSON | XML | Field Description |
|-----|-----|-------------------|
|`typeName`|`TypeName`| String name/ID for the specified category. |
|`typeSummary` | `TypeSummary`| Summary of how many entities fall under this type, given the specified time or driving limits.<br /><br />Example: `5 Department Stores in 30 Minutes by Driving`|
|`entities` | `Entities`| List of entity resources. |
   

## Entity Resource

|JSON | XML | Field Description |
|-----|-----|-------------------|
|`entityName` | `EntityName` | Name of entity. |