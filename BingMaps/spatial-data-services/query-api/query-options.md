---
title: "Query Options | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 71be2e0e-75be-4d23-ab8b-803c9852f976
caps.latest.revision: 29
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Query Options

When you use the Query API, you can specify query options that define what data is returned and how it is formatted. Query options are specified as URL parameters. The query options used by the Query API include a subset of the query options defined by an [Open Data Protocol (OData) specification](https://www.odata.org/documentation/). In addition to the OData query options, the Query API also provides custom query options, such as a spatial filter. Use spatial filter to define the area to query.  
  
## OData Query Options  
  
|Query Option|Description|  
|------------------|------------------------------------------|  
|$filter|Specifies a conditional expression for a list of properties and values. **Note:**  You cannot filter on the latitude and longitude entity properties. <br /><br /> The Query API supports logical operators and precedence grouping. For a complete list of the supported operators, see the **Supported $filter Operators** section below.<br /><br /> The Query API also supports the StartsWith and EndsWith functions to perform wildcard searches. Only one wildcard search can be performed at a time, and wildcard searches cannot be combined with additional $filter expressions. Wildcard searches are not supported for the PointsOfInterest data source. For more information, see The **Wildcard Search Functions** section below.<br /><br /> **Examples**:<br /><br /> -   $filter=City Eq 'Seattle' And OpenOnSunday Eq 'Y'<br />-   $filter=StartsWith(Locality,'San')|  
|$format|Specifies the format of the HTTP response. The supported formats for the Query API are JSON and Atom. The default format is Atom.<br /><br /> **Example**: $format=json|  
|$inlinecount|Specifies whether or not to return a count of the results in the response. Possible values for this query option include:<br /><br /> -   allpages<br />-   none [default]<br /><br /> **Example**: $inlinecount=allpages|  
|$orderby|Specifies one or more properties to use to sort the results of a query. You can specify up to three (3) properties. Results are sorted in ascending order.<br /><br /> Each type of query, such as Query by ID or Query by Property, has a default sort order for query results. If the $orderby option is not specified, query results are sorted using the default sort for that query type. For information about the default sort rules, see the documentation for each query type. **Note:**  You cannot use the latitude and longitude properties to sort results. You can use the elevation property. **Note:**  When you specify the $orderby query option, you must also specify a spatial filter or a $filter query option. For information about spatial filters, see [Query by Area](../query-api/query-by-area.md). <br /><br /> **Example**: $orderby=PostalCode|  
|$select|Specifies one of the following:<br /><br /> 1.  The data source properties to return in the response. If the $select query option is not specified or if it is set to "*" ($select=\*), all data source properties are returned.<br />     **Example**: $select=Name,Phone<br />2.  The intersection of the entity latitude or longitude or geographical area (defined by the entity geography) with the specified geography. If an entity has both latitude and longitude and geography properties in the schema, the intersection is computed with the geography property value. . To see definitions of the available geography types, see the types defined in [Geography Types](../data-source-management-api/load-data-source-dataflow/geography-types.md). While many different geography types are available, you will get the best performance if you use polygon, linestring or point types.<br />     **Example:**$select=intersection(POLYGON((9.86445 57.13876,9.89266 57.13876, 9.89266 56.94234,9.86445 56.94234,9.86445 57.13876)))|  
|$skip|Specifies to not return a specified number of query results. For example, if this value is set to 50, then the first result that is returned is the 51st result. This option is not available in queries for the [PointsOfInterest](../public-data-sources/pointsofinterest) data source when using a Basic key. You can use the $skip query option with the $top query option to display a subset of the query results. For example, the following parameter combinations provide sets of 10 results at a time.<br /><br /> &$skip=0&$top=10 [provides results 1 to 10]<br /><br /> &$skip=10&$top=10 [provides results 11 to 20]<br /><br /> **Example**: $skip=10|  
|$top|Specifies the maximum number of results to return in the query response. The default value is 25 and the maximum value is 250. You can return more than 250 results by making multiple queries and using the $skip parameter to step through the results.<br /><br /> **Example**: $top=10|  
  
### Supported $filter Comparison Operators  
  
> [!NOTE]
>  When you are performing a StartsWith or EndsWith wildcard search, you cannot use the And or Or comparison operators to combine multiple $filter expressions.  
  
|Operator|Description|  
|--------------|-----------------|  
|**Logical Operators**|  
|Eq|Equal|  
|Ne|Not equal|  
|Gt|Greater than|  
|Ge|Greater than or equal|  
|Lt|Less than|  
|Le|Less than or equal|  
|And|Logical and **Note:**  Not supported when combined with StartsWith or EndsWith wildcard searches.|  
|Or|Logical or **Note:**  Not supported when combined with StartsWith or EndsWith wildcard searches.|  
|Not|Logical negation|  
|**Grouping Operator**|  
|()|Precedence grouping|  
  
### Wildcard Search Functions  
  
> [!NOTE]
>  Wildcard searches are not supported for the PointsOfInterest data source.  
>   
>  Wildcard searches do not support And or Or comparison operators. Therefore, you cannot combine a wildcard search with additional $filter expressions, and you cannot request more than one wildcard search at a time.  
  
|||  
|-|-|  
|$filter=StartsWith(property,searchString) eq true|Finds all property values that start with ‘searchString’.<br /><br /> Example:$filter=StartsWith(Locality,'San') eq true|  
|$filter=EndsWith(property,searchString) eq true|Finds all property values that end with 'searchString'<br /><br /> Example:$filter=EndsWith(Locality,'York') eq true|  
  
## Spatial Filter Query Options  
 Use the spatial filter in your query to set the area to search. The Query API offers four spatial filters.  
  
 **Search a set distance from a location**  
  
```url
spatialFilter=nearby(latitude,longitude,maximum distance in kilometers)  
```  
  
 **Search in a bounding box (an area defined by pairs of longitude and latitude values)**  
  
```url
spatialFilter=bbox(South Latitude,West Longitude,North Latitude,East Longitude)  
```  
  
 **Search near a route**  
  
 When you perform a nearRoute search, entities that are within one (1) mile or 1.6 kilometers are returned.  
  
```url
spatialFilter=nearRoute(latitude or ddress of route start,longitude or address of route end)  
```  
  
 **Search within a geographical area defined by a geography type**  
  
 When you perform an ‘intersects’ search, entities that are within the geographical area defined by the specified geography are returned. Supported geography types include polygon and line string and are also used to define geography properties for entities. To see definitions of these types, see [Geography Types](../data-source-management-api/load-data-source-dataflow/geography-types.md).  
  
```url
spatialFilter=intersects('geography description')  
```  
  
 Example: spatialFilter=intersects('POLYGON((9.86445 57.13876,9.89266 57.13876, 9.89266 56.94234,9.86445 56.94234,9.86445 57.13876))')
