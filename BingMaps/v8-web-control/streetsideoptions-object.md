---
title: "StreetsideOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 556bc4e9-4dcb-4df6-bfb2-b4b8ca2d259f
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# StreetsideOptions Object
The following streetside options can be used to customize how the streetside map mode is displayed to the user.

Name                           | Type              | Description
------------------------------ | ----------------- | ---------------------------
`disablePanoramaNavigation`    | boolean           | A boolean indicating if the ability to navigate between image bubbles should be disabled in streetside map mode. Default: **false**
`locationToLookAt`             | [Location](../v8-web-control/location-class.md)          | The location that the streetside panorama should be looking towards. This can be used instead of a heading.
`onErrorLoading`               | function()        | A callback function that is triggered after the streetside view has not loaded successfully.
`onSuccessLoading`             | function()        | A callback function that is triggered after the streetside view has loaded successfully.
`overviewMapMode`              | [OverviewMapMode](../v8-web-control/overviewmapmode-enumeration.md)   | Specifies how to render the overview map when in streetside mode.<br/><br/>Default: **Microsoft.Maps.OverviewMapMode.expanded**
`panoramaInfo` | [PanoramaInfo](../v8-web-control/panoramainfo-object.md) | Information for a streetside panorama scene to load.
`panoramaLookupRadius`         | number            | The radius in meters to search in for available streetside panoramas.
`showCurrentAddress`           | boolean           | A boolean indicating if the current address being viewed should be hidden when in streetside map mode. Default: **true**
`showExitButton`               | boolean           | A boolean indicating if the exit button should be hidden when in streetside map mode. Default: **true**
`showHeadingCompass`           | boolean           | A boolean indicating if the heading compass button is hidden when in streetside map mode. Default: **true**
`showProblemReporting`         | boolean           | A boolean indicating if the link to report a problem with a streetside image is hidden when in streetside map mode. Default: **true**
`showZoomButtons`              | boolean	         | A boolean indicating if the zoom buttons should be displayed when in streetside map mode. Default: **true**
