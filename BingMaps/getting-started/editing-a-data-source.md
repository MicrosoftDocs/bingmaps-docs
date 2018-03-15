---
title: "Editing a Data Source | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c287a1fb-44f7-48d3-8bc2-b3e51c88254b
caps.latest.revision: 9
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Editing a Data Source
You can edit the entity data and the data schema of any data source associated with a Bing Maps account on [Bing Maps Dev Center](https://www.bingmapsportal.com/). This includes data sources that were uploaded by using Bing Spatial Data Services.  
  
 As an alternative to editing the entity data and data schema on the Bing Maps Dev Center, you can also download a data source, make your changes and upload and publish the updated file. For more information, see [Downloading a Data Source](../getting-started/downloading-a-data-source.md).  
  
> [!NOTE]
> For information on data source limits that apply to this feature, see [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md)  
  
<a name="BKMKEditGeocode"></a>   
## Edit Entity Data  
 To edit, create and delete entity data for a data source, go to the **Manage my data sources** page under **Data sources** on [Bing Maps Dev Center](https://www.bingmapsportal.com/), and click the **Published Data Sources** tab. Click the data source name you want to edit to view the list of entities in the data source. You can delete and create new entities from this page or hover over any entity to see its location on the map. To edit an individual entity, click the entity ID. When you make changes to individual entities and click **Update**, the changes are saved locally but are not published to the data source. If you want to geocode changes to the address information, clear the latitude and longitude fields before you click **Update**. Similarly, if you want to reverse-geocode new latitude and longitude coordinates, clear all address fields before you click **Update**. Entities that have been deleted are highlighted in red and entities that are new or have been changes are highlighted in green in the entity list.  
  
> [!IMPORTANT]
> After you make changes, you **must publish your changes** for them to appear in the data source.  
  
## Edit Entity Data Schema  
 To edit the entity data schema for a data source, go to the **Manage my data sources** page under **Data sources** on [Bing Maps Account Center](http://www.bingmapsportal.com), and click the **Published Data Sources** tab. Click **Edit Schema** for the data source schema, and then make your changes.  
  
> [!IMPORTANT]
> After you make changes, you **must publish your changes to the schema** to apply them to the data source.