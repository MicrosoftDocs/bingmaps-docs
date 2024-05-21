---
title: "Filter Class | Microsoft Docs"
description: Describes the filter class, which defines filter expression logic, and provides its constructor and methods.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ad462418-0043-48bb-b0e4-0e3abe98ea18
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Filter Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

The Filter class defines the logic behind a filter expression that can be executed against a JSON object or generate a filter string that can be used with the Bing Spatial Data Services.

## Constructor

> Filter(propertyName: string, operator: string | [FilterCompareOperator](filtercompareoperator-enumeration.md), value: any)

## Methods

Name                   | Return Type         | Description
---------------------- | ------------------- | -------------------------------
`execute(object: any)`    | boolean             | Executes the filter logic against a JSON object and returns a boolean indicating if the object meets the requirement of the Filter. 
`toString()`             | string              | Converts the filter logic into a string format that is compatible with the Bing Spatial Data Services. 

> [!TIP]
> If you have an array of objects and want to filter out those that match your filters, simply loop through your array and execute the filter against each object.