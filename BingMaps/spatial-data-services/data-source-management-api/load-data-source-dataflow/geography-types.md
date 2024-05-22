---
title: "Geography Types | Microsoft Docs"
description: Describes geography types and provides tables that outline attributes, descriptions, and data types for all supported geography types.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a34b5d41-52e5-432b-add1-3133a013df50
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Geography Types

[!INCLUDE [bing-maps-enterprise-service-retirement](../../../includes/bing-maps-enterprise-service-retirement.md)]

These geography types can be used to:  
  
- Add a geography property to a data source entity schema. See [Data Schema and Sample Input](../../data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md).  
  
- Query for entities that are within a specified geography using the 'intersects' spatial filter. See [Query Options](../../query-api/query-options.md).  
  
- Query for entities and return the intersection of the geography for each entity with a specified geography using the 'intersections' function. See [Query Options](../../query-api/query-options.md).  
  
 **Limits and Requirements**  
  
- The maximum number of points for any entity geography value is 100,000.  
  
- The maximum number of points for the 'intersects' spatial filter and 'intersection' function is 250.  
  
- When using CSV format to define entity data, enclose the geography description in quotes ("").  
  
- When using 'intersects' and 'intersection' functions, enclose the geography description in single quotes(' ').  
  
## Recommended Geographies

 The following geography types are recommended to give the best performance when querying.

|Attribute|Description|Input Data Type|OData Data Type|  
|-|-|-|-|  
|Point|A pair of latitude and longitude values. For a more detailed description, see [Point](https://technet.microsoft.com/library/bb964737.aspx).<br /><br /> Examples:<br /><br /> POINT(116.03059 44.49031)|well-known text (WKT)|Edm.Geography|  
|LineString|A set of latitude and longitude values that are connected by line segments. For a more detailed description and examples, see [LineString](https://technet.microsoft.com/library/bb895372.aspx).<br /><br /> For CSV files, this value must be enclosed in quotes ("") when the value contains a comma (,).<br /><br /> Examples:<br /><br /> LINESTRING(-116.03059 44.49031, -116.03117 44.4928)<br /><br /> CSV file: "LINESTRING (-116.03059 44.49031, -116.03117 44.4928)"|well-known text (WKT)|Edm.Geography|  
|Polygon|One or more sets of latitude and longitude points that describe a closed outer shape and closed shapes within the outer shape. The area of the polygon is the space between the inner and outer shape boundaries. Points are connected by line segments. The first and last points of each set must be the same. For a more detailed description and examples, see [Polygon](https://technet.microsoft.com/library/bb895267.aspx).<br /><br /> For CSV files, this value must be enclosed in quotes ("") when the value contains a comma (,).<br /><br /> Examples:<br /><br /> POLYGON ((-95.44067 48.6559, -95.44083 48.66306, …-95.44067 48.6559))<br /><br /> CSV file: "POLYGON ((-95.44067 48.6559, -95.44083 48.66306, …-95.44067 48.6559))"|well-known text (WKT)|Edm.Geography|  
  
## Other Geographies

 The following geography types are supported, but for best performance when querying, use line string, polygon and point types.  
  
|Attribute|Description|Input Data Type|OData Data Type|
|-|-|-|-|  
|MultiPoint|A set of points. For a more detailed description and examples, see  [MultiPoint](https://technet.microsoft.com/library/bb964738.aspx).<br /><br /> For CSV files, this value must be enclosed in quotes ("") when the value contains a comma (,).<br /><br /> Examples:<br /><br /> MULTIPOINT((-122.3, 47),( -121.3 47))<br /><br /> CSV file: "MULTIPOINT((-122.3, 47),( -121.3 47))"|well-known text (WKT)|Edm.Geography|  
|MultiLineString|A set of line strings. For a more detailed description and examples, see  [MultiLineString](https://technet.microsoft.com/library/bb895166.aspx).<br /><br /> For CSV files, this value must be enclosed in quotes ("") when the value contains a comma (,).<br /><br /> Examples:<br /><br /> MULTILINESTRING((-122.3 47, -121.3 47), (-121.3 45, -122.3 47))<br /><br /> CSV file: "MULTILINESTRING((-122.3 47, -121.3 47), (-121.3 45, -122.3 47))"|well-known text (WKT)|Edm.Geography|  
|MultiPolygon|A set of polygons that to not overlap. For a more detailed description and examples, see  [MultiPolygon](https://technet.microsoft.com/library/bb964739.aspx).<br /><br /> Examples:<br /><br /> MULTIPOLYGON((-95.44067 48.6559, -95.44083 48.66306, -95.43524 48.66315, -95.44067 48.6559)),((-95.43503 48.65588, -95.42981 48.65556, -95.4297 48.6524, -95.43503 48.65588)))<br /><br /> CSV file: " MULTIPOLYGON((-95.44067 48.6559, -95.44083 48.66306, -95.43524 48.66315, -95.44067 48.6559)),((-95.43503 48.65588, -95.42981 48.65556, -95.4297 48.6524, -95.43503 48.65588)))"|well-known text (WKT)|Edm.Geography|  
|GeometryCollection|A set of multiple geography types. For a more detailed description and examples, see  [GeometryCollection](https://technet.microsoft.com/library/bb933792.aspx).<br /><br /> For CSV files, this value must be enclosed in quotes ("") when the value contains a comma (,).<br /><br /> Examples:<br /><br /> GEOMETRYCOLLECTION(POINT(116.03059 44.49031),LINESTRING(-115.92223 44.23223, -115.73234 44.432784))<br /><br /> CSV file: "GEOMETRYCOLLECTION(POINT(116.03059 44.49031),LINESTRING(-115.92223 44.23223, -115.73234 44.432784))"|well-known text (WKT)|Edm.Geography|
