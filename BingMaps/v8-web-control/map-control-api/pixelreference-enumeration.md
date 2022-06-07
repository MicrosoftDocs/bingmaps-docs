---
title: "PixelReference Enumeration | Microsoft Docs"
description: "Describes the PixelReference enumeration and provides a table that outlines the description for the control, page, and viewport enumerations."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d773a67b-1298-48c1-beb5-67919bf103c8
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# PixelReference Enumeration
An enumeration which is used to defined what pixel coordinates are relative to.

Name       | Description
---------- | -------------------------
control    | The pixel is defined relative to the map control’s root element, where the top left corner of the map control is (0, 0). Using this option might cause a page reflow which may negatively impact performance.
page       | The pixel is defined relative to the page, where the top left corner of the HTML page is (0, 0). This option is best used when working with mouse or touch events. Using this option might cause a page reflow which may negatively impact performance.
viewport   | The pixel is defined in viewport coordinates, relative to the center of the map, where the center of the map is (0, 0). This option is best used for positioning geo-aligned entities added to the user layer.
