---
title: "FilterGroup Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a4d4f00b-b44a-4aae-b3ff-7c2636f526e0
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# FilterGroup Class
A class that groups two or more logical filters or filter groups together. It can be executed against a JSON or generate a filter string that can be used with the Bing Spatial Data Services.

## Constructor

> FilterGroup(filters: ([Filter](../v8-web-control/filter-class.md) _or_ [FilterGroup](../v8-web-control/filtergroup-class.md))[], operator: [FilterLogicalOperator](../v8-web-control/filterlogicaloperator-enumeration.md), not?: boolean)

## Methods

Name                   | Return Type         | Description
---------------------- | ------------------- | -------------------------------
`execute(object: any)`    | boolean             | Executes the filter group logic against a JSON object and returns a boolean indicating if the object meets the requirement of the Filter. 
`toString()`             | string              | Converts the filter group logic into a string format that is compatible with the Bing Spatial Data Services. 

