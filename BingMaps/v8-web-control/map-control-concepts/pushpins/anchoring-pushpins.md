---
title: "Anchoring Pushpins | Microsoft Docs"
description: Describes how to anchor custom pushpins to the map so they maintain correct placement when zoomed in using anchor values.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7bb03aea-f569-4187-9b25-eca7732766ce
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Anchoring Pushpins

One of the most common issues developers come across when using custom pushpins is that when they zoom the map it appears as if their pushpin is drifting to or from the location it is meant to be anchored to. This is due to an incorrect anchor value in the pushpin options. The anchor specifies which pixel coordinate of the image, relative to the top left corner of the image, should overlap the pushpins location coordinate.
  
For example, consider the following pushpin, which is 24 pixels wide and 26 pixels tall. For this pushpin we would want the bottom point of the pushpin to align with the pushpins location coordinate which in this case would need an x offset that is half the wide and a y offset equal to the height of the image. This would require an anchor point of (12, 36):

![Diagram showing the vertical dimension of a pushpin icon is 36 px and the horizontal dimension is 12 px.](../../media/bmv8-anchoringpushpins-dimensions.png)
 
Here are some addition pushpin images and anchor values that can be used to properly position the pushpin.

:::image type="icon" source="../../media/bmv8-anchoringpushpins-aligncenter.png":::
#### Align with Center Anchor: (17, 17)

:::image type="icon" source="../../media/bmv8-anchoringpushpins-alignwithpoint.png":::
#### Align with Point Anchor: (3, 30)

:::image type="icon" source="../../media/bmv8-anchoringpushpins-alignpushpin.png":::
#### Align with Point Anchor: (3, 30)


