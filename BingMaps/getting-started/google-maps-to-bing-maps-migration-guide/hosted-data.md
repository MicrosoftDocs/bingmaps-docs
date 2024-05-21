---
title: Download location data hosted in Google Fusion tables
titleSuffix: Bing Maps
description: "Learn about migrating data from Google Fusion Tables to Bing Maps."
author: stevemunk
ms.author: v-munksteve
ms.date: 07/27/2022
ms.topic: conceptual
ms.service: bing-maps
services: bing-maps
---

# Download location data hosted in Google Fusion tables

[!INCLUDE [bing-maps-enterprise-service-retirement](../../includes/bing-maps-enterprise-service-retirement.md)]

In Google Maps, developers often store their custom map data using Google Fusion. Bing Maps provides a similar solution called Bing Spatial Data Services (SDS).

This service provides three key functionalities:

1. Bulk geocoding and reverse geocoding (geocode 200,000 addresses with a single request).
1. Ability to host your custom data and expose it as a spatial REST service which can
    easily be accessed from your application. There are also many public data
    sources available which you can also access.
1. Access to Bing Maps administrative boundary data.

If you are preparing to migrate from Google Maps to Bing Maps, and you store your custom map data using Google Fusion, this article will guide you through that process.

When it comes to hosting your data in the Bing Spatial Data Services, Bing Maps provides a simple user interface where you can upload
and maintain your data easily. Bing Maps also provides a set of REST services which allows you to do all this programmatically.

## Migrate your data from Google Fusion Tables

Follow these steps to migrate data from Google Fusion Tables to the Bing Spatial Data Services:

1. Log into your Google Fusion Tables account and select the table of data you want to export.

1. select **Download** from the **File** menu.

1. Select **All rows** to download.

1. Set the file type to **KML**.

   > *If a filter is currently applied to the map, choose whether to apply it for the KML download*

1. Select the **download** button.

1. Log into your [Bing Maps account](https://www.bingmapsportal.com)

1. select **Upload Data** from the **Data sources** tab.

    :::image type="content" source="./media/image3.png" alt-text="Screen shot of the upload a data source page in Bing Maps.":::

1. Give your data source a name. The name can be up to 50 characters in
    length and must not have any spaces.

1. Select one of your Bing Maps keys to be the Master key. Master keys can
    modify the data source using the REST API's. It is not recommended
    that this same key be used in your application as users could
    potentially edit your data source.

1. Select a different Bing Maps key to be the Query Key. A query key is
    only able to query the data source. It is recommended that this same
    key is used to load your map.

1. Set the data format to **KML**.

1. Select the **Browser** button then select your KML file.

1. Select the **Upload** button.

    This will take you to a new page where you can manage your data
    sources. Once the upload process has completed you can publish your
    data source. Later you can also come here to manually edit your data
    if you desire.

1. Once published, under the **Data sources tab**, select **Data Source
    Information**.

1. Find your newly published data source. Copy the **Query URL** and
    use this in your application to query this data source.

## Additional information

If you need information on reformating location data to match the required schema for the Bing [Spatial Data Services](../../spatial-data-services/index.md)
see [Load Data Source Data Schema](../../spatial-data-services/data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md).

## Next steps

> [!div class="nextstepaction"]
> [Migrating Google Maps to Bing Maps](Google-Maps-to-Bing-Maps-Migration-Guide.md)
