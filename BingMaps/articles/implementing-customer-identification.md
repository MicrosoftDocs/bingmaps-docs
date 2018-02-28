---
title: "Implementing Customer Identification | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ad1d11be-52fd-476d-a9cd-711edee9690b
caps.latest.revision: 37
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Implementing Customer Identification
> [!IMPORTANT]
>  The Bing Maps Token Service is no longer available. Instead, use Bing Maps Keys to authenticate your [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] application as described in [Getting a Bing Maps Key](../getting-started/getting-a-bing-maps-key.md). Information about transaction accounting provided by Bing Maps Keys is in [Understanding Bing Maps Transactions](../getting-started/understanding-bing-maps-transactions.md).  
  
 [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] software development kit (SDK) Version 6.1 gives users the ability to implement a customer identification mechanism in their application. This mechanism gives customers the ability to view reports detailing their [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] usage as well as giving business users authorization to use commercial-application-only features.  
  
 This article describes the details of integrating [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] Customer Identification into your commercial application.  
  
## Prerequisites  
 This article assumes that you are already familiar with the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] and JavaScript.  
  
 You will need [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] developer account credentials.  You can sign up for a free developer account on the [Bing Maps Developer Account Request](https://mappoint-css.live.com/mwssignup) site.  This is described in more detail in Step 1 below.  
  
 If you are using .NET to build your application, knowledge of the following is also required:  
  
-   Simple Object Access Protocol (SOAP) application programming interface (API)  
  
-   C# or Visual Basic .NET  
  
-   ASP .NET  
  
 If you are using Java to build your application, supporting Java code can be found in the [Supporting Files for Java](../articles/supporting-files-for-java.md) topic, which requires that you have the following systems:  
  
-   J2SE 5.0 or higher - The code in this topic was developed against J2SE 5.0.09.  
  
-   JDK 5.0 or higher - Portions of the JDK are needed to compile and execute the code.  
  
-   [Axis 1.4](http://ws.apache.org/axis) - The web service portion of the sample code was developed with Axis1.4.  Other web service libraries may be used, but the specific development steps may be particular to your web service library.  
  
-   [Jakarta Commons HttpClient](http://hc.apache.org/httpclient-3.x/) - The Jakarta Commons HttpClient is required to provide support for digest authentication through Axis1.4.  
  
-   [Apache XMLRPC](http://www.apache.org/dyn/closer.cgi/ws/xmlrpc/) - This library is a prerequisite for Axis.  
  
-   Container for Java Web Application - Any suitable Java capable Web Server will work.  
  
 For more information about the [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)], visit the [Bing Maps for Enterprise Web site](http://www.microsoft.com/maps). For information about programming with the [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] and the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)], see the [Bing Maps Interactive SDK](http://www.microsoft.com/maps/isdk/ajax).  
  
## Overview  
 In a simple [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] project, you write JavaScript that is executed by the client.  However, if you intend to track transactions, you will need to execute a web service call on the server to retrieve a token, pass the token to the client, and then register the token with each of the client's **VEMap** instances. The [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] will then embed the token into requests sent to [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] and these requests can be identified by Microsoft.  
  
 ![7ce8a3d8&#45;ec6c&#45;4e1c&#45;8aea&#45;5ab0b8f383b8](../articles/media/7ce8a3d8-ec6c-4e1c-8aea-5ab0b8f383b8.PNG "7ce8a3d8-ec6c-4e1c-8aea-5ab0b8f383b8")  
  
 Figure 1. *Interaction with the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] servers*  
  
## Using the Customer Identification Feature  
 To integrate the [!INCLUDE[ve_platform_cust_id](../articles/includes/ve-platform-cust-id-md.md)] feature into your Web application, first use your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] credentials to request a token. This token contains encrypted information including the end-client’s IP address and your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] developer account ID. A token is only valid for the duration specified in the initial request, beginning from the time the token request is made from your server. Set this token in the map control instance that is loaded into the client’s browser and then all requests made to [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] from your application are identified as requests made by you. [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] logs these requests and you will be able to view [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] transaction reports on the [!INCLUDE[ve_platform_css](../articles/includes/ve-platform-css-md.md)].  
  
 These steps are described in further detail in the following sections.  
  
### Step 1: Sign up for a Developer Account  
 In order to use the Customer Identification feature, you must [sign up for a Bing Maps developer account](https://mappoint-css.live.com/mwssignup). You will need a [Windows Live ID](https://login.live.com/) to sign up for an account. Once your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] developer account is set up, you will have access to the [Bing Maps Customer Services site](https://mappoint-css.live.com/cscv3). On your first visit to the Customer Services site, you will be asked to set your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] developer account password. This is different than the [!INCLUDE[winlive_id_name](../articles/includes/winlive-id-name-md.md)] and password that you use to sign in to the Customer Services site.  
  
### Step 2: Add a reference to the [!INCLUDE[ve_token_svc](../articles/includes/ve-token-svc-md.md)]  
 Before the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] is loaded into the end-client’s browser, a token must be retrieved from the [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)]. [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] provides a secure SOAP API which contains a **GetClientToken** method to accomplish this. To use the [!INCLUDE[ve_platform_css](../articles/includes/ve-platform-css-md.md)], you need your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] credentials, which consist of your developer account ID (found on the **Manage Account** page of the [Bing Maps Customer Services site](https://mappoint-css.live.com/cscv3)) and your developer account password. Microsoft provides a staging environment to test your application and a production environment to use once you have become a licensed customer.  
  
##### Staging Environment  
 The [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] staging environment is separate from but complementary to the production services you use when your application goes live. You can use the staging environment to prototype, develop, and test new applications.  
  
 **Note** The staging environment is not scaled for the extraordinary volumes that the production environment is designed to provide. Any application stress or performance testing is limited to a certain number of requests per second and time of day.  
  
 The [!INCLUDE[ve_token_svc](../articles/includes/ve-token-svc-md.md)] URL in the staging environment is [https://staging.common.virtualearth.net/find-30/common.asmx](https://staging.common.virtualearth.net/find-30/common.asmx).  
  
> [!NOTE]
>  If you obtained a developer evaluation account, you will only have access to the staging environment. In this case, make sure that you retrieve tokens from the staging [!INCLUDE[ve_token_svc](../articles/includes/ve-token-svc-md.md)].  
  
##### Production Environment  
 The [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] production environment is fully scaled for all [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] customers. You use this environment when your application is made available to the public through the Internet, including live, beta, evaluation, and prerelease types of applications. To access the Production environment, you must be a licensed customer. Contact the [Bing Maps Licensing Team](mailto:maplic@microsoft.com?subject=Customer%20Identification%20feature%20access) for more information.  
  
 **Note** Activity in the production environment is billable. For more information about Billable Transactions, see the **Billable Transactions** section below.  
  
 The [!INCLUDE[ve_token_svc](../articles/includes/ve-token-svc-md.md)] URL in the production environment is [https://common.virtualearth.net/find-30/common.asmx](https://common.virtualearth.net/find-30/common.asmx).  
  
 If you are using ASP .NET to build your application, then in your web application project add a web reference to the Staging or Production [!INCLUDE[ve_token_svc](../articles/includes/ve-token-svc-md.md)].  If you are planning on using Java to request a token, depending on your Java Web Service API you may need to create proxy classes before accessing the **GetClientToken** method.  You can find information about this in the [Supporting Files for Java](../articles/supporting-files-for-java.md) topic.  
  
### Step 3: Retrieve a Token  
 The **GetClientToken** method takes a **TokenSpecification** object, which contains two pieces of information:  
  
-   The IP address of the client - You can usually extract this information from the client Http Headers using the request.getRemoteHost() method.  
  
-   The length of time the token will be valid - Tokens are issued for a specific time length.  You must specify a number of minutes ranging from 15 to 480 (8 hours).  
  
 The **TokenSpecification** Class declaration is below.  
  
```  
[Visual Basic]  
Public Class TokenSpecification Inherits System.Object   
[C#]   
public class TokenSpecification : System.Object  
```  
  
#### Public Properties  
  
|Property|Description|  
|--------------|-----------------|  
|ClientIPAddress|A string representing the IPAddress to store in the token. Must be a valid IPv4 form.|  
|TokenValidityDurationMinutes|An integer representing the number of minutes the token will be valid, beginning from the time the request is made. Maximum allowable value is 480. Minimum allowable value is 15.|  
  
 Once you have instantiated the **TokenSpecification** object, you need to pass it to the **GetClientToken** method to return a token.  The **GetClientToken** method returns a `String`, which is the token.  The **GetClientToken** function declaration is below.  
  
```  
[Visual Basic]  
Public Function GetClientToken (ByVal specification As TokenSpecification) As String   
[C#]   
public string GetClientToken (TokenSpecification specification)  
```  
  
 The following code gets a token and makes it available for use by the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)]. This code must be called every time the client requests your Web page.  
  
 If you are using .NET to build your application, the Visual Basic or C# code can be inserted into the server-side **Page_Load** event of your ASP .NET Web Application so that it runs before the map control is loaded on the client.  
  
```  
[Visual Basic]  
' Place the following code in the Page_Load event of your ASP .NET Web  
' application so that it runs before the map control is loaded.  
' This code assumes an Imports reference to the Bing Maps  
' Token service.   
' Be sure to use an SSL connection to protect your information.  
  
Dim commonService As New CommonServiceSoap()  
commonService.Url = "https://staging.common.virtualearth.net/find-30/common.asmx"  
commonService.Credentials =   
  New System.Net.NetworkCredential(  
    "Bing Maps Developer Account ID",   
    "Bing Maps Developer Account password")  
  
' Create the TokenSpecification object to pass to GetClientToken.  
Dim tokenSpec As New TokenSpecification()  
  
' Use the Page object to retrieve the end-client’s IPAddress.  
tokenSpec.ClientIPAddress = Page.Request.UserHostAddress  
  
' The maximum allowable token duration is 480 minutes (8 hours).  
' The minimum allowable duration is 15 minutes.  
tokenSpec.TokenValidityDurationMinutes = 480  
  
' Now get a token from the Bing Maps Token service.  
Dim clienttoken As String  
clienttoken = commonService.GetClientToken(tokenSpec)  
```  
  
```  
[C#]  
// Place the following code in the Page_Load event of your ASP .NET Web  
// application so that it runs before the map control is loaded.  
// This code assumes a using reference to the Bing Maps  
// Token service.   
// Be sure to use an SSL connection to protect your information.  
CommonServiceSoap commonService = new CommonServiceSoap();  
commonService.Url = "https://staging.common.virtualearth.net/find-30/common.asmx";  
commonService.Credentials =   
  new System.Net.NetworkCredential(  
    "Bing Maps Developer Account ID",   
    "Bing Maps Developer Account password");  
  
// Create the TokenSpecification object to pass to GetClientToken.  
TokenSpecification tokenSpec = new TokenSpecification();  
  
// Use the Page object to retrieve the end-client’s IPAddress.  
tokenSpec.ClientIPAddress = Page.Request.UserHostAddress;  
  
// The maximum allowable token duration is 480 minutes (8 hours).  
// The minimum allowable duration is 15 minutes.  
tokenSpec.TokenValidityDurationMinutes = 480;  
  
// Now get a token from the Bing Maps Token service.  
string clienttoken = commonService.GetClientToken(tokenSpec);  
```  
  
 If you are using Java and Axis proxy classes to build your application, the code will be similar to the code below.  The classes used in this code sample are detailed in the [Supporting Files for Java](../articles/supporting-files-for-java.md) topic.  
  
```  
[Java]  
tokenSpec = new TokenSpecification();  
commonStub = new CommonServiceSoapStub(new  
 URL("https://staging.common.virtualearth.net/find-30/common.asmx"), null);  
env = (Context) new InitialContext().lookup("java:comp/env");  
UserName = (String) env.lookup("UserName");  
Password = (String) env.lookup("Password");  
commonStub.setUserName(UserName);  
commonStub.setPassword(Password);  
tokenSpec.setClientIPAddress(clientIP);  
  
//The maximum allowable token duration is 480 minutes (8 hours).  
tokenSpec.setTokenValidityDurationMinutes(480);  
  
//Retrieve the token.  
String token = commonStub.getClientToken(tokenSpec);  
```  
  
### Step 4: Set the Token in the Map Control  
 After the token has been retrieved from the [!INCLUDE[ve_token_svc](../articles/includes/ve-token-svc-md.md)], it must be passed to the client and set for every **VEMap** instance.  You can pass the token to the client using any of a variety of web methods, including adding it as a hidden field, or putting it in the query string.  
  
 If you are building your application using ASP .NET, you can use the following code on the client to retrieve the `clienttoken` server variable set in the Visual Basic .NET or C# code samples in Step 2.  
  
```  
[JavaScript]  
// Retrieve the clienttoken variable from server-side code.  
var token = "<%=clienttoken %>";  
```  
  
 After you have passed the token string to the client, load the staging or production map control and use the **SetClientToken** method of the **VEMap** class to set the token on the **VEMap** instance.  
  
 The **Staging** environment reference to the map control is:  
  
```  
<script type="text/javascript" src="http://staging.dev.virtualearth.net/mapcontrol/mapcontrol.ashx?v=6.2"></script>  
```  
  
 The **Production** environment reference to the map control is:  
  
```  
<script type="text/javascript" src="http://ecn.dev.virtualearth.net/mapcontrol/mapcontrol.ashx?v=6.2"></script>  
```  
  
> [!NOTE]
>  A token retrieved from the staging Token Service only works against the staging map control and a token retrieved from the production Token Service only works against the production map control. If you have an evaluation account, make sure that you use the staging map control.  
  
 Setting the token before you load the map or make any other [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] requests ensures that every request sent to [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] is identified.  
  
```  
[JavaScript]  
// Set the token before loading the map or making any other   
// Bing Maps requests.  
var map = new VEMap(‘mymap’);  
map.SetClientToken(token);  
map.LoadMap();  
```  
  
 Once the token is set, all transactions are logged against your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] Developer Account.  
  
### Step 5: Handle Token Expiration and Error Events  
 Every time a [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] request is made, the token that was set is passed to the server for identification and validation. There are two callback events that can be used to catch token errors. The first is the **ontokenerror** event. This event occurs when a map control request is made with a token that is not a valid [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] token. The second is the **ontokenexpire** event and it occurs when a map control request is made with an expired token. A client token is valid for the duration specified in the request, beginning from the time the request for the token was made to the [!INCLUDE[ve_token_svc](../articles/includes/ve-token-svc-md.md)]. Once the token expires, you will want to alert the end-client that their session has expired and that their browser should be refreshed. To catch these events, use the [VEMap.AttachEvent Method](http://msdn.microsoft.com/en-us/5163d7c9-6ad9-4725-be55-435ba36d03c8). The following code sample shows how to catch token expire and token error events.  
  
```  
[JavaScript]  
// Attach token expired and token error events.  
var map = new VEMap(‘mymap’);  
map.AttachEvent('ontokenexpire', MyHandleTokenExpire);  
map.AttachEvent('ontokenerror', MyHandleTokenError);  
  
function MyHandleTokenExpire()  
{  
   // insert code here to handle token expiration  
}  
  
function MyHandleTokenError()  
{  
   // insert code here to handle token errors  
}  
```  
  
## Viewing Usage Reports  
 Once the [!INCLUDE[ve_platform_cust_id](../articles/includes/ve-platform-cust-id-md.md)] feature is integrated into your application, transactions sent to [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] by your application are logged and you are able to view transaction usage reports on the [Bing Maps Customer Services site](https://mappoint-css.live.com/cscv3). Log in to the [Bing Maps Customer Services site](https://mappoint-css.live.com/cscv3) using the [!INCLUDE[winlive_id_name](../articles/includes/winlive-id-name-md.md)] you used to create your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] developer account. Click on the **View Reports** menu item on the left-hand side of the Home page. On the **View Reports** page, select one of the available [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] reports.  
  
### Viewing [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] Reports  
 The [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] reports, which are found on the **View Reports** page of the [Bing Maps Customer Services site](https://mappoint-css.live.com/cscv3), display information about your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] usage, including your billable transactions ("Billable Transactions"). [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] transactions include MapPoint Web Service (**[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]**) transactions, [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)](**[!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)]**\) map control transactions, [!INCLUDE[vews_product_name](../articles/includes/vews-product-name-md.md)] (**[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]**) transactions, as well as Photosynth transactions.  
  
 Once you have selected a report type, you can choose to filter by Environment to show Staging or Production transactions. Staging transactions are not billable transactions. Production transactions are billable transactions.  
  
 To access the Production environment you must be a licensed customer. Contact the [Bing Maps Licensing Team](mailto:maplic@microsoft.com?subject=Customer%20Identification%20feature%20access) for more information.  
  
#### Billable Transactions  
 The [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] includes the [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)], the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)], the [!INCLUDE[vews_product_name](../articles/includes/vews-product-name-md.md)], and Photosynth.  
  
##### [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)]  
 The [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] (**[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]**) methods that cause billable transactions to be accrued include **Find**, **FindAddress**, **FindById**, **FindByProperty**, **FindNearby**, **FindNearRoute**, **FindPolygon**, **GetLocationInfo**, **ParseAddress**, **GetMap**, **GetLineDriveMap**, **CalculateRoute**, and **CalculateSimpleRoute**.  
  
##### [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)]  
 Certain [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] (**[!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)]**) map control requests made after the [VEMap.SetClientToken Method](http://msdn.microsoft.com/en-us/af70cbf7-bab2-4f04-9ad3-4770e7181dad) is called with a valid token are included in your transaction reports. The following [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] features count as billable transactions and appear in your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] Reports.  
  
 **Map navigation ([!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)]: Load Standard Map)** – Transactions are counted any time new map tiles are requested from [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)]. [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] bills per map view, which is calculated based on the assumption that a map view is multiple tile transactions. This includes **VEMap.LoadMap**, **VEMap.ZoomIn**, **VEMap.ZoomOut**, **VEMap.Pan**, **VEMap.SetMapView**, and many other methods that cause the map to move. A single Billable Transaction shall equate to eight (8) [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] image tiles being fetched from Microsoft servers.  
  
 **Traffic requests ([!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)]: Load Traffic Map)** – If traffic is turned on, you are charged double for every tile that includes traffic information. [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] bills per map view, which is calculated based on the assumption that a map view is multiple tile transactions. A single Billable Transaction shall equate to eight (8) [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] image tiles being fetched from [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] servers.  
  
 **[!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)]: Geocode** – Any time [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] makes a *where-only* request for a find result, one transaction is counted. This includes *where-only* requests from the **VEMap.Find** method as well as the **VEMap.GetDirections** method.  
  
 **VE: ReverseGeocode** - Each request made using the **VEMap.FindLocations** method counts as one transaction.  
  
 **VE: CalculateRoute** – If you make a request for a route using the new **VEMap.GetDirections** method, one transaction per returned route is counted. Use of the deprecated **GetRoute** method is not counted.  
  
##### [!INCLUDE[vews_product_name](../articles/includes/vews-product-name-md.md)]  
 The following [!INCLUDE[vews_product_name](../articles/includes/vews-product-name-md.md)] (**[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]**) requests count as billable transactions and appear in your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] Reports.  
  
 **[!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)]: Load Standard Map** – Transactions are counted any time map tiles are requested from [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] using URIs returned from the [GetMapUri method](../Topic/ImageryServiceClient.GetMapUri%20Method.md) or the [GetImageryMetadata method](../Topic/ImageryServiceClient.GetImageryMetadata%20Method.md). [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] bills per map view, which is calculated based on the assumption that a map view is multiple tile transactions. A single Billable Transaction shall equate to eight (8) [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] image tiles being fetched from Microsoft servers.  
  
 **[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]: Geocode** – Any time a request is made using the [Geocode method](../Topic/GeocodeServiceClient.Geocode%20Method.md), one transaction is counted.  
  
 **[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]: ReverseGeocode** - Any time a request is made using the [ReverseGeocode method](../Topic/GeocodeServiceClient.ReverseGeocode%20Method.md), one transaction is counted.  
  
 **[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]: GetMapUri** - Any time a request is made using the [GetMapUri method](../Topic/ImageryServiceClient.GetMapUri%20Method.md), one transaction is counted. Note that the use of any URIs returned from the **GetMapUri** are counted separately as map tile requests.  
  
 **[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]: CalculateRoute** – Any time a request is made using the [CalculateRoute method](../Topic/RouteServiceClient.CalculateRoute%20Method.md), one transaction is counted.  
  
 **[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]: CalculateRoutesFromMajorRoads** – If you make a request using the [CalculateRoutesFromMajorRoads method](../Topic/RouteServiceClient.CalculateRoutesFromMajorRoads%20Method.md) and the [ReturnRoutes Property](../Topic/MajorRoutesOptions.ReturnRoutes%20Property.md) is set to `false`, one transaction is counted. If you make a request using the [CalculateRoutesFromMajorRoads method](../Topic/RouteServiceClient.CalculateRoutesFromMajorRoads%20Method.md) and the [ReturnRoutes Property](../Topic/MajorRoutesOptions.ReturnRoutes%20Property.md) is set to `true`, one transaction plus one transaction per returned route is counted.  
  
 **[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]: Search** - Any time a request is made using the [Search method](../Topic/SearchServiceClient.Search%20Method.md), one transaction is counted.  
  
##### Photosynth  
 The following Photosynth requests count as billable transactions and appear in your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] Reports.  
  
 **[!INCLUDE[vews_product_abbr](../articles/includes/vews-product-abbr-md.md)]: PhotoSynthView** - Every Synth is associated with a Windows Live ID. Each time a Synth associated with a Windows Live ID that corresponds to a commercial Photosynth account is viewed, one transaction is counted.  
  
## Conclusion  
 By using the [!INCLUDE[ve_platform_cust_id](../articles/includes/ve-platform-cust-id-md.md)] feature in your application, you can view reports detailing your [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] usage as well as gain access to commercial-application-only features.