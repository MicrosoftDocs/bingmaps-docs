---
title: "Understanding Scale and Resolution | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 06a298e3-d114-47ae-b285-02606957b92b
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Understanding Scale and Resolution
One of the more difficult questions to answer about a [Bing](http://bing.com/) map involves determining the exact scale or resolution of a particular image.  The answer is complicated as resolution depends on several factors including the current latitude and longitude. Scale is further dependent on screen resolution.  In this article we will look at the factors that affect scale and resolution and provide you with formulas you can use to calculate approximate values.  
  
## The Mercator Projection  
 The first problem with both scale and resolution is that the world is neither flat, nor spherical.  Any flat representation of the planet is therefore a compromise between accuracy and convenience.  The [Mercator projection](http://en.wikipedia.org/wiki/Mercator_projection) is one of the traditional map projections and offers some very compelling advantages:  
  
-   The map is conformal.  In other words, that means that the scale is constant around any position.  In other words, once we have our "x" scale, we also know our "y" scale for a map segment.  
  
-   Rhumb lines are straight segments - The easiest way to understand a rhumb line is to imagine you are sailing a ship.  If you point your ship on a compass heading and go forward, you are traveling a rhumb line.  The nice feature of Mercator maps is that rhumb lines are straight lines.  You can therefore track your course with a ruler, watch and compass (assuming you correct for magnetic declination of course).  
  
 Because of these two features, Mercator projection maps are immensely valuable to sailors.  They are also very useful for mapping applications because the math works out nicely.  
  
 However, there are problems with the Mercator projection.  The Mercator projection enforces parallel lines of latitude and longitude.  That means that the distance between lines defining one degree of longitude will remain constant, even though the actual distance varies greatly as you travel away from the equator.  Latitude is affected the same way.  The stretching effect makes objects away from the equator appear larger, although the shape remains relatively correct.  
  
 The practical effect of using the Mercator projection is that our local maps are easy to understand and draw, but that the scale and resolution are going to change as a function of latitude and longitude.  
  
### Calculating Resolution  
 Map resolution is a function of the latitude, the zoom level, and a constant value.  The constant is based on the diameter of the Earth and the equations Microsoft used to set the zoom levels.  
  
 At any latitude and zoom level, you can determine the scale by using the following equation:  
  
```  
Map resolution = 156543.04 meters/pixel * cos(latitude) / (2 ^ zoomlevel)  
```  
  
 Remember that the zoom level goes from 1 to 19, and that latitude goes from -90 to 90 (assuming your cosine function works with degrees; if you need radians, multiply the latitude by Pi/180).  The equation naturally fails if you get too close to either pole, as the Mercator projection also fails when you get too close to the poles.  
  
 From this equation, we can calculate an estimated scale for each zoom level by assuming that we are at the equator:  
  
|||||  
|-|-|-|-|  
|**Zoom Level**|**Scale (m/pixel)**|**Zoom Level**|**Scale (m/pixel)**|  
|**1**|78271.52|**11**|76.44|  
|**2**|39135.76|**12**|38.22|  
|**3**|19567.88|**13**|19.11|  
|**4**|9783.94|**14**|9.55|  
|**5**|4891.97|**15**|4.78|  
|**6**|2445.98|**16**|2.39|  
|**7**|1222.99|**17**|1.19|  
|**8**|611.50|**18**|0.60|  
|**9**|305.75|**19**|0.30|  
|**10**|152.87|||  
  
 *Table 1 Resolution at the equator by zoom level*  
  
 Keep in mind that these scales will fluctuate with latitude.  For example, in Toronto (latitude 43.65), at zoom level 13, the resolution will be `19.11 * cos(43.65)` or about 13.8 meters/pixel.  If you are American, you can convert that to feet by 3.28 feet/meter to get 54.26 feet/pixel.  
  
### Calculating Scale  
 Most map people prefer to think in terms of map scale rather than resolution.  That is, they'd rather know that 1 map inch translates to 1000 feet.  In order to calculate scale, you have to know screen resolution, zoom level, and latitude.  You also have to assume that the screen resolution is fixed and equal in both x and y directions.  Since screen resolution is usually defined in pixels per inch, you also have to convert to metric.  
  
 The equation becomes:  
  
```  
Map scale = 1 : (ScreenRes pixels/inch * 39.37 inches/meter * 156543.04 meters/pixel * cos(latitude) / (2 ^ zoomlevel))  
```  
  
 For example, assuming a typical screen resolution of 85 pixels/inch and a zoom level of 13, you would have a resolution of 1 : 85 * 39.37 * 19.11 or 1 : 63950.  That means that every inch on the screen translates to 63,950 inches, or about 1 mile.  For those metrically inclined, that would be 1 cm on the screen mapping to 63950 centimeters, or about 0.64 kilometers.  
  
### Conclusion  
 In practical terms, you shouldn't ever really need to worry about resolution or scale for most mapping tasks.  Just use the built in scale and let Microsoft do the math.  However, if you need to precisely map your points or calculate your own distances, you should be familiar with both equations described above.