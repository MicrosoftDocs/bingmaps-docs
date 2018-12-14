---
title: "Geodata API1 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e7cd66c0-834e-472f-8209-1e798b4c6d1a
caps.latest.revision: 17
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geodata API
Use the following URLs to request a set of polygons that describe the boundaries of a geographic entity, such as an AdminDivision1 (such as a state or province) or a Postcode1 (such as a zip code) that contain a given point (latitude and longitude) or address.  
  
## Supported Http Methods  
 GET  
  
 HTTP and HTTPS  
  
## URL Template  
  
> [!IMPORTANT]
>  Note that these URLs contain a different base address (platform.bing.com) than what is found in other Bing Spatial Data Services API.  
  
 **Get the set of boundary polygons for an entity that contains the specified latitude and longitude.**  
  
```url
http://platform.bing.com/geo/spatial/v1/public/Geodata?SpatialFilter=GetBoundary(latitude,longitude,levelOfDetail,entityType,getAllPolygons,getEntityMetadata,culture,userRegion)&PreferCuratedPolygons=preferCuratedPolygons&$format=responseFormat&key=BingMapsKey  
```  
  
 **Get the set of boundary polygons for an entity that contains the specified address string. The address is geocoded to get a corresponding latitude and longitude.**  
  
```url
http://platform.bing.com/geo/spatial/v1/public/Geodata?SpatialFilter=GetBoundary(address,levelOfDetail,entityType,getAllPolygons,getEntityMetadata,culture,userRegion)&PreferCuratedPolygons=preferCuratedPolygons&$format=responseFormat&key=BingMapsKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive.  
  
|Parameter|Description|Values|  
|-|-|-|  
|latitude, longitude|**An address or latitude and longituede is required.** A  latitude and longitude specifying a point inside the entity you are requesting.  For example, when you request the boundaries of the United States, you can specify any latitude-longitude pair that falls within the land area of the United States.|A set of double values representing degrees of latitude and longitude.<br /><br /> Valid range of latitude values: [-90, +90]<br /><br /> **Example**: 47.673099<br /><br /> Valid range of longitude values: [-180, +180]<br /><br /> **Example**: -122.11871|  
|address|**An address or latitude and longitude is required.** An address stringthat is geocoded by the service to get latitude and longitude coordinates.<br /><br /> Note: This call will result in two individual usage transactions: RESTLocations (for geocoding) and RESTSpatialDataService:Geodata.   For more information about usage transactions, see [Understanding Bing Maps Transactions](../getting-started/bing-maps-dev-center-help/understanding-bing-maps-transactions.md).|A string that contains address information such as street address, locality (such as a city), admin district (such as a state).<br /><br /> **Example**: ‘1 Microsoft Way Redmond WA 98052’|  
|LevelOfDetail|**Required.** The level of detail for the boundary polygons returned.|An integer between 0 and 3, where 0 specifies the coarsest level of boundary detail and 3 specifies the best.|  
|entityType|**Required.** The entity type to return.<br /><br /> Note that not all entity types are available for each location.|A string that contains one of the following the entity types.<br /><br /> -   **CountryRegion**: Country or region<br /><br /> -   **AdminDivision1**: First administrative level within the country/region level, such as a state or a province.<br /><br /> -   **AdminDivision2**: Second administrative level within  the country/region level, such as a county.<br /><br /> -   **Postcode1**: The smallest post code category, such as a zip code.<br /><br /> -   **Postcode2**: The next largest post code category after Postcode1 that is created by aggregating Postcode1 areas.<br /><br /> -   **Postcode3**: The next largest post code category after Postcode2 that is created by aggregating Postcode2 areas.<br /><br /> -   **Postcode4**: The next largest post code category after Postcode3 that is created by aggregating Postcode3 areas.<br /><br /> -   **Neighborhood:** A section of a populated place that is typically well-known, but often with indistinct boundaries.<br /><br /> -   **PopulatedPlace**: A concentrated area of human settlement, such as a city, town or village.|  
|getAllPolygons|**Required.** Specifies whether the response should include all of the boundary polygons for the requested entity or just return a single polygon that represents the main outline of the entity.|A Boolean value.<br /><br /> -   0 or false: Return only the main outline.<br />-   1 or true: Return all polygons.<br /><br /> **Example**: If you are requesting the boundary of the United States, a value of 1 or true returns a large number of polygons which include Alaska, Hawaii and various outlying islands. However, a value of value of 0 returns a single polygon representing the main outline of the continental United States.|  
|getEntityMetadata|**Required.** Specifies whether the response should include metadata about the entity, such as AreaSqKm and others. For a list of common metadata values returned, see the table in the **Response** section.|A Boolean value.<br /><br /> -   0 or false: Do not return metadata.<br />-   1 or true: Return all entity metadata.|  
|culture|**Optional.** Specifies the preferred language to use for any metadata text about the entity or polygons.|A string containing e code of the preferred language.<br /><br /> **Examples**: en-us, zh-hans, ar.|  
|userRegion|**Optional.** Specifies the user’s home country or region|A string containing a country/region code from the ISO 3166-1 alpha-2 standard<br /><br /> Examples: US, FR, CN|  
|preferCuratedPolygons|**Optional.** Prefer curated boundary polygons. Curated polygons have been optimized for display purposes. These polygons are typically clipped to the land, and can fall somewhere between medium and high fidelity. Setting this value to true will return curated polygons if available or will fall back and return a polygon at the specified levelOfDetail. |A Boolean value.<br /><br /> -   0 or false: Returns polygons at the specified levelOfDetail.<br />-   1 or true: Tries to return curated polygons if available, otherwise returns a polygon at the specified levelOfDetail.|
|responseFormat|**Optional.**Specifies the output format of the response.|A string specifying one of the following options:<br /><br /> -   atom **[default]**<br />-   json|  
|key|**Required.** The Bing Maps Key to use for this request.|A string that contains the Bing Maps Key.|  
  
## Response  
 This URL supports the following response formats.  
  
-   Atom (application/atom + xml) [**default**]  
  
-   JSON (application/json)  
  
 When the output format is set to Atom, the results are returned in the response as one or more Atom Entries. For more information about Atom response formats, see [OData AtomPub Format](https://www.odata.org/developers/protocols/atom-format) and the Atom examples in the **Examples** section.  
  
 **Response Fields**  
  
 The following fields may be returned in the response. For actual examples, see the **Examples** section below.  
  
> [!NOTE]
>  Some information has been removed from these responses to make small enough to easily understand. Both of these responses contain a `Result` class which has the following properties.  
  
|Name|Type|Description|  
|----------|----------|-----------------|  
|Copyright|Copyright|A class that contains copyright related information.|  
|EntityID|string|A unique ID number associated with this entity.|  
|EntityMetadata|Metadata|A collection of metadata information associated with the entity. For common metadata types, see **Common metadata fields** below.|  
|Name|Name|The name information for the entity.|  
|Primitives|Primitive[]|An array of Primitive objects which contain the polygon boundary information for the entity.|  
  
 The `Copyright` class is used to store information about the various data providers used to create the data in the result entity and the associated copyright information for them. This class has the following properties.  
  
|Name|Type|Description|  
|----------|----------|-----------------|  
|CopyrightURL|string|A URL that lists many of the data providers for Bing Maps and their related copyright information.|  
|Sources|CopyrightSource[]|An array of copyright information for the various sources of data used in this entity.|  
  
 The `CopyrightSource` class contains the information of each individual copyright and has the following properties  
  
|Name|Type|Description|  
|----------|----------|-----------------|  
|SourceID|string|The ID of the source which aligns with the source ID used by the `Primiative` class.|  
|SourceName|string|The name of the data provider represented by this Source element.|  
|Copyright|string|The copyright string for the source.|  
  
 The `Metadata` class contains a number of different types of metadata which may be included with some entities. The following is a list of properties that this class has. Note that most entities will likely only have information for some and not all of these properties.  
  
|Name|Type|Description|  
|----------|----------|-----------------|  
|AreaSqKm|string|The approximate total surface area (in square kilometers) covered by all the polygons that comprise this entity.|  
|BestMapViewBox|string|An area on the Earth that provides the best map view for this entity. This area is defined as a bounding box in the format of a MULTIPOINT ((WestLongitude SouthLatitude), (EastLongitude NorthLatitude)).|  
|OfficialCulture|string|The culture associated with this entity.|  
|RegionalCulture|string|The approximate population within this entity.|  
|PopulationClass|string|The regional culture associated with this entity.|  
  
 The `Name` class may sometimes be returned for an entity and contain its well-known name. This class has the following properties.  
  
|Name|Type|Description|  
|----------|----------|-----------------|  
|EntityName|string|The name associated with the entity. For example “United States”|  
|Culture|string|The culture in which the name information is in.|  
|SourceID|string|An ID identifying the data provider that supplied the data. This ID number will reference one of the sources listed in the `CopyrightSources` collection.|  
  
 The `Primitive` class contains the polygon information that makes up the boundaries of the entity. This class has the following properties.  
  
|Name|Type|Description|  
|----------|----------|-----------------|  
|PrimativeID|string|A unique ID associated with this polygon primitive.|  
|Shape|string|A comma-delimited sequence starting with the version number of the polygon set followed by a list of compressed polygon “rings” (closed paths represented by sequences of latitude and-longitude points).|  
|NumPoints|string|The number of vertex points used to define the polygon.|  
|SourceID|string|An ID identifying the data provider that supplied the data. This ID number will reference one of the sources listed in the `CopyrightSources` collection.|  
  
 **Common metadata fields**  
  
 When you set the getAllMetadata parameter to true (or 1), entity metadata is returned. The following are common metadata fields that may be returned.  
  
||||  
|-|-|-|  
|**Metadata Field**|**Type**|**Description**|  
|BestMapViewBox|string|An area on the Earth that provides the best map view for this entity. This area is defined as a bounding box in the format of a MULTIPOINT ((WestLongitude SouthLatitude), (EastLongitude NorthLatitude)).|  
|AreaSqKm|double|The approximate total surface area (in square kilometers) covered by all the polygons that comprise this entity.|  
|OfficialCulture|string|The culture associated with this entity.|  
|RegionalCulture|string|The regional culture associated with this entity.|  
|PopulationClass|string|The approximate population within this entity.<br /><br /> **Example**: PopClass20000to99999|  
  
### Decompression Algorithm  
 The point compression algorithm used to generate each compressed polygon ring string is documented in [Point Compression Algorithm](https://msdn.microsoft.com/en-us/library/jj158958.aspx). To retrieve the points that make up the polygon, use the following decompression algorithm.  
  
```csharp
public const string safeCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-";  
  
private static bool TryParseEncodedValue(string value, out List<Location> parsedValue)  
{  
    parsedValue = null;  
    var list = new List<Location>();  
    int index = 0;  
    int xsum = 0, ysum = 0;  
  
    while (index < value.Length)        // While we have more data,  
    {  
        long n = 0;                     // initialize the accumulator  
        int k = 0;                      // initialize the count of bits  
  
        while (true)  
        {  
            if (index >= value.Length)  // If we ran out of data mid-number  
                return false;           // indicate failure.  
  
            int b = safeCharacters.IndexOf(value[index++]);  
  
            if (b == -1)                // If the character wasn't on the valid list,  
                return false;           // indicate failure.  
  
            n |= ((long)b & 31) << k;   // mask off the top bit and append the rest to the accumulator  
            k += 5;                     // move to the next position  
            if (b < 32) break;          // If the top bit was not set, we're done with this number.  
        }  
  
       // The resulting number encodes an x, y pair in the following way:  
       //  
       //  ^ Y  
       //  |  
       //  14  
       //  9 13  
       //  5 8 12  
       //  2 4 7 11  
       //  0 1 3 6 10 ---> X  
  
       // determine which diagonal it's on  
       int diagonal = (int)((Math.Sqrt(8 * n + 5) - 1) / 2);  
  
       // subtract the total number of points from lower diagonals  
       n -= diagonal * (diagonal + 1L) / 2;  
  
       // get the X and Y from what's left over  
       int ny = (int)n;  
       int nx = diagonal - ny;  
  
       // undo the sign encoding  
       nx = (nx >> 1) ^ -(nx & 1);  
        ny = (ny >> 1) ^ -(ny & 1);  
  
        // undo the delta encoding  
        xsum += nx;  
        ysum += ny;  
  
        // position the decimal point  
        list.Add(new Location(ysum * 0.00001, xsum * 0.00001));  
    }  
  
    parsedValue = list;  
    return true;  
}  
  
```  
  
## Examples

**EXAMPLE:** Get polygons that make up the PostCode1 entity that contains the coordinates (47.64054,-122.12934). Metadata is also requested.  
  
```url
https://platform.bing.com/geo/spatial/v1/public/geodata?spatialFilter=GetBoundary(47.64054,-122.12934,1,'PostCode1',1,1,'en','us')&key=BingMapsKey  
```  
  
 URL with ATOM response  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<d:feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:bsi="http://schemas.microsoft.com/bing/spatial/2010/11/odata">  
  <bsi:copyright>© 2013 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.</bsi:copyright>  
  <id>https://platform.bing.com/geo/spatial/v1/public/geodata?spatialFilter=GetBoundary(47.64054,-122.12934,1,'PostCode1',1,1,'en','us')</id>  
  <entry>  
    <id>https://platform.bing.com/geo/spatial/v1/public/geodata?$filter=GetEntity(-37999897300L,1,1,'en','us')</id>  
    <content type="application/xml">  
      <m:property>  
        <d:EntityID m:type="Edm.Int64">-37999897300</d:EntityID>  
        <d:EntityMetadata m:type="Entity.Metadata">  
          <d:BestMapViewBox>MULTIPOINT ((-122.16467 47.6269799), (-122.07723 47.7340119))</d:BestMapViewBox>  
        </d:EntityMetadata>  
        <d:Primitives m:type="Collection(Entity.Primitive)">  
          <d:Primitive m:type="Entity.Primitive">  
            <d:PrimitiveID m:type="Edm.Int64">-37999851053</d:PrimitiveID>  
            <d:Shape>1,4-8vssy_rQpsEwyB-lCyfoN0NmKnlgC84uBwnJl9B2ZxpBrjBqyDingfDF56Ow4QrhEwutBr8H7rDh6e08D  
6wY4EI91hGshd8miC2zyEikGpmnCp5iCFn2lCgxBBFs5Cr81G1ljEgkBuEDFxpDBj9Y88iGv_wFkqBgRFl6EFz8B5KFkZo  
GBvtBw6CihH8nalrsxBsmK51B13CFy7P25DwUxFvF4GxF4GuEnIhPlTwzChvCquL9pY3hE7gGqa8rB5cm9DCFxqIy-EtLwmBum  
B2RM-0iB4tb93CF12B0qCD3vBu6Bo ...  
            </d:Shape>  
        <d:NumPoints m:type="Edm.Int64">6210</d:NumPoints>  
            <d:SourceID m:type="Edm.Byte">8</d:SourceID>  
          </d:Primitive>  
        </d:Primitives>  
        <d:Copyright m:type="Entity.Copyright">  
          <d:CopyrightURL>http://windows.microsoft.com/en-us/windows-live/about-bing-data-suppliers</d:CopyrightURL>  
          <d:Sources m:type="Collection(Entity.Copyright.Source)">  
            <d:Source m:type="Entity.Copyright.Source">  
              <d:SourceID m:type="Edm.Byte">8</d:SourceID>  
              <d:SourceName>TOM</d:SourceName>  
              <d:Copyright></d:Copyright>  
            </d:Source>  
          </d:Sources>  
        </d:Copyright>  
      </m:property>  
    </content>  
  </entry>  
</d:feed>  
```  
  
 URL with JSON response  
  
```json
{  
   "d":{  
      "Copyright":"\u00a9 2013 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https:\/\/platform.bing.com\/geo\/spatial\/v1\/public\/geodata?$filter=GetEntity(-37999897300L,1,1,'en','us')"  
            },  
            "EntityID":"-37999897300",  
            "EntityMetadata":{  
               "BestMapViewBox":"MULTIPOINT ((-122.16467 47.6269799), (-122.07723 47.7340119))"  
            },  
            "Primitives":[  
               {  
                  "PrimitiveID":"-37999851053",  
                  "Shape":"1,4-8vssy_rQpsEwyB-lCyfoN0NmKnlgC84uBwnJl9B2ZxpBrjBqyDingfDF56Ow4QrhEwutBr8H7rDh6e08D  
6wY4EI91hGshd8miC2zyEikGpmnCp5iCFn2lCgxBBFs5Cr81G1ljEgkBuEDFxpDBj9Y88iGv_wFkqBgRFl6EFz8B5KFkZo  
GBvtBw6CihH8nalrsxBsmK51B13CFy7P25DwUxFvF4GxF4GuEnIhPlTwzChvCquL9pY3hE7gGqa8rB5cm9DCFxqIy-EtLwmBum  
B2RM-0iB4tb93CF12B0qCD3vBu6Bo ...  
",  
                  "NumPoints":"6210",  
                  "SourceID":"8"  
               }  
            ],  
            "Copyright":{  
               "CopyrightURL":"http:\/\/windows.microsoft.com\/en-us\/windows-live\/about-bing-data-suppliers",  
               "Sources":[  
                  {  
                     "SourceID":"8",  
                     "SourceName":"TOM",  
                     "Copyright":""  
                  }  
               ]  
            }  
         }  
      ]  
   }  
}  
```  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<d:feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:bsi="http://schemas.microsoft.com/bing/spatial/2010/11/odata">  
  <bsi:copyright>© 2013 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.</bsi:copyright>  
  <id>https://platform.bing.com/geo/spatial/v1/public/geodata?spatialFilter=GetBoundary(47.64054,-122.12934,1,'PostCode1',1,1,'en','us')</id>  
  <entry>  
    <id>https://platform.bing.com/geo/spatial/v1/public/geodata?$filter=GetEntity(-37999897300L,1,1,'en','us')</id>  
    <content type="application/xml">  
      <m:property>  
        <d:EntityID m:type="Edm.Int64">-37999897300</d:EntityID>  
        <d:EntityMetadata m:type="Entity.Metadata">  
          <d:BestMapViewBox>MULTIPOINT ((-122.16467 47.6269799), (-122.07723 47.7340119))</d:BestMapViewBox>  
        </d:EntityMetadata>  
        <d:Primitives m:type="Collection(Entity.Primitive)">  
          <d:Primitive m:type="Entity.Primitive">  
            <d:PrimitiveID m:type="Edm.Int64">-37999851053</d:PrimitiveID>  
            <d:Shape>1,4-8vssy_rQpsEwyB-lCyfoN0NmKnlgC84uBwnJl9B2ZxpBrjBqyDingfDF56Ow4QrhEwutBr8H7rDh6e08D6wY4EI91hGshd8miC2zyEikGpmnCp5iCFn2lCgxBBFs5Cr81G1ljEgkBuEDFxpDBj9Y88iGv_wFkqBgRFl6EFz8B5KFkZoGBvtBw6CihH8nalrsxBsmK51B13CFy7P25DwUxFvF4GxF4GuEnIhPlTwzChvCquL9pY3hE7gGqa8rB5cm9DCFxqIy-EtLwmBumB2RM-0iB4tb93CF12B0qCD3vBu6BosB4lB7Xk3J81Gq_Sn9GkuR8ZumE45B9-FuElrIpsE91Bz9Bl7Hp7UlrH7-FFw0HqgF1iDg7CykEyuYmw5C2_9B5vhCx8B92RBrgB24uB74bDF9KlcwG7mF0tFx2CwgCF50BhWhWyPhb_uQ_nU_LnkXi4D32HloD72HgMs7EnkQkqnBppE14GixGm6T-BF6xYqE4zBhI4xEp1hB_lE5_FpD8zBu-XCF50eqqbDFtx5GOmpGFByla249Dq6Tx3D-zgByzYr6U4q7CirBxrEp0gB3PdDFh_6EFB7tgBsyX1gBlWnWxgB-sB9zBu0Ky-G-sP29RrhFg_dqB4C-BqB9B2C0C7B0CXvDtD12eix-B_nNDFl9J8eFB8iElmIljHtpCwpB9sBjbrKujG0YxgBq_hC0ktBhOv6mBviEyaxvB5XwrC02I9HmBtuH3tMw7FihODF99BhpBFl6EFB7jMhWlWkGkoCF8DixDgawxOn4E3uBnlFvXxOrFo0Q6pCjL3Ox9BpluBjhPsBmyD47pC5OvF8UuwLDy8W4Mpc3jzBDF2mNpqD17tBFBs-sBg9hBy_hC8hK6q8Bk8fvxbtsPi-Bk-Bp1WusUzPjM_gB7P3P1OilBw9gClIF4JFhCsGFzK4jEswC43D63D0wBzbyegpC30DFqMFrsCvBn0N6iM5-YwGyVzlCFD5LFzpDpdF1sDorFDFB8kVgyDZ7O-xF8xEssgB5sYy7CjiBD4JF1LFqkDg2KupLzkCyNziB6GuE-tCjgE_jMr-G4oWrnCihC66D8jHv9BgnKMsarP9K87CDnvBFweqgC30lCw4D0hJBnpE6CnPvL_Z2lDr1D92C72C47Cg8CyyCrlCx6LrjDD-FuC3OmV7X2JrXllChTn2BkNFx_BxTjXthBFr8B7WkH1FxsEF-sBnkMm9eyxX10CvrK-Ce-EBtvawuC5GsD8SmLrEuFrEsDqDpEsF5EpmB8hKtsPhWonU-ajjCk-BxrCs3B4DPWcLh_GtI0E2zCFBF3NgMpHnK_FnK_FlK_H_HgL5E5E7ErHkGkGmGmMvK-NmGkGkG9EpK4IhW4SBssE6uB56DgwKo1LnrBBxhChV2OwwG1iEDl_hCpnFq0CpYvdgwLn2Nbu5QljB6wR1iEBF0uE2d03Ey1By0F34Mv7BvHgJB8r9B4v8Bp9tCtPj_iBsyHx2xD-rJDFFBgvI2lzByY3_4Brh1Bm-BjbpWBCh3xCyD3CjHnE9wE6Dy2Nw83D0dwnC-9Dz8FxK_PixBuUj0DqQyZxwX9vJmHrOlFqsVkHq3GBFjtBwwCltekMwoRBB-Z9myBL5MiL2SCBxG0DkY2F8cgTwDtEyF3GsDpE1GsFupBBC2BB2BDlErCDhED2ZgPBECSSCnUk1kBkYmjBolR0BtQrMnG7vE4gB3P6EowGsr7F5xH-yE63D3nJ_8hB5nhCn7BCBv4mLr0Ct0EspBv0E2wrBprBjV3pEB0nC0P1sa3xEhwD_hBpjS0_3BojBijE4IwmmBh0B-wnB6oGnuBv1Ws2I69CFB6l1JljBBFwm3H605Br2mBvCiCPiE1KzHFkgCqqBsuDz67BokPlkC14eDr0SlvBpI0_NszEsVrXlwBq9DDgfVq5B3T8yD2NDwJzwSFFjSkJkE6C3F9uCFBFkCjD4x7F_iK6IB8BxCgGuwG4DsFqDsDqDrEiIxJ9MiIzJiI7jH10a8tOr2CjiBDFlYBFB4SpEvJ4SyO7C-ew1B3MxQz0EsYpmB-azNnHsYrgBrmB0dB6SlKs3B-Vz0ErgBI9EzRpmB8vCi-Bl9DyPrgBqjB6iDpmBmwBrgBs3BslR_vC9tVl7BqjB6D4Sc4B5EojBBj6Bj8BFB8iEl7BBCCtxBk7Mw4Uh5gC5oClvD2-DrnJ07OmgD-iJxoE6nBxGCDgwD85pD75gD_5fq7dq17DgvJtq_BmtIy8rE519QqPiYxRiCpmB9aydxRGzN-VyP7CkC8LnK3N0PyPnkMnjC6TpHzNnKC9alhCvlDq8O8hB_HpmBupBnyDs2NCB1M_tIuO2hBoOliI1zBiCBsDCvEwDC6FmD1pF2o5Bz5BpSBmxNC3E2iEvjMlECpZlE-zGrpCoccBlB4BBC6H6sDqYJUjBjKtCtCx3Gy6E-lIj9DClpG6vCswGklRlyD__BnEr0Cy3DpgBnEm2NrJ_4CqFCD9H9uW3BgiI76ExluBqpG6mNjmmDCD1tConVs-wJD8Mg1G02cCxqR_xtEzMrCmuB_pDmDRj4G1jSo6LyPrvV71Ek4BlonC8-BiqBn1CuvE6dBtBgLB9MkIoLzyBgT5GuXmoBCC0Zs7B_rCqK95CxwQlMuzcutBhoC5jB_Rw0B6WlEpyB43BBk8G7ocvhBFBp4XpE70J7qFwGqQnhEDFBBmuCzCBC0B6kCjvDCyHzxBplE6HynBvGynB-5DlElElEvGnJlEmDnEoF6HxGurE4hB3mPvGv0EqYnpCnEqFo3B4hBglCuPg0f7iHjyCppC1lEwO_8R1MspBwO8H6H2B0B2BjBrCoDoDoDqFwrOwO3nDmhPqqD1sBqnF_-D5UkuI_KDChLxO84J3a6hB03DEmowBrECBCDl5Ck7BsH7nB43Gv1B9H_2BC1jP2-DCDh9Bi4FzrOrqD32C59EguI9rf3z3BhyHxZCD043Ex65DpDpD_5-Bu-1BDijsBmu2DstmB1S6mN3S0Gv5nBCDrFvqlBC2vCsrEiCCBxqFkc8H8HjBoD7xB_9H0_IknC7VkXvR8H2BmD8HrJzkBjpCsuBu8M2BpJzM8KtQiXuOkchrB2nB3wOs3E-sUwOr4KuO4nB-qBw2C-iCi-Gmc1lE-iC86xBtCg3R13GqF7iH8sDr0J8K_KkXjwLmDvsBiqIrB6nB9e60Dm7ahKzkBkXwOkXzzBlmK8HnmBmc4iEy3DJJCjB5U9e13G2hB3kBmjBrJp7FoD5zU0TCDuCrFkyCu7Cx1B9HyGzlYzoM-0L32CtqDgiIpDMvFkB5hB3tCDg8Czck8CXD_GxFmlBmVzX3coViNqVsVoarvBuVjPkRjPxLqNnPDFgKvIrP1L4VtiDkgB0Eya0V4lB-cxDMwEviBxoBuEFxLoB6G2rB8Q9OxrI6GxF34EtD6G2hCpL8nK-StoBX-HufrtJqlBz8Ul7xD2J85B8Qq8C39B_yCgzC1zrBq8C7lCknGuEsEFhxK7OmrlCpLD3cufkawfslBtiBDp2B8gM_mExjpC6G_9Ns2JqV5c_rkBma-O-O99Bu2QlIzF6rBxoBlvB4rBp2Bg6Bw8CvrDsmDmarL-OjT6rBt2BpvBwlB5uC-9B5uCoaiNtLoB6JkRxL5FvIOhChCF6CnFkEuG-7lB52CgxOxoMv3MogDCz_L5UurEhrB7gOw1WiqI44b1kB80DwOrBD2BjBj9DgxN3lG59ClmKxGtGjEtGvG8FnEspBiwB3U8H6KCkFs6kCCnvDkvKzVByIjB3kBWxrCwjBBBCgXk5kB80LppC4hB8HCz4D4pECM52BnnC8mlClrqB2M0qF--DpqpCDFwZ_4Bw3F3tMY1Vl0CogDCDsvclkFh6HvwG8iHk6-BpwBhLwQrqD9_Ik2HvqHwyHxqByHDgD7D9d8sBD_as2OoHiWqHuKwKD</d:Shape>  
            <d:NumPoints m:type="Edm.Int64">6210</d:NumPoints>  
            <d:SourceID m:type="Edm.Byte">8</d:SourceID>  
          </d:Primitive>  
        </d:Primitives>  
        <d:Copyright m:type="Entity.Copyright">  
          <d:CopyrightURL>http://windows.microsoft.com/en-us/windows-live/about-bing-data-suppliers</d:CopyrightURL>  
          <d:Sources m:type="Collection(Entity.Copyright.Source)">  
            <d:Source m:type="Entity.Copyright.Source">  
              <d:SourceID m:type="Edm.Byte">8</d:SourceID>  
              <d:SourceName>TOM</d:SourceName>  
              <d:Copyright></d:Copyright>  
            </d:Source>  
          </d:Sources>  
        </d:Copyright>  
      </m:property>  
    </content>  
  </entry>  
</d:feed>  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../spatial-data-services/status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   401  
  
-   500  
  
-   503