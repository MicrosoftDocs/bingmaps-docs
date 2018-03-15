---
title: "JSON Data Contracts | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7f2270bd-9427-42ec-8b6f-e10b2d1bf234
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# JSON Data Contracts
> [!IMPORTANT]
>  Update: Since writing this documentation the Bing Maps team has released an open source portable class library which makes it easy to access the Bing Maps REST services from any .NET application. You can find this library on GitHub              [here](https://github.com/Microsoft/BingMapsRESTToolkit/). Going forward the data contracts on this page will no longer be updated. Please refer to the .NET REST Toolkit for the latest JSON contrcts.  
  
 The following data contracts include classes for all Bing Maps REST Services. For examples of how to use these data contracts, see [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md).  
  
## Data Contracts  
  
### C# Data Contracts  
  
```csharp  
using System.Runtime.Serialization;  
  
namespace BingMapsRESTService.Common.JSON  
{  
    [DataContract]  
    public class Address  
    {  
        [DataMember(Name = "addressLine", EmitDefaultValue = false)]  
        public string AddressLine { get; set; }  
  
        [DataMember(Name = "adminDistrict", EmitDefaultValue = false)]  
        public string AdminDistrict { get; set; }  
  
        [DataMember(Name = "adminDistrict2", EmitDefaultValue = false)]  
        public string AdminDistrict2 { get; set; }  
  
        [DataMember(Name = "countryRegion", EmitDefaultValue = false)]  
        public string CountryRegion { get; set; }  
  
        [DataMember(Name = "countryRegionIso2", EmitDefaultValue = false)]  
        public string CountryRegionIso2 { get; set; }  
  
        [DataMember(Name = "formattedAddress", EmitDefaultValue = false)]  
        public string FormattedAddress { get; set; }  
  
        [DataMember(Name = "locality", EmitDefaultValue = false)]  
        public string Locality { get; set; }  
  
        [DataMember(Name = "postalCode", EmitDefaultValue = false)]  
        public string PostalCode { get; set; }  
  
        [DataMember(Name = "neighborhood", EmitDefaultValue = false)]  
        public string Neighborhood { get; set; }  
  
        [DataMember(Name = "landmark", EmitDefaultValue = false)]  
        public string Landmark { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class BirdseyeMetadata : ImageryMetadata  
    {  
        [DataMember(Name = "orientation", EmitDefaultValue = false)]  
        public double Orientation { get; set; }  
  
        [DataMember(Name = "tilesX", EmitDefaultValue = false)]  
        public int TilesX { get; set; }  
  
        [DataMember(Name = "tilesY", EmitDefaultValue = false)]  
        public int TilesY { get; set; }  
    }  
  
    [DataContract]  
    public class BoundingBox  
    {  
        [DataMember(Name = "southLatitude", EmitDefaultValue = false)]  
        public double SouthLatitude { get; set; }  
  
        [DataMember(Name = "westLongitude", EmitDefaultValue = false)]  
        public double WestLongitude { get; set; }  
  
        [DataMember(Name = "northLatitude", EmitDefaultValue = false)]  
        public double NorthLatitude { get; set; }  
  
        [DataMember(Name = "eastLongitude", EmitDefaultValue = false)]  
        public double EastLongitude { get; set; }  
    }  
  
    [DataContract]  
    public class Detail  
    {  
        [DataMember(Name = "compassDegrees", EmitDefaultValue = false)]  
        public int CompassDegrees { get; set; }  
  
        [DataMember(Name = "maneuverType", EmitDefaultValue = false)]  
        public string ManeuverType { get; set; }  
  
        [DataMember(Name = "startPathIndices", EmitDefaultValue = false)]  
        public int[] StartPathIndices { get; set; }  
  
        [DataMember(Name = "endPathIndices", EmitDefaultValue = false)]  
        public int[] EndPathIndices { get; set; }  
  
        [DataMember(Name = "roadType", EmitDefaultValue = false)]  
        public string RoadType { get; set; }  
  
        [DataMember(Name = "locationCodes", EmitDefaultValue = false)]  
        public string[] LocationCodes { get; set; }  
  
        [DataMember(Name = "names", EmitDefaultValue = false)]  
        public string[] Names { get; set; }  
  
        [DataMember(Name = "mode", EmitDefaultValue = false)]  
        public string Mode { get; set; }  
  
        [DataMember(Name = "roadShieldRequestParameters", EmitDefaultValue = false)]  
        public RoadShield roadShieldRequestParameters { get; set; }  
    }  
  
    [DataContract]  
    public class Generalization  
    {  
        [DataMember(Name = "pathIndices", EmitDefaultValue = false)]  
        public int[] PathIndices { get; set; }  
  
        [DataMember(Name = "latLongTolerance", EmitDefaultValue = false)]  
        public double LatLongTolerance { get; set; }  
    }  
  
    [DataContract]  
    public class Hint  
    {  
        [DataMember(Name = "hintType", EmitDefaultValue = false)]  
        public string HintType { get; set; }  
  
        [DataMember(Name = "text", EmitDefaultValue = false)]  
        public string Text { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    [KnownType(typeof(StaticMapMetadata))]  
    [KnownType(typeof(BirdseyeMetadata))]  
    public class ImageryMetadata : Resource  
    {  
        [DataMember(Name = "imageHeight", EmitDefaultValue = false)]  
        public string ImageHeight { get; set; }  
  
        [DataMember(Name = "imageWidth", EmitDefaultValue = false)]  
        public string ImageWidth { get; set; }  
  
        [DataMember(Name = "imageUrl", EmitDefaultValue = false)]  
        public string ImageUrl { get; set; }  
  
        [DataMember(Name = "imageUrlSubdomains", EmitDefaultValue = false)]  
        public string[] ImageUrlSubdomains { get; set; }  
  
        [DataMember(Name = "vintageEnd", EmitDefaultValue = false)]  
        public string VintageEnd { get; set; }  
  
        [DataMember(Name = "vintageStart", EmitDefaultValue = false)]  
        public string VintageStart { get; set; }  
  
        [DataMember(Name = "zoomMax", EmitDefaultValue = false)]  
        public int ZoomMax { get; set; }  
  
        [DataMember(Name = "zoomMin", EmitDefaultValue = false)]  
        public int ZoomMin { get; set; }  
    }  
  
    [DataContract]  
    public class Instruction  
    {  
        [DataMember(Name = "maneuverType", EmitDefaultValue = false)]  
        public string ManeuverType { get; set; }  
  
        [DataMember(Name = "text", EmitDefaultValue = false)]  
        public string Text { get; set; }  
    }  
  
    [DataContract]  
    public class ItineraryItem  
    {  
        [DataMember(Name = "childItineraryItems", EmitDefaultValue = false)]  
        public ItineraryItem[] ChildItineraryItems { get; set; }  
  
        [DataMember(Name = "compassDirection", EmitDefaultValue = false)]  
        public string CompassDirection { get; set; }  
  
        [DataMember(Name = "details", EmitDefaultValue = false)]  
        public Detail[] Details { get; set; }  
  
        [DataMember(Name = "exit", EmitDefaultValue = false)]  
        public string Exit { get; set; }  
  
        [DataMember(Name = "hints", EmitDefaultValue = false)]  
        public Hint[] Hints { get; set; }  
  
        [DataMember(Name = "iconType", EmitDefaultValue = false)]  
        public string IconType { get; set; }  
  
        [DataMember(Name = "instruction", EmitDefaultValue = false)]  
        public Instruction Instruction { get; set; }  
  
        [DataMember(Name = "maneuverPoint", EmitDefaultValue = false)]  
        public Point ManeuverPoint { get; set; }  
  
        [DataMember(Name = "sideOfStreet", EmitDefaultValue = false)]  
        public string SideOfStreet { get; set; }  
  
        [DataMember(Name = "signs", EmitDefaultValue = false)]  
        public string[] Signs { get; set; }  
  
        [DataMember(Name = "time", EmitDefaultValue = false)]  
        public string Time { get; set; }  
  
        [DataMember(Name = "tollZone", EmitDefaultValue = false)]  
        public string TollZone { get; set; }  
  
        [DataMember(Name = "towardsRoadName", EmitDefaultValue = false)]  
        public string TowardsRoadName { get; set; }  
  
        [DataMember(Name = "transitLine", EmitDefaultValue = false)]  
        public TransitLine TransitLine { get; set; }  
  
        [DataMember(Name = "transitStopId", EmitDefaultValue = false)]  
        public int TransitStopId { get; set; }  
  
        [DataMember(Name = "transitTerminus", EmitDefaultValue = false)]  
        public string TransitTerminus { get; set; }  
  
        [DataMember(Name = "travelDistance", EmitDefaultValue = false)]  
        public double TravelDistance { get; set; }  
  
        [DataMember(Name = "travelDuration", EmitDefaultValue = false)]  
        public double TravelDuration { get; set; }  
  
        [DataMember(Name = "travelMode", EmitDefaultValue = false)]  
        public string TravelMode { get; set; }  
  
        [DataMember(Name = "warning", EmitDefaultValue = false)]  
        public Warning[] Warning { get; set; }  
    }  
  
    [DataContract]  
    public class Line  
    {  
        [DataMember(Name = "type", EmitDefaultValue = false)]  
        public string Type { get; set; }  
  
        [DataMember(Name = "coordinates", EmitDefaultValue = false)]  
        public double[][] Coordinates { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class Location : Resource  
    {  
        [DataMember(Name = "name", EmitDefaultValue = false)]  
        public string Name { get; set; }  
  
        [DataMember(Name = "point", EmitDefaultValue = false)]  
        public Point Point { get; set; }  
  
        [DataMember(Name = "entityType", EmitDefaultValue = false)]  
        public string EntityType { get; set; }  
  
        [DataMember(Name = "address", EmitDefaultValue = false)]  
        public Address Address { get; set; }  
  
        [DataMember(Name = "confidence", EmitDefaultValue = false)]  
        public string Confidence { get; set; }  
  
        [DataMember(Name = "matchCodes", EmitDefaultValue = false)]  
        public string[] MatchCodes { get; set; }  
  
        [DataMember(Name = "geocodePoints", EmitDefaultValue = false)]  
        public Point[] GeocodePoints { get; set; }  
  
        [DataMember(Name = "queryParseValues", EmitDefaultValue = false)]  
        public QueryParseValue[] QueryParseValues { get; set; }  
    }  
  
    [DataContract]  
    public class QueryParseValue  
    {  
       [DataMember(Name = "property", EmitDefaultValue = false)]  
        public string Property { get; set; }  
  
       [DataMember(Name = "value", EmitDefaultValue = false)]  
        public string Value { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class PinInfo  
    {  
        [DataMember(Name = "anchor", EmitDefaultValue = false)]  
        public Pixel Anchor { get; set; }  
  
        [DataMember(Name = "bottomRightOffset", EmitDefaultValue = false)]  
        public Pixel BottomRightOffset { get; set; }  
  
        [DataMember(Name = "topLeftOffset", EmitDefaultValue = false)]  
        public Pixel TopLeftOffset { get; set; }  
  
        [DataMember(Name = "point", EmitDefaultValue = false)]  
        public Point Point { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class Pixel  
    {  
        [DataMember(Name = "x", EmitDefaultValue = false)]  
        public string X { get; set; }  
  
        [DataMember(Name = "y", EmitDefaultValue = false)]  
        public string Y { get; set; }  
    }  
  
    [DataContract]  
    public class Point : Shape  
    {  
        [DataMember(Name = "type", EmitDefaultValue = false)]  
        public string Type { get; set; }  
  
        /// <summary>  
        /// Latitude,Longitude  
        /// </summary>  
        [DataMember(Name = "coordinates", EmitDefaultValue = false)]  
        public double[] Coordinates { get; set; }  
  
        [DataMember(Name = "calculationMethod", EmitDefaultValue = false)]  
        public string CalculationMethod { get; set; }  
  
        [DataMember(Name = "usageTypes", EmitDefaultValue = false)]  
        public string[] UsageTypes { get; set; }  
    }  
  
    [DataContract]  
    [KnownType(typeof(Location))]  
    [KnownType(typeof(Route))]  
    [KnownType(typeof(TrafficIncident))]  
    [KnownType(typeof(ImageryMetadata))]  
    [KnownType(typeof(ElevationData))]  
    [KnownType(typeof(SeaLevelData))]      
    [KnownType(typeof(CompressedPointList))]  
    public class Resource  
    {  
        [DataMember(Name = "bbox", EmitDefaultValue = false)]  
        public double[] BoundingBox { get; set; }  
  
        [DataMember(Name = "__type", EmitDefaultValue = false)]  
        public string Type { get; set; }  
    }  
  
    [DataContract]  
    public class ResourceSet  
    {  
        [DataMember(Name = "estimatedTotal", EmitDefaultValue = false)]  
        public long EstimatedTotal { get; set; }  
  
        [DataMember(Name = "resources", EmitDefaultValue = false)]  
        public Resource[] Resources { get; set; }  
    }  
  
    [DataContract]  
    public class Response  
    {  
        [DataMember(Name = "copyright", EmitDefaultValue = false)]  
        public string Copyright { get; set; }  
  
        [DataMember(Name = "brandLogoUri", EmitDefaultValue = false)]  
        public string BrandLogoUri { get; set; }  
  
        [DataMember(Name = "statusCode", EmitDefaultValue = false)]  
        public int StatusCode { get; set; }  
  
        [DataMember(Name = "statusDescription", EmitDefaultValue = false)]  
        public string StatusDescription { get; set; }  
  
        [DataMember(Name = "authenticationResultCode", EmitDefaultValue = false)]  
        public string AuthenticationResultCode { get; set; }  
  
        [DataMember(Name = "errorDetails", EmitDefaultValue = false)]  
        public string[] errorDetails { get; set; }  
  
        [DataMember(Name = "traceId", EmitDefaultValue = false)]  
        public string TraceId { get; set; }  
  
        [DataMember(Name = "resourceSets", EmitDefaultValue = false)]  
        public ResourceSet[] ResourceSets { get; set; }  
    }  
  
    [DataContract]  
    public class RoadShield  
    {  
        [DataMember(Name = "bucket", EmitDefaultValue = false)]  
        public int Bucket { get; set; }  
  
        [DataMember(Name = "shields", EmitDefaultValue = false)]  
        public Shield[] Shields { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class Route : Resource  
    {  
        [DataMember(Name = "id", EmitDefaultValue = false)]  
        public string Id { get; set; }  
  
        [DataMember(Name = "distanceUnit", EmitDefaultValue = false)]  
        public string DistanceUnit { get; set; }  
  
        [DataMember(Name = "durationUnit", EmitDefaultValue = false)]  
        public string DurationUnit { get; set; }  
  
        [DataMember(Name = "travelDistance", EmitDefaultValue = false)]  
        public double TravelDistance { get; set; }  
  
        [DataMember(Name = "travelDuration", EmitDefaultValue = false)]  
        public double TravelDuration { get; set; }  
  
        [DataMember(Name = "routeLegs", EmitDefaultValue = false)]  
        public RouteLeg[] RouteLegs { get; set; }  
  
        [DataMember(Name = "routePath", EmitDefaultValue = false)]  
        public RoutePath RoutePath { get; set; }  
    }  
  
    [DataContract]  
    public class RouteLeg  
    {  
        [DataMember(Name = "travelDistance", EmitDefaultValue = false)]  
        public double TravelDistance { get; set; }  
  
        [DataMember(Name = "travelDuration", EmitDefaultValue = false)]  
        public double TravelDuration { get; set; }  
  
        [DataMember(Name = "actualStart", EmitDefaultValue = false)]  
        public Point ActualStart { get; set; }  
  
        [DataMember(Name = "actualEnd", EmitDefaultValue = false)]  
        public Point ActualEnd { get; set; }  
  
        [DataMember(Name = "startLocation", EmitDefaultValue = false)]  
        public Location StartLocation { get; set; }  
  
        [DataMember(Name = "endLocation", EmitDefaultValue = false)]  
        public Location EndLocation { get; set; }  
  
        [DataMember(Name = "itineraryItems", EmitDefaultValue = false)]  
        public ItineraryItem[] ItineraryItems { get; set; }  
    }  
  
    [DataContract]  
    public class RoutePath  
    {  
        [DataMember(Name = "line", EmitDefaultValue = false)]  
        public Line Line { get; set; }  
  
        [DataMember(Name = "generalizations", EmitDefaultValue = false)]  
        public Generalization[] Generalizations { get; set; }  
    }  
  
    [DataContract]  
    [KnownType(typeof(Point))]  
    public class Shape  
    {  
        [DataMember(Name = "boundingBox", EmitDefaultValue = false)]  
        public double[] BoundingBox { get; set; }  
    }  
  
    [DataContract]  
    public class Shield  
    {  
        [DataMember(Name = "labels", EmitDefaultValue = false)]  
        public string[] Labels { get; set; }  
  
        [DataMember(Name = "roadShieldType", EmitDefaultValue = false)]  
        public int RoadShieldType { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class StaticMapMetadata : ImageryMetadata  
    {  
        [DataMember(Name = "mapCenter", EmitDefaultValue = false)]  
        public Point MapCenter { get; set; }  
  
        [DataMember(Name = "pushpins", EmitDefaultValue = false)]  
        public PinInfo[] Pushpins { get; set; }  
  
        [DataMember(Name = "zoom", EmitDefaultValue = false)]  
        public string Zoom { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class TrafficIncident : Resource  
    {  
        [DataMember(Name = "point", EmitDefaultValue = false)]  
        public Point Point { get; set; }  
  
        [DataMember(Name = "congestion", EmitDefaultValue = false)]  
        public string Congestion { get; set; }  
  
        [DataMember(Name = "description", EmitDefaultValue = false)]  
        public string Description { get; set; }  
  
        [DataMember(Name = "detour", EmitDefaultValue = false)]  
        public string Detour { get; set; }  
  
        [DataMember(Name = "start", EmitDefaultValue = false)]  
        public string Start { get; set; }  
  
        [DataMember(Name = "end", EmitDefaultValue = false)]  
        public string End { get; set; }  
  
        [DataMember(Name = "incidentId", EmitDefaultValue = false)]  
        public long IncidentId { get; set; }  
  
        [DataMember(Name = "lane", EmitDefaultValue = false)]  
        public string Lane { get; set; }  
  
        [DataMember(Name = "lastModified", EmitDefaultValue = false)]  
        public string LastModified { get; set; }  
  
        [DataMember(Name = "roadClosed", EmitDefaultValue = false)]  
        public bool RoadClosed { get; set; }  
  
        [DataMember(Name = "severity", EmitDefaultValue = false)]  
        public int Severity { get; set; }  
  
        [DataMember(Name = "toPoint", EmitDefaultValue = false)]  
        public Point ToPoint { get; set; }  
  
        [DataMember(Name = "locationCodes", EmitDefaultValue = false)]  
        public string[] LocationCodes { get; set; }  
  
        [DataMember(Name = "type", EmitDefaultValue = false)]  
        public int Type { get; set; }  
  
        [DataMember(Name = "verified", EmitDefaultValue = false)]  
        public bool Verified { get; set; }  
    }  
  
    [DataContract]  
    public class TransitLine  
    {  
        [DataMember(Name = "verboseName", EmitDefaultValue = false)]  
        public string verboseName { get; set; }  
  
        [DataMember(Name = "abbreviatedName", EmitDefaultValue = false)]  
        public string abbreviatedName { get; set; }  
  
        [DataMember(Name = "agencyId", EmitDefaultValue = false)]  
        public long AgencyId { get; set; }  
  
        [DataMember(Name = "agencyName", EmitDefaultValue = false)]  
        public string agencyName { get; set; }  
  
        [DataMember(Name = "lineColor", EmitDefaultValue = false)]  
        public long lineColor { get; set; }  
  
        [DataMember(Name = "lineTextColor", EmitDefaultValue = false)]  
        public long lineTextColor { get; set; }  
  
        [DataMember(Name = "uri", EmitDefaultValue = false)]  
        public string uri { get; set; }  
  
        [DataMember(Name = "phoneNumber", EmitDefaultValue = false)]  
        public string phoneNumber { get; set; }  
  
        [DataMember(Name = "providerInfo", EmitDefaultValue = false)]  
        public string providerInfo { get; set; }  
    }  
  
    [DataContract]  
    public class Warning  
    {  
        [DataMember(Name = "warningType", EmitDefaultValue = false)]  
        public string WarningType { get; set; }  
  
        [DataMember(Name = "severity", EmitDefaultValue = false)]  
        public string Severity { get; set; }  
  
        [DataMember(Name = "text", EmitDefaultValue = false)]  
        public string Text { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class CompressedPointList : Resource  
    {  
        [DataMember(Name = "value", EmitDefaultValue = false)]  
        public string Value { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class ElevationData : Resource  
    {  
        [DataMember(Name = "elevations", EmitDefaultValue = false)]  
        public int[] Elevations { get; set; }  
  
        [DataMember(Name = "zoomLevel", EmitDefaultValue = false)]  
        public int ZoomLevel { get; set; }  
    }  
  
    [DataContract(Namespace = "http://schemas.microsoft.com/search/local/ws/rest/v1")]  
    public class SeaLevelData : Resource  
    {  
        [DataMember(Name = "offsets", EmitDefaultValue = false)]  
        public int[] Offsets { get; set; }  
  
        [DataMember(Name = "zoomLevel", EmitDefaultValue = false)]  
        public int ZoomLevel { get; set; }  
    }  
}  
```  
  
### Visual Basic Data Contracts  
  
```vb  
Imports System.Runtime.Serialization  
  
Namespace BingMapsRESTService.Common.JSON  
    <DataContract()> _  
    Public Class Address  
        <DataMember(Name:="addressLine", EmitDefaultValue:=False)> _  
        Public Property AddressLine() As String  
  
        <DataMember(Name:="adminDistrict", EmitDefaultValue:=False)> _  
        Public Property AdminDistrict() As String  
  
        <DataMember(Name:="adminDistrict2", EmitDefaultValue:=False)> _  
        Public Property AdminDistrict2() As String  
  
        <DataMember(Name:="countryRegion", EmitDefaultValue:=False)> _  
        Public Property CountryRegion() As String  
  
        <DataMember(Name:="countryRegionIso2", EmitDefaultValue:=False)> _  
        Public Property CountryRegionIso2() As String  
  
        <DataMember(Name:="formattedAddress", EmitDefaultValue:=False)> _  
        Public Property FormattedAddress() As String  
  
        <DataMember(Name:="locality", EmitDefaultValue:=False)> _  
        Public Property Locality() As String  
  
        <DataMember(Name:="postalCode", EmitDefaultValue:=False)> _  
        Public Property PostalCode() As String  
  
        <DataMember(Name:="neighborhood", EmitDefaultValue:=False)> _  
        Public Property Neighborhood() As String  
  
        <DataMember(Name:="landmark", EmitDefaultValue:=False)> _  
        Public Property Landmark() As String  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class BirdseyeMetadata  
        Inherits ImageryMetadata  
        <DataMember(Name:="orientation", EmitDefaultValue:=False)> _  
        Public Property Orientation() As Double  
  
        <DataMember(Name:="tilesX", EmitDefaultValue:=False)> _  
        Public Property TilesX() As Integer  
  
        <DataMember(Name:="tilesY", EmitDefaultValue:=False)> _  
        Public Property TilesY() As Integer  
    End Class  
  
    <DataContract()> _  
    Public Class BoundingBox  
        <DataMember(Name:="southLatitude", EmitDefaultValue:=False)> _  
        Public Property SouthLatitude() As Double  
  
        <DataMember(Name:="westLongitude", EmitDefaultValue:=False)> _  
        Public Property WestLongitude() As Double  
  
        <DataMember(Name:="northLatitude", EmitDefaultValue:=False)> _  
        Public Property NorthLatitude() As Double  
  
        <DataMember(Name:="eastLongitude", EmitDefaultValue:=False)> _  
        Public Property EastLongitude() As Double  
    End Class  
  
    <DataContract()> _  
    Public Class Detail  
        <DataMember(Name:="compassDegrees", EmitDefaultValue:=False)> _  
        Public Property CompassDegrees() As Integer  
  
        <DataMember(Name:="maneuverType", EmitDefaultValue:=False)> _  
        Public Property ManeuverType() As String  
  
        <DataMember(Name:="startPathIndices", EmitDefaultValue:=False)> _  
        Public Property StartPathIndices() As Integer()  
  
        <DataMember(Name:="endPathIndices", EmitDefaultValue:=False)> _  
        Public Property EndPathIndices() As Integer()  
  
        <DataMember(Name:="roadType", EmitDefaultValue:=False)> _  
        Public Property RoadType() As String  
  
        <DataMember(Name:="locationCodes", EmitDefaultValue:=False)> _  
        Public Property LocationCodes() As String()  
  
        <DataMember(Name:="names", EmitDefaultValue:=False)> _  
        Public Property Names() As String()  
  
        <DataMember(Name:="mode", EmitDefaultValue:=False)> _  
        Public Property Mode() As String  
  
        <DataMember(Name:="roadShieldRequestParameters", EmitDefaultValue:=False)> _  
        Public Property roadShieldRequestParameters() As RoadShield  
    End Class  
  
    <DataContract()> _  
    Public Class Generalization  
        <DataMember(Name:="pathIndices", EmitDefaultValue:=False)> _  
        Public Property PathIndices() As Integer()  
  
        <DataMember(Name:="latLongTolerance", EmitDefaultValue:=False)> _  
        Public Property LatLongTolerance() As Double  
    End Class  
  
    <DataContract()> _  
    Public Class Hint  
        <DataMember(Name:="hintType", EmitDefaultValue:=False)> _  
        Public Property HintType() As String  
  
        <DataMember(Name:="text", EmitDefaultValue:=False)> _  
        Public Property Text() As String  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    <KnownType(GetType(StaticMapMetadata))> _  
    <KnownType(GetType(BirdseyeMetadata))> _  
    Public Class ImageryMetadata  
        Inherits Resource  
        <DataMember(Name:="imageHeight", EmitDefaultValue:=False)> _  
        Public Property ImageHeight() As String  
  
        <DataMember(Name:="imageWidth", EmitDefaultValue:=False)> _  
        Public Property ImageWidth() As String  
  
        <DataMember(Name:="imageUrl", EmitDefaultValue:=False)> _  
        Public Property ImageUrl() As String  
  
        <DataMember(Name:="imageUrlSubdomains", EmitDefaultValue:=False)> _  
        Public Property ImageUrlSubdomains() As String()  
  
        <DataMember(Name:="vintageEnd", EmitDefaultValue:=False)> _  
        Public Property VintageEnd() As String  
  
        <DataMember(Name:="vintageStart", EmitDefaultValue:=False)> _  
        Public Property VintageStart() As String  
  
        <DataMember(Name:="zoomMax", EmitDefaultValue:=False)> _  
        Public Property ZoomMax() As Integer  
  
        <DataMember(Name:="zoomMin", EmitDefaultValue:=False)> _  
        Public Property ZoomMin() As Integer  
    End Class  
  
    <DataContract()> _  
    Public Class Instruction  
        <DataMember(Name:="maneuverType", EmitDefaultValue:=False)> _  
        Public Property ManeuverType() As String  
  
        <DataMember(Name:="text", EmitDefaultValue:=False)> _  
        Public Property Text() As String  
    End Class  
  
    <DataContract()> _  
    Public Class ItineraryItem  
        <DataMember(Name:="childItineraryItems", EmitDefaultValue:=False)> _  
        Public Property ChildItineraryItems() As ItineraryItem  
  
        <DataMember(Name:="compassDirection", EmitDefaultValue:=False)> _  
        Public Property CompassDirection() As String  
  
        <DataMember(Name:="details", EmitDefaultValue:=False)> _  
        Public Property Details() As Detail()  
  
        <DataMember(Name:="exit", EmitDefaultValue:=False)> _  
        Public Property [Exit]() As String  
  
        <DataMember(Name:="hints", EmitDefaultValue:=False)> _  
        Public Property Hints() As Hint()  
  
        <DataMember(Name:="iconType", EmitDefaultValue:=False)> _  
        Public Property IconType() As String  
  
        <DataMember(Name:="instruction", EmitDefaultValue:=False)> _  
        Public Property Instruction() As Instruction  
  
        <DataMember(Name:="maneuverPoint", EmitDefaultValue:=False)> _  
        Public Property ManeuverPoint() As Point  
  
        <DataMember(Name:="sideOfStreet", EmitDefaultValue:=False)> _  
        Public Property SideOfStreet() As String  
  
        <DataMember(Name:="signs", EmitDefaultValue:=False)> _  
        Public Property Signs() As String()  
  
        <DataMember(Name:="time", EmitDefaultValue:=False)> _  
        Public Property Time() As String  
  
        <DataMember(Name:="tollZone", EmitDefaultValue:=False)> _  
        Public Property TollZone() As String  
  
        <DataMember(Name:="towardsRoadName", EmitDefaultValue:=False)> _  
        Public Property TowardsRoadName() As String  
  
        <DataMember(Name:="transitLine", EmitDefaultValue:=False)> _  
        Public Property TransitLine() As TransitLine  
  
        <DataMember(Name:="transitStopId", EmitDefaultValue:=False)> _  
        Public Property TransitStopId() As Integer  
  
        <DataMember(Name:="transitTerminus", EmitDefaultValue:=False)> _  
        Public Property TransitTerminus() As String  
  
        <DataMember(Name:="travelDistance", EmitDefaultValue:=False)> _  
        Public Property TravelDistance() As Double  
  
        <DataMember(Name:="travelDuration", EmitDefaultValue:=False)> _  
        Public Property TravelDuration() As Double  
  
        <DataMember(Name:="travelMode", EmitDefaultValue:=False)> _  
        Public Property TravelMode() As String  
  
        <DataMember(Name:="warning", EmitDefaultValue:=False)> _  
        Public Property Warning() As Warning()  
    End Class  
  
    <DataContract()> _  
    Public Class Line  
        <DataMember(Name:="type", EmitDefaultValue:=False)> _  
        Public Property Type() As String  
  
        <DataMember(Name:="coordinates", EmitDefaultValue:=False)> _  
        Public Property Coordinates() As Double()()  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class Location  
        Inherits Resource  
        <DataMember(Name:="name", EmitDefaultValue:=False)> _  
        Public Property Name() As String  
  
        <DataMember(Name:="point", EmitDefaultValue:=False)> _  
        Public Property Point() As Point  
  
        <DataMember(Name:="entityType", EmitDefaultValue:=False)> _  
        Public Property EntityType() As String  
  
        <DataMember(Name:="address", EmitDefaultValue:=False)> _  
        Public Property Address() As Address  
  
        <DataMember(Name:="confidence", EmitDefaultValue:=False)> _  
        Public Property Confidence() As String  
  
        <DataMember(Name:="matchCodes", EmitDefaultValue:=False)> _  
        Public Property MatchCodes() As String()  
  
        <DataMember(Name:="geocodePoints", EmitDefaultValue:=False)> _  
        Public Property GeocodePoints() As Point()  
  
        <DataMember(Name:="queryParseValues", EmitDefaultValue:=False)> _  
        Public Property QueryParseValues() As QueryParseValue()  
    End Class  
  
    <DataContract()> _  
    Public Class QueryParseValue  
        <DataMember(Name:="property", EmitDefaultValue:=False)> _  
        Public Property Property() As String  
  
        <DataMember(Name:="value", EmitDefaultValue:=False)> _  
        Public Property Value() As String        
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class PinInfo  
        <DataMember(Name:="anchor", EmitDefaultValue:=False)> _  
        Public Property Anchor() As Pixel  
  
        <DataMember(Name:="bottomRightOffset", EmitDefaultValue:=False)> _  
        Public Property BottomRightOffset() As Pixel  
  
        <DataMember(Name:="topLeftOffset", EmitDefaultValue:=False)> _  
        Public Property TopLeftOffset() As Pixel  
  
        <DataMember(Name:="point", EmitDefaultValue:=False)> _  
        Public Property Point() As Point  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class Pixel  
        <DataMember(Name:="x", EmitDefaultValue:=False)> _  
        Public Property X() As String  
  
        <DataMember(Name:="y", EmitDefaultValue:=False)> _  
        Public Property Y() As String  
    End Class  
  
    <DataContract()> _  
    Public Class Point  
        Inherits Shape  
        <DataMember(Name:="type", EmitDefaultValue:=False)> _  
        Public Property Type() As String  
  
        ''' <summary>  
        ''' Latitude,Longitude  
        ''' </summary>  
        <DataMember(Name:="coordinates", EmitDefaultValue:=False)> _  
        Public Property Coordinates() As Double()  
  
        <DataMember(Name:="calculationMethod", EmitDefaultValue:=False)> _  
        Public Property CalculationMethod() As String  
  
        <DataMember(Name:="usageTypes", EmitDefaultValue:=False)> _  
        Public Property UsageTypes() As String()  
    End Class  
  
    <DataContract()> _  
    <KnownType(GetType(Location))> _  
    <KnownType(GetType(Route))> _  
    <KnownType(GetType(TrafficIncident))> _  
    <KnownType(GetType(ImageryMetadata))> _  
    <KnownType(GetType(ElevationData))> _  
    <KnownType(GetType(SeaLevelData))> _  
    <KnownType(GetType(CompressedPointList))> _  
    Public Class Resource  
        <DataMember(Name:="bbox", EmitDefaultValue:=False)> _  
        Public Property BoundingBox() As Double()  
  
        <DataMember(Name:="__type", EmitDefaultValue:=False)> _  
        Public Property Type() As String  
    End Class  
  
    <DataContract()> _  
    Public Class ResourceSet  
        <DataMember(Name:="estimatedTotal", EmitDefaultValue:=False)> _  
        Public Property EstimatedTotal() As Long  
  
        <DataMember(Name:="resources", EmitDefaultValue:=False)> _  
        Public Property Resources() As Resource()  
    End Class  
  
    <DataContract()> _  
    Public Class Response  
        <DataMember(Name:="copyright", EmitDefaultValue:=False)> _  
        Public Property Copyright() As String  
  
        <DataMember(Name:="brandLogoUri", EmitDefaultValue:=False)> _  
        Public Property BrandLogoUri() As String  
  
        <DataMember(Name:="statusCode", EmitDefaultValue:=False)> _  
        Public Property StatusCode() As Integer  
  
        <DataMember(Name:="statusDescription", EmitDefaultValue:=False)> _  
        Public Property StatusDescription() As String  
  
        <DataMember(Name:="authenticationResultCode", EmitDefaultValue:=False)> _  
        Public Property AuthenticationResultCode() As String  
  
        <DataMember(Name:="errorDetails", EmitDefaultValue:=False)> _  
        Public Property errorDetails() As String()  
  
        <DataMember(Name:="traceId", EmitDefaultValue:=False)> _  
        Public Property TraceId() As String  
  
        <DataMember(Name:="resourceSets", EmitDefaultValue:=False)> _  
        Public Property ResourceSets() As ResourceSet()  
    End Class  
  
    <DataContract()> _  
    Public Class RoadShield  
        <DataMember(Name:="bucket", EmitDefaultValue:=False)> _  
        Public Property Bucket() As Integer  
  
        <DataMember(Name:="shields", EmitDefaultValue:=False)> _  
        Public Property Shields() As Shield()  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class Route  
        Inherits Resource  
        <DataMember(Name:="id", EmitDefaultValue:=False)> _  
        Public Property Id() As String  
  
        <DataMember(Name:="distanceUnit", EmitDefaultValue:=False)> _  
        Public Property DistanceUnit() As String  
  
        <DataMember(Name:="durationUnit", EmitDefaultValue:=False)> _  
        Public Property DurationUnit() As String  
  
        <DataMember(Name:="travelDistance", EmitDefaultValue:=False)> _  
        Public Property TravelDistance() As Double  
  
        <DataMember(Name:="travelDuration", EmitDefaultValue:=False)> _  
        Public Property TravelDuration() As Double  
  
        <DataMember(Name:="routeLegs", EmitDefaultValue:=False)> _  
        Public Property RouteLegs() As RouteLeg()  
  
        <DataMember(Name:="routePath", EmitDefaultValue:=False)> _  
        Public Property RoutePath() As RoutePath  
    End Class  
  
    <DataContract()> _  
    Public Class RouteLeg  
        <DataMember(Name:="travelDistance", EmitDefaultValue:=False)> _  
        Public Property TravelDistance() As Double  
  
        <DataMember(Name:="travelDuration", EmitDefaultValue:=False)> _  
        Public Property TravelDuration() As Double  
  
        <DataMember(Name:="actualStart", EmitDefaultValue:=False)> _  
        Public Property ActualStart() As Point  
  
        <DataMember(Name:="actualEnd", EmitDefaultValue:=False)> _  
        Public Property ActualEnd() As Point  
  
        <DataMember(Name:="startLocation", EmitDefaultValue:=False)> _  
        Public Property StartLocation() As Location  
  
        <DataMember(Name:="endLocation", EmitDefaultValue:=False)> _  
        Public Property EndLocation() As Location  
  
        <DataMember(Name:="itineraryItems", EmitDefaultValue:=False)> _  
        Public Property ItineraryItems() As ItineraryItem()  
    End Class  
  
    <DataContract()> _  
    Public Class RoutePath  
        <DataMember(Name:="line", EmitDefaultValue:=False)> _  
        Public Property Line() As Line  
  
        <DataMember(Name:="generalizations", EmitDefaultValue:=False)> _  
        Public Property Generalizations() As Generalization()  
    End Class  
  
    <DataContract()> _  
    <KnownType(GetType(Point))> _  
    Public Class Shape  
        <DataMember(Name:="boundingBox", EmitDefaultValue:=False)> _  
        Public Property BoundingBox() As Double()  
    End Class  
  
    <DataContract()> _  
    Public Class Shield  
        <DataMember(Name:="labels", EmitDefaultValue:=False)> _  
        Public Property Labels() As String()  
  
        <DataMember(Name:="roadShieldType", EmitDefaultValue:=False)> _  
        Public Property RoadShieldType() As Integer  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class StaticMapMetadata  
        Inherits ImageryMetadata  
        <DataMember(Name:="mapCenter", EmitDefaultValue:=False)> _  
        Public Property MapCenter() As Point  
  
        <DataMember(Name:="pushpins", EmitDefaultValue:=False)> _  
        Public Property Pushpins() As PinInfo()  
  
        <DataMember(Name:="zoom", EmitDefaultValue:=False)> _  
        Public Property Zoom() As String  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class TrafficIncident  
        Inherits Resource  
        <DataMember(Name:="point", EmitDefaultValue:=False)> _  
        Public Property Point() As Point  
  
        <DataMember(Name:="congestion", EmitDefaultValue:=False)> _  
        Public Property Congestion() As String  
  
        <DataMember(Name:="description", EmitDefaultValue:=False)> _  
        Public Property Description() As String  
  
        <DataMember(Name:="detour", EmitDefaultValue:=False)> _  
        Public Property Detour() As String  
  
        <DataMember(Name:="start", EmitDefaultValue:=False)> _  
        Public Property Start() As String  
  
        <DataMember(Name:="end", EmitDefaultValue:=False)> _  
        Public Property [End]() As String  
  
        <DataMember(Name:="incidentId", EmitDefaultValue:=False)> _  
        Public Property IncidentId() As Long  
  
        <DataMember(Name:="lane", EmitDefaultValue:=False)> _  
        Public Property Lane() As String  
  
        <DataMember(Name:="lastModified", EmitDefaultValue:=False)> _  
        Public Property LastModified() As String  
  
        <DataMember(Name:="roadClosed", EmitDefaultValue:=False)> _  
        Public Property RoadClosed() As Boolean  
  
        <DataMember(Name:="severity", EmitDefaultValue:=False)> _  
        Public Property Severity() As Integer  
  
        <DataMember(Name:="toPoint", EmitDefaultValue:=False)> _  
        Public Property ToPoint() As Point  
  
        <DataMember(Name:="locationCodes", EmitDefaultValue:=False)> _  
        Public Property LocationCodes() As String()  
  
        <DataMember(Name:="type", EmitDefaultValue:=False)> _  
        Public Property Type() As Integer  
  
        <DataMember(Name:="verified", EmitDefaultValue:=False)> _  
        Public Property Verified() As Boolean  
    End Class  
  
    <DataContract()> _  
    Public Class TransitLine  
        <DataMember(Name:="verboseName", EmitDefaultValue:=False)> _  
        Public Property verboseName() As String  
  
        <DataMember(Name:="abbreviatedName", EmitDefaultValue:=False)> _  
        Public Property abbreviatedName() As String  
  
        <DataMember(Name:="agencyId", EmitDefaultValue:=False)> _  
        Public Property AgencyId() As Long  
  
        <DataMember(Name:="agencyName", EmitDefaultValue:=False)> _  
        Public Property agencyName() As String  
  
        <DataMember(Name:="lineColor", EmitDefaultValue:=False)> _  
        Public Property lineColor() As Long  
  
        <DataMember(Name:="lineTextColor", EmitDefaultValue:=False)> _  
        Public Property lineTextColor() As Long  
  
        <DataMember(Name:="uri", EmitDefaultValue:=False)> _  
        Public Property uri() As String  
  
        <DataMember(Name:="phoneNumber", EmitDefaultValue:=False)> _  
        Public Property phoneNumber() As String  
  
        <DataMember(Name:="providerInfo", EmitDefaultValue:=False)> _  
        Public Property providerInfo() As String  
    End Class  
  
    <DataContract()> _  
    Public Class Warning  
        <DataMember(Name:="warningType", EmitDefaultValue:=False)> _  
        Public Property WarningType() As String  
  
        <DataMember(Name:="severity", EmitDefaultValue:=False)> _  
        Public Property Severity() As String  
  
        <DataMember(Name:="text", EmitDefaultValue:=False)> _  
        Public Property Text() As String  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class CompressedPointList  
        Inherits Resource  
        <DataMember(Name:="value", EmitDefaultValue:=False)> _  
        Public Property Value() As String  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class ElevationData  
        Inherits Resource  
        <DataMember(Name:="elevations", EmitDefaultValue:=False)> _  
        Public Property Elevations() As Integer()  
  
        <DataMember(Name:="zoomLevel", EmitDefaultValue:=False)> _  
        Public Property ZoomLevel() As Integer  
    End Class  
  
    <DataContract([Namespace]:="http://schemas.microsoft.com/search/local/ws/rest/v1")> _  
    Public Class SeaLevelData  
        Inherits Resource  
        <DataMember(Name:="offsets", EmitDefaultValue:=False)> _  
        Public Property Offsets() As Integer()  
  
        <DataMember(Name:="zoomLevel", EmitDefaultValue:=False)> _  
        Public Property ZoomLevel() As Integer  
    End Class  
End Namespace  
```