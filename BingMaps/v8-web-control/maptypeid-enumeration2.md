---
title: "MapTypeId Enumeration2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0b7c9c94-458f-4230-a3ec-c07b31fa92a5
caps.latest.revision: 9
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# MapTypeId Enumeration
This enumeration is used to specify the type of map style that should be displayed by the map.  It is specified as `Microsoft.Maps.MapTypeId.[Name]` where `[Name]` can be any of the following values.

Name             | Description                        | Example
---------------- | ---------------------------------- | :------------------------:
`aerial`         | The map displays aerial imagery.   | ![Aerial Map View](../v8-web-control/media/bmv8-aerialmap.png) 
`canvasDark`     | A dark version of the road maps. | ![Dark Road Map View](../v8-web-control/media/bmv8-canvasdark.PNG)
`canvasLight`    | A lighter version of the road maps which also has some of the details such as hill shading disabled. | ![Light Road Map View](../v8-web-control/media/bmv8-canvaslight.PNG)
`birdseye` | High resolution aerial imagery taken at 45 degrees to the ground, from 4 different directions. | ![Birdseye Map View](../v8-web-control/media/bmv8-birdseyetumb.png)
`grayscale`      | A grayscale version of the road maps. | ![Grayscale Road Map View](../v8-web-control/media/bmv8-grayscale.PNG)
`mercator`       | The map does not display any imagery. Use this option if you want to display custom imagery instead of Bing Maps imagery. | 
`ordnanceSurvey` | The map displays Ordnance Survey imagery. Ordnance Survey imagery is only available in the UK. Bing Maps provides the 1:25,000 OS Explorer Map and 1:50,000 OS Landranger maps. When the map is panned or zoomed out of range, road map imagery will be displayed. Map culture must be set to en-GB. 	    | ![Ordnance Survey Map View](../v8-web-control/media/bmv8-osmap.png)
`road`           | The map displays road imagery.	    | ![Road Map View](../v8-web-control/media/bmv8-roadmapimage.PNG)
`streetside`     | Provides streetside panoramas from the street level.  | ![Streetside View](../v8-web-control/media/bmv8-ssmap.png)

## High Contrast Support

To make Bing Maps more accessible, high contrast support has been added. When the user’s computer is in high contrast mode, a high contrast version of the road maps will be displayed. 
 
![High Contrast Road Map View](../v8-web-control/media/bmv8-highcontrast.png)
