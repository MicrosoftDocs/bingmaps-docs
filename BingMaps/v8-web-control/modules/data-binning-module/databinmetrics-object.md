---
title: "DataBinMetrics Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: eeae080e-e49c-4353-a7bc-f6fe73f30c46
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# DataBinMetrics Object

A set of values calculated from the pushpins in a data bin.

| Name          | Type   | Description                                                                          |
|---------------|--------|--------------------------------------------------------------------------------------|
| `average`       | number | The average value of the aggregation property of the pushpins in a data bin.         |
| `count`         | number | The number of pushpins in a data bin.                                                |
| `countNotBlank` | number | The number of pushpins in the data bin whose aggregation property has a value.       |
| `countNumbers`  | number | The number of pushpins in the data bin whose aggregation property is a valid number. |
| `sum`           | number | The sum of the aggregation property of the pushpins in a data bin.                   |