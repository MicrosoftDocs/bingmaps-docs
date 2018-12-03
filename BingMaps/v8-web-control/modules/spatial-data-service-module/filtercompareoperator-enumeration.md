---
title: "FilterCompareOperator Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d32bc41f-b704-490b-bdb7-08f54c8a150a
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# FilterCompareOperator Enumeration

An enumeration that defines how to compare the filters value against the corresponding property value.  

Name                    | String Operator      | Description
----------------------- | -------------------- | ----------------------------------------
`endsWith`              | endsWith             | Determines if a string value ends with a specified string value
`equals`                | eq                   | Determines if two values are equal.
`greaterThan`           | gt                   | Determines if a first value is greater than a second value. 
`greaterThanOrEqual`    | ge                   | Determines if a first value is greater than or equal to a second value.
`isIn`                  | in                   | Determines if a value is within an array.
`lessThan`              | lt                   | Determines if a first value is less than a second value.
`lessThanOrEqual`       | le                   | Determines if a first value is less than or equal a second value.
`notEndsWith`           | not endsWith         | Determines if a string value does not end with a specified string value.
`notEquals`             | ne                   | Determines if two values are not equal.
`notStartsWith`         | not startsWith       | Determines if a string value does not start with a specified string value.
`startsWith`            | statrsWith           | Determines if a string value starts with a specified string value.

> [!TIP]
> The string operator version of the enumeration can be used with the Filter class as an alternative to using the enumeration object. This would reduce the amount of code that you would need to write to create a filter, but may make it less clear what the filter does.
 
> [!NOTE]
> If an object type that is not supported by a filter compare operator is used, executing the filter will return false.

> [!NOTE]
> The NavteqNA and NavteqEU data sources do not support the endsWith, notEndsWith, notStartsWith, or startsWith filter compare operators.