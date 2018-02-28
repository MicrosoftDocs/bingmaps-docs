---
title: "Colors | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b00fe5f7-57bc-430e-9e00-3113d17b8392
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Colors
Colors are used by a number of classes in Bing Maps such as Polylines and Polygons and can be specified in one of two ways. The first method is to use [CSS3 color strings](http://www.w3.org/wiki/CSS3/Color). All CSS3 colors are supported, including [extended named colors](http://www.w3.org/wiki/CSS3/Color/Extended_color_keywords). Here are some examples of the different CSS3 color strings you can use.

Color Type         | Example                    | Description
------------------ | -------------------------- | -----------------------
Hex Color          | `#ff0000`                  | This would be the color red. This format does not support transparency.
RGB                | `rgb(0, 255, 0)`           | This would be the color green. This format does not support transparency.
RGBA               | `rgba(0, 255, 0, 0.5)`     | This would be the color green with 50% transparency.
HSL                | `hsl(0, 100%, 50%)`        | HSL stands for Hue-Saturation-Lightness. This example would be the color red. This format does not support transparency.
HSLA               | `hsla(0, 100%, 50%, 0.4)`  | This would be the color red with a 40% transparency.
Color Name         | `red`                      | This would be the color red. This format does not support transparency.
Extend Color Name  | `deepskyblue`              | This would be a deep sky blue color. This format does not support transparency.

The second way to define a color in Bing Maps is by using the [Microsoft.Maps.Color](Color%20Class.md) class. 

The benefit of using the [Color class](Color%20Class.md) over CSS3 color strings is that you can easily access the individual properties of the color in a programmatic way.


### References

  * [Color Class](Color%20Class.md)
