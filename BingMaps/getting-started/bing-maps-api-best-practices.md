---
title: "Bing Maps API Best Practices | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d90d6d54-9c6c-4d45-add9-b2be68dbb8e4
caps.latest.revision: 21
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Bing Maps API Best Practices
These best practices provide guidelines for using the Bing Maps APIs.  
  
 **Terminology**  
  
 The following terms are used in this document to represent API groups. API’s may also be called out individually.  
  
 **Bing Maps services**  
  
 Includes:  
  
1.  Bing Maps REST Services: Provides geocoding, routing, elevations, imagery and traffic incident information using REST URL requests.  
  
2.  Bing Maps Spatial Data Services: Provides batch geocoding, spatial data source (database with spatial entities) management and data source query services using REST URL requests.  
  
 **Bing Maps controls**  
  
 Includes:  
  
1.  Bing Maps V8 Web Control: Use for web applications.  
  
2.  Windows 10 UWP Map control: Use for Windows 10 UWP apps that use C#, C++ or Visual Basic.  
  
3.  Bing Maps WPF Control: Use for Windows Presentation Foundation (WPF) applications.  
  
## Guidelines for Bing Maps services  
 Please adhere to the following guidelines when coding for Bing Maps services.  
  
> [!TIP]
>  When using query filters in the Bing Spatial Dara Services specific to OData services, single quotes can be escaped in a text value by using two single quotes side by side. This is particularly useful when you want to filter your data by property when if this property has a single quote in it. Please see [How to escape a single quote to be used in an OData query](http://stackoverflow.com/questions/3979367/how-to-escape-a-single-quote-to-be-used-in-an-odata-query) for more information.  
  
### Use batch geocoding when you need to geocode or reverse-geocode a large number of items  
 If you have a set of addresses to geocode, you can significantly reduce transactions by using the Geocode Dataflow API to batch geocode up 200, 000 addresses at a time for a single non-billable transaction.  
  
> [!NOTE]
>  There is a 1M limit of free geocode entities per year  
  
### Use the Find by Query API  
 The Bing Maps REST Services Locations API provides options for geocoding addresses. The recommended method is to pass in addresses as single-line queries using the `Find by Query` API. This will this will help ensure that the parts of the address are correctly categorized and will probably give you the most accurate results.  
  
> [!TIP]
>  This method will make it easier for the user as they will only need to enter the data into a single textbox rather than filling in multiple textboxes.  
  
 For more information on Bing REST Services, please see [Bing Maps REST Service Tips & Tricks](../getting-started/bing-maps-api-best-practices.md#BKMK-Tips-Tricks) below.  
  
### Rate Limiting  
 In the Bing Maps [terms of use](http://www.microsoft.com/maps/product/terms.html) trial and basic keys are limited in the number of transactions they can generate within a period of time. Pubic facing Windows Store, Windows Phone, and WPF apps have a limit of 50,000 transactions in a 24 hour period. Internal Windows apps, public facing web sites and non-Windows mobile apps have a limit of 125,000 transactions a year. Rate limiting occurs when the frequency of requests made against the Bing Maps REST and/or SOAP services by an account exceeds these free terms of use. Rate limiting can also occur when the services are under a lot of load. This is done to ensure that the usage from trial and basic keys do no interrupt the services for those using an Enterprise keys. Enterprise keys are not rate limited and the only way to get around rate limiting is to upgrade to an Enterprise key. For more information see our [Bing Maps Licensing Options](http://www.microsoft.com/maps/Licensing/licensing.aspx) page.  
  
 When a request is rate limited, the response will return no results. This may be confusing at first as it looks like Bing Maps was unable to find results. To indicate that the request was rate limited a flag is added to the header of the response (`X-MS-BM-WS-INFO`) which is set to the value of 1 as documented the [Status Codes and Error Handling](https://msdn.microsoft.com/en-us/library/ff701703.aspx) page. To make for a better user experience, applications that use trial or basic keys should look for this flag in the header and handle requests which are rate limited. Something as simple as logging the fact that a request was rate limited in your application log could help when debugging reported issues.  
  
<a name="BKMK-Tips-Tricks"></a>   
## Bing Maps REST Service Tips & Tricks  
 We recommend the Bing Maps REST services rather than SOAP services. They are newer, have more features, are faster, and can be consumed by non .NET languages with greater ease. If you have the Bing Maps REST services return JSON the response size of a request is significantly smaller than the response size from the same request using the Bing Maps SOAP services. This section will go through and highlight some tips for getting the most out of the Bing Maps REST services.  
  
### Using the REST services in managed code  
 For those of you that have been having issues consuming the Bing Maps REST Services APIs using .NET, please note the following resources:  
  
-   The documentation on how to consume the JSON responses from the Bing Maps REST services can be found on MSDN on the [Using the REST Services with .NET](https://msdn.microsoft.com/en-us/library/jj819168.aspx) page.  
  
-   If you are using Java then take a look at how the REST services are handled in the [bing Maps Android SDK](http://bingmapsandroidsdk.codeplex.com/).  
  
### Geocoding  
 Unless you are geocoding English addresses in the US you should specify a culture parameter to help ensure you get the most relevant results. By default, the culture for all requests is set to **en-US**. If geocoding addresses in the UK, you will find that in some cases using the culture parameter **en-GB** will return better results. This becomes even more important when geocoding addresses that are not in English. To specify a culture in a REST request simply use “&c=cultureCode”. You can take a look at the complete list of [Supported Cultures](https://msdn.microsoft.com/en-us/library/hh441729.aspx).  
  
 Encode address and query parameters. This is especially important when working with non-English languages as special characters often will not work correctly. This is also important if you want to use an ampersand (&) in your query. By encoding an ampersand it will appear in the URL as “%26″. Here are the methods that can be used in different programming languages to encode URL parameters.  
  
|**Language**|**Method**|**Example**|  
|------------------|----------------|-----------------|  
|**JavaScript**|[encodeURIComponent](http://www.w3schools.com/jsref/jsref_encodeURIComponent.asp)|encodeURIComponent(*query*)|  
|**C#/VB**|[Uri](http://msdn.microsoft.com/en-us/library/system.uri.aspx)|Uri.EscapeDataString (*query*)|  
  
 When geocoding free form queries use the unstructured URL format rather than the structured format. The unstructured URL format tends to be much more successful for these types of queries. Note: the structured format actually overlaps with the reverse geocoding URL request format and can return odd results if your query is just made up of numbers.  
  
|**Yes**: Unstructured URL|  
|-------------------------------|  
|http://dev.virtualearth.net/REST/v1/Locations?`query=locationQuery`&key=BingMapsKey|  
  
|**No**: Structured URL|  
|----------------------------|  
|http://dev.virtualearth.net/REST/v1/Locations/`locationQuery`?key=BingMapsKey|  
  
 The Bing Maps geocoder will attempt to find the closest match as possible to your query. In some cases, it will not be able to find an exact match. This is where the match code parameter of the returned results becomes useful. The match code parameter is an array of values and can have any combination of the following three values; Good, Ambiguous, or UpHierarchy. If you are only interested in exact matches then keep a look out for UpHierachy as this indicates that your exact query was not found but an upper level address value was found. For example, you attempt to geocode a postal code but instead the associated country is returned as the postal code was not found.  
  
 If you are using the REST services from server side code, you may find that the results in your application may differ from the results found when using the services locally. The reason for this is that the REST services take your IP address into consideration when making a request. To help reduce this issue you can set the [userIp](https://msdn.microsoft.com/en-us/library/ff701704.aspx) parameter of the request to 127.0.0.1. This will trick the service into thinking you are making the call from a local application and cause it to ignore your IP address.  
  
 If you have a lot of data you want to geocode at once consider using the [Geocode Dataflow API](https://msdn.microsoft.com/en-us/library/ff701733.aspx) and the batch geocoding functionality. This service allows you to geocode up to 200,000 addresses in a single request.  
  
### Reverse Geocoding  
 Limit your coordinates to 6 decimal places. At 6 decimal places you have an accuracy of approximately 10cm on the ground. Any more than 6 decimal places just makes for a longer URL and can confuse the reverse geocoder into thinking this is a free form query search.  
  
 Ensure that your numbers are not being turned into scientific notation format when converting them to string. This occurs quite often when working with small numbers. For example, it is not uncommon for some languages to convert 0.00005 to 5E-5. Scientific notation is not supported by the service and will be interpreted as a free form query.  
  
 Ensure that when converting your coordinates to string that you use an invariant culture. Coordinates that use commas for decimal places will not work correctly.  
  
 Like the batch geocoder you can also do batch reverse geocoding using the Bing Spatial Data Services if you need to reverse geocode a large number of coordinates in one request.  
  
### Routing  
 Many of the tips in the geocoding service apply for the routing service, such as being sure to encode your address locations. However, don’t encode coordinate based locations.  
  
 The default distance units are in Kilometers. Use the [distanceUnit](https://msdn.microsoft.com/en-us/library/ff701717.aspx) parameter to change this to miles if that is your preferred unit of measurement.  
  
 You can now have up to three possible routes returned by the routing engine for transit and driving directions in certain countries. This may be desirable in some applications but it is best to make this optional to your users. Although the calculation on Bing Maps end is fast, the response from Bing Maps is much larger when returning 3 routes rather than one. This could become an issue for users with slow internet connections (i.e. mobile users).  
  
 When using Bing Maps in areas where geocoding coverage is limited, consider allowing the user to select their start and end point on the map via a click event or by dragging a pushpin. This will allow you to pass in coordinates for your end points rather than an address. The routing engine is capable of calculating routes anywhere there is road data, even if there is no geocoding coverage.  
  
 If you want to retrieve the coordinates that make up the route line along the roads use the [routePathOutput](https://msdn.microsoft.com/en-us/library/ff701717.aspx) parameter.  
  
### Imagery Service  
 When requesting a static map image from Bing Maps the imagery service the service will automatically choose the best image format to return the image in for best resolution. Note: this may not be the preferred image type in some cases. For example, the service may return Ordnance Survey maps in PNG format; you may find you prefer these maps returned as JPG of GIF format. You can specify the image type using the [format](https://rbrundritt.wordpress.com/2012/01/06/bing-maps-rest-service-net-libraries/) parameter.  
  
 The Imagery service can return two different types of metadata. The [first type](https://rbrundritt.wordpress.com/2009/08/01/ve-silverlight-control-%e2%80%93-pushpins-infoboxes-and-best-map-view/) of metadata gives you information about the imagery in Bing Maps for a specific location, zoom level and map type. This is useful if you want to find the age of the imagery or want to know is a specific type of imagery is available for a certain location. The [second type](https://msdn.microsoft.com/en-us/library/hh667439.aspx) of metadata is for a static image generated from the imagery service. This second metadata may include information such as pixel coordinates of pushpins on your image. This is useful if you want to be able to tie events to the generated image or create an [HTML image map](http://www.w3schools.com/TAGS/tag_map.asp).  
  
### Reducing Usage Transactions  
 If you are using the Bing Maps Rest services in conjunction with one of the Bing Maps map controls, you can significantly reduce the number of transactions your application incurs against your Bing Maps account if you request the Bing Maps key from the map control rather than using your normal Bing Maps key. This is quite often an overlooked feature. When getting the credentials from the map you do not get back your original Bing Maps key. Instead, you get a special session key which you can use as a Bing Maps key to make requests of the Bing Maps services. By doing this, all transactions incurred by this session key will be non-billable. Here are some examples of how to properly use a session key.  
  
 **Bing Maps V8 Web Control**  
  
```  
function ClickGeocode()  
 {  
                map.getCredentials(MakeBingMapsRESTRequest);  
 }  
  
 function MakeBingMapsRESTRequest(sessionKey)  
 {  
                //Generate a request URL for the Bing Maps REST services.  
                //Use the session key in the request as the Bing Maps key  
 }  
  
```  
  
 A full working sample for the above using JavaScript can be found on MSDN in the [Geocoding a Location](https://msdn.microsoft.com/en-us/library/gg427601.aspx) page.  
  
 **Bing Maps WPF control**  
  
```  
Map.CredentialsProvider.GetCredentials((c) =>  
{  
                string sessionKey = c.ApplicationId;  
  
                //Generate a request URL for the Bing Maps REST services.  
                //Use the session key in the request as the Bing Maps key  
});  
  
```  
  
 Full working samples using .NET can be found on MSDN in the [Using the REST Services with .NET](https://msdn.microsoft.com/en-us/library/jj819168.aspx) page.  
  
## Guidelines for Bing Maps controls  
 Please adhere to the following guidelines when coding for Bing Maps controls.  
  
### Minimize map control sessions to reduce billable transactions  
 When you use the Bing Maps V8 control to add maps to your application, you are charged one billable transaction per session. A session is created when you load the map control on a web page and ends when you leave that web page. If you load the map control in a separate web page, you start a new session and are charged another billable transaction. If it’s possible to not change pages and still perform the map operations you need on the same web page, you will save on transactions. For example, if you want to show a map of locations and show directions to a particular location upon request, you will have the fewest transactions if you show the map of locations and the map with directions on the same web page. If you want to make use of any of the Bing Maps services, you can also save transactions by using a session key instead of a Bing Maps Key. For more information, see Use session keys to use Bing Maps services from within Bing Maps controls.  
  
> [!IMPORTANT]
>  A session key can only be used with the Bing Maps services on the same webpage or application instance that the map control was loaded on.  
  
### Making use of Sessions  
 This section will go through and highlight many useful tips to help you make the most of your Bing Maps sessions and transactions. This can have a huge impact on the number of billable transactions that get generated by your application and as a result make a big difference in terms of licensing. To start off, there are a couple of definitions you should know.  
  
-   **Bing Maps Session**: A Bing Maps session occurs when one of the map controls is loaded. Any transactions occurred against the Bing Maps services, while within a session is non-billable. Note this requires the application to properly use Bing Maps Keys.  
  
-   **Bing Maps Transaction**: A Bing Maps transaction occurs any time a service request is made. For example, some of the more common services used that incur transactions are: Bing Maps Geocoding, Routing, and Imagery service, Bing Spatial Data Service Query.  
  
-   **Bing Maps Key**: A Bing Maps Key is a unique string that is used to authenticate a user’s Bing Maps application or service request. This is the primary method used for tracking usage of the Bing Maps API’s.  
  
 Complete documentation explaining all the different ways sessions and transactions are incurred can be found at [Understanding Bing Maps Transactions](https://msdn.microsoft.com/en-us/library/ff859477.aspx).  
  
> [!TIP]
>  Many of the Bing Maps API’s have a method for getting the credentials from the map after you have loaded it using a valid Bing Maps key. One often overlooked feature is that, by getting the credentials from the map, you do not get back your original Bing Maps key. Instead, you get a special session key which you can use as a Bing Maps key to make requests to the Bing Maps services. By doing this, all transactions occurred by this session key will be non-billable. Many developers overlook this feature and opt to simply use their original Bing Maps key, not knowing that they are actually incurring more billable transactions than they need to.  
  
#### Implementing Session Keys  
 Implementing session keys is pretty straight forward. You simply use a session key instead of a Bing Maps Key. When using the REST services, simply use your session key with the `key` parameter of your requests.  
  
 The following are examples of how you can generate session keys in the different Bing Maps controls.  
  
 **Bing Maps V8 Web Control**  
  
```  
var sessionKey;  
  
map.getCredentials(function (c) {  
    sessionKey = c;  
});  
```  
  
 **Bing Maps WPF Controls**  
  
```  
  
      C#  
string sessionKey;  
  
map.CredentialsProvider.GetCredentials((c) =>  
{  
    sessionKey = c.ApplicationId;  
});  
  
Visual Basic  
Dim sessionKey As String  
  
map.CredentialsProvider.GetCredentials(Function(c)   
sessionKey = c.ApplicationId  
End Function)  
  
```  
  
## Guidelines for both Bing Maps services and Bing Maps controls  
 Please adhere to the following guidelines when coding for both Bing Services and Bing Maps controls.  
  
### Use session keys to use Bing Maps services with Bing Maps controls  
 Bing Maps service requests made in the context of a Bing Maps control session with a session key (instead of a Bing Maps Key) create only non-billable transactions. This is true even if the transaction is noted as billable in the transactions table. For example, if you use the Bing Maps V8 Web control to show a map in a web page, and query for a list of points of interest (POIs) near a point using the Bing Maps Spatial Data Services by using a session key, a non-billable transaction is recorded. If you had made the request with a Bing Maps Key, this request would be billable and would count towards the billable transaction limits.  
  
 To obtain a session key, you must establish a Bing Maps session. A Bing Maps session is created when you use one of the Bing Maps controls to show a map in your application. If you are using the Bing Maps V8 Web Control, the session ends when you move away from a web page that displays the control. Note that the application displays a map on two separate web pages, each of those web pages is a separate session. For applications that use the Bing Maps for Windows Store apps control (C++, C#, or Visual Basic) or the WPF control, a session is created when you start the application and ends when you close the application. The session key is used in place of the Bing Maps key in the request. For information about how to create a session key, see [Using the REST Services with .NET](https://msdn.microsoft.com/en-us/library/jj819168.aspx) and [Geocoding a Location](https://msdn.microsoft.com/en-us/library/gg427601.aspx).  
  
-   Non-billable request  
    http://BingMapsServiceRequest?key=sessionKey  
  
-   Billable request  
    http://BingMapsServiceRequest?key=BingMapsKey  
  
### Encode address values before geocoding  
 Make parameter string parameter values UTF-8 encoded strings so that blanks and other special characters are encoded. For example, blank spaces are encoded as %20 and ampersands (&) are encoded as %26. Languages that contain more than Latin characters, such as Japanese native character sets, must be encoded. Among options for encoding strings are the JavaScript [encodeURI](http://www.w3schools.com/jsref/jsref_encodeURI.asp) function and the .NET [System.URI](https://msdn.microsoft.com/en-us/library/system.uri.aspx) class.  
  
> [!IMPORTANT]
>  For JavaScript, if you wish to geocode cross streets or intersections that may include an ampersand (&) in your query we recommend the `encodeURIComponent` function rather than the `encodeURI` function, as `encodeURIComponent` will return the actual ampersand rather than %26.