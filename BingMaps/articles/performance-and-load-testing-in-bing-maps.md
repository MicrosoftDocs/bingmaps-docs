---
title: "Performance and Load Testing in Bing Maps | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5daa7e1c-8ce1-450f-abed-5abc0c425c47
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Performance and Load Testing in Bing Maps
This article examines different types of testing on [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] applications, including client side performance testing, server side performance testing, load testing, and stress testing without bombarding the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] servers with requests.  
  
## General Testing Best Practices  
 When performing tests on your web site it is good practice to thoroughly test one page at a time and make sure each page is reliable before proceeding to the next page. Carefully document all details on how to reproduce bugs and the methods used to resolve the bugs. This documentation will prove handy if future similar bugs arise.  
  
 After fixing a bug you should perform regression testing, which consists of re-testing a section of the site to make sure the bug fix hasn’t broken some other component or created new bugs in your site. When testing and debugging, be sure to clear your cache after each fix.  It is very common for a repaired bug to remain in the Web browser cache, and this can cause confusion when you try to resolve the issue.  
  
 Test your web site on multiple browsers and platforms. There are many different browsers available and it is not unusual for web pages to render differently in one browser when compared to another. It is also common for a buggy script to work in one browser but not another. The common browsers to test include Internet Explorer 6 and 7, and Firefox 1.5 and 2. Safari 2 and 3 are also becoming more popular.  
  
 Another commonly overlooked test is to view your pages on different types of monitors. Various fonts and styles may look wonderful on an LCD monitor but may be impossible to read on a CRT monitor, thus making your web site unusable. On the same note it is also good practice to view your pages in a variety of screen resolutions and color palettes.  
  
 You should also verify that all links work properly and point to the correct location. There is software available that can test the functionality of all links on your site, but such software is not capable of knowing whether the links point to the correct locations, so be sure to check manually as well. Similarly, it is also good practice to check that all download links point to the correct files.  
  
 Finally, test error pages by intentionally entering incorrect URLs into the address bar. Verify that the appropriate error is being displayed and that helpful information is provided. Having links to redirect the user back to the site when an error occurs is helpful as well.  
  
## General Performance Considerations  
 [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] applications depend on multiple connections to a variety of servers (your local servers as well as Microsoft’s servers) and the client.  Given the interactive nature of these applications, performance is a key consideration.  
  
 The best way to optimize performance is to reduce the number of HTTP requests made by your site. Reducing the number of HTTP requests has the biggest impact of any change you can make in terms of reducing response time, and is also often the easiest performance improvement to make.  
  
 The following sections show some simple ways to improve performance.  
  
### Set the Map Center Point and Zoom Level on Load  
 In [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] applications, one common way of testing site performance is to load the map and then set the center point and zoom in. Some simple code to perform these steps is shown below.  
  
```  
function GetMap()  
{  
var myCenterPoint = new VELatLong(42.43511345,-110.432452345);  
var myZoomLevel = 15;  
var map = new VEMap('myMap');  
map.LoadMap();  
  
map.SetCenterAndZoom(myCenterPoint,myZoomLevel);  
}  
```  
  
 This code requires that your web application load the map tiles twice: once for the default map, and once for the zoomed map. In many cases, however, you can calculate the location of where you want your map to be centered and zoomed before loading the map, and then apply this information as a constructor to the LoadMap() method.  
  
 By making this simple change, we can cut the number of tiles that need to be loaded in half. This has two benefits: fewer tiles to load (and therefore faster loading time); and the number of transactions made against your account will be cut in half (therefore halving your costs). The next code sample shows improved code for loading a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map at a specific position and zoom level.  
  
```  
function GetMap()  
{  
var myCenterPoint = new VELatLong(42.43511345,-110.432452345);  
var myZoomLevel = 15;  
var map = new VEMap('myMap');  
map.LoadMap(myCenterPoint,myZoomLevel);  
}  
```  
  
### Make Your [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] Pages Cacheable  
 If your Web application is one that users visit on a regular basis, then making your page cacheable will greatly reduce the loading times for future visits.  Caching reduces the number of HTTP requests that have to go back to the server on subsequent visits to your site. To make a page cacheable, set the **expires** HTML META tag or equivalent HTTP header property to a future date (the date on which you want the cache to expire), as shown below.  
  
```  
//HTML META tag  
<META HTTP-EQUIV="expires" CONTENT="Wed, 27 Feb 2008 08:21:57 GMT">  
//header property expires: Wed, 27 Feb 2008 08:21:57 GMT  
```  
  
 Note that setting an expiration date that is far in the future can be risky, as it will require you to modify the names of updated components if you want them to load correctly. If you modify a component of your web application but do not change the name, the old component will still be displayed as it is what is stored in the user’s cache. A common naming convention when using this method is to add version numbers to your component names.  
  
 Another disadvantage to having expiration dates that are far in the future is that your web application may not be displaying the most up to date [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] image tiles. Setting the expiration date so that it is no more than a few weeks into the future is usually optimal. The impact of this performance improvement depends on how often a user visits your site.  
  
### Using Compression for [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] HTTP Responses  
 Another variable that affects response times is the size of the HTTP responses. HTTP response size can be reduced by implementing compression. A common method of compression is to use Gzip as the encoding type for the HTTP response messages. For compression to work, the client side code must have a variable in its HTTP request to the server that indicates that it supports compression. Compression support is indicated in the **Accept-Encoding** header of the HTTP request.  
  
```  
Accept-Encoding: gzip, deflate  
```  
  
 If the web server sees the **Accept-Encoding** header in the request, it will compress the response using one of the methods listed (e.g. gzip). The web server notifies the web client of what type of compression it used to compress the HTTP response in the **Content-Encoding** header in the response.  
  
```  
Content-Encoding: gzip  
```  
  
 Compressing HTTP responses reduces the response size, on average, by about 70%. Compression is very common when HTTP responses frequently include scripts, style sheets, and text responses such as XML and JSON. The compression method should not be used for images and PDFs, since they are already compressed.  
  
### Progressive Page Rendering  
 Another way to make your web application load faster is to put your style sheets in the \<head> element of your pages, which allows the page to render progressively. Progressive rendering means that the page will render and display whatever content it has as soon as possible. This technique is important for pages that have a lot of content but may also have users on slower internet connections. Note that it is important to give the user visual feedback that the page is loading if it is going to take a long time, and progressive page rendering is one way of supplying this improved user experience.  
  
 You can use the opposite method for scripts and add them at the bottom of the page instead of at the top, which will also allow the page to load faster. The reason for this is that if the script is loaded before the style sheets, then progressive rendering is blocked. Also, when a script is downloading, the browser will not allow any other downloads to start until the script is finished downloading. By having your scripts near the bottom of your page you avoid this problem and allow for parallel downloads. Note that this method cannot always be used, since some scripts use the **document.write** method to insert parts into the page’s content during loading.  
  
### External Files  
 Finally, keep your style sheets and scripts in external files. This will allow these files to be cached and therefore reduce the number of files that will need to be downloaded the next time the user visits the page. Scripts and style sheets that are in line with the HTML markup get downloaded every time the page is requested.  
  
## Client Side Performance Testing  
 Unfortunately, the tools for client side testing of JavaScript have not evolved to the level of tools for compiled or server side code.  However, there are several third party options that can provide you insight into the JavaScript call stack and allow you to generate some basic performance numbers.  The tools are often browser specific, however, so your analysis and results may or may not improve the experience for all users.  
  
## Server Side Performance Testing  
 There are many products for testing server side code, but the tool you use depends on the language of your server side code. Visual Studio is a common tool to use when the server-side code is ASP.NET. ASP.NET offers simple mechanisms to track page behavior.  For example, it is easy to turn on timers to calculate how long it took for a method to process.  To do this turn on application tracing, or add Trace="true" to the page declaration of the pages you wish to evaluate.  You can also turn on application level tracing in the web.config file.  
  
 When performing Server Side testing it is recommended to do all of your testing on a staging server. Ideally your staging and production servers are identical for accurate testing results. Server side performance testing can be done at the same time as load testing. When the load testing is simulating a thousand or more users accessing your web site, you should monitor the CPU, memory, disk I/O and network I/O usage.  
  
## Load Testing  
 Load testing general consists of emulating the performance bottlenecks that would be experienced if thousands of users visit your site. The goals of load testing are to expose bugs that do not surface in stand alone tests, such as memory leaks, and overflow buffers. Another goal is to ensure that the application meets the performance baseline established during performance testing. There are many load testing products available on the market today.  
  
 When performing load testing the same steps should be covered regardless of the tool you are using. These steps are:  
  
-   Identify Key Scenarios  
  
-   Identify Workload  
  
-   Identify Metrics  
  
-   Create Test Cases  
  
-   Simulate Load  
  
-   Analyze the Results  
  
 One major contract caveat to load testing is that you are not allowed to load test the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] servers without prior arrangement and negotiation with Microsoft.  Therefore your load testing strategies need to consider how to avoid this constraint and properly test your code without unduly stressing the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] servers.  
  
#### Identify Key Scenarios  
 Scenarios are anticipated user paths that generally incorporate multiple application activities. A general method for identifying key scenarios is to first identify the high level scenarios. For example, consider a general stores web site. A user may connect to the main web page then connect to the locator page, from which they will go to a results page.  
  
 After identifying the high level scenarios you can identify the low level scenarios involved. You may have to log on to the web site, then select the locator link. You will then have to fill out the search criteria, which may have several different possible scenarios. There might also be filters available on the search page which will increase the number of possible combinations of test cases.  
  
 After identifying the high and low level scenarios you have to identify the most commonly executed scenarios and be sure to focus more load testing resources on those scenarios. In the general stores web site example, there may be a “contact us” page which would have less traffic than the store locator page.  
  
#### Identify Workload  
 The purpose of identifying the workload is to calculate the ratio between the number of users executing a scenario and ratio of work for each scenario. For an existing web application this information is available in the IIS logs. For a new site this can be calculated based on market research, historical data, and market trends. This information will give you an idea of the type of load you can expect to have on your web site. Once again, you will want to stress the high workload areas more than the lower workload areas.  
  
#### Identify Metrics  
 Metrics are helpful in identifying problem areas and bottlenecks within your application. Metrics also identify how close your application is to meeting your performance goals.  
  
 Here is the process of identifying metrics:  
  
-   Define questions related to your application performance which can be easily tested. For example, what is the response time when searching for a location? How many searches are performed in a minute?  
  
-   Determine answers for the questions identified and use these as performance goals. For example search response time should be 2 seconds and a maximum of 100 searches should be placed in a minute. The answers are based on market research, historical data, and market trends.  
  
-   With the list of performance related questions and answers, you can set out to identify metrics. A sample of a high level metrics would be how your web application serves against the quality goals.  
  
|Metric|Performance Goal|  
|------------|----------------------|  
|Search Response Time|2 seconds|  
|Searches Per Minute|100|  
  
 •Using the same approach you can identify lower level metrics which focus on measuring the performance and identifying the bottlenecks in the system. When identifying low level metrics, you should determine a baseline for them under normal load conditions. This helps you decide on the acceptable load levels for your application. Baseline values help you analyze your application performance at varying load levels. Here is an example of low level metric.  
  
|Metric|Accepted Level|  
|------------|--------------------|  
|Request Execution Time|Must not exceed 8 seconds|  
|Requests Rejected|Less than 5|  
|Throughput|100 or more requests per second|  
|Percent Processor Time|Must not exceed 75%|  
|Memory Available|25% of total RAM|  
  
 Additionally, to evaluate the performance of your application in more detail and to identify the potential bottlenecks, monitor metrics under the following categories:  
  
-   **Network-specific metrics**. This set of metrics provides information about the overall health and efficiency of your network, including routers, switches, and gateways.  
  
-   **System-related metrics**. This set of metrics helps you identify the resource utilization on your server. The resources are CPU, memory, disk I/O, and network I/O.  
  
-   **Platform-specific metrics**. Platform-specific metrics are related to software that is used to host your application, such as the .NET Framework common language runtime and ASP.NET-related metrics.  
  
-   **Application-specific metrics**. These include custom performance counters inserted in your application code to monitor application health and identify performance issues. You might use custom counters to determine the number of concurrent threads waiting to acquire a particular lock or the number of requests queued to make an outbound call to a Web service.  
  
-   **Service level metrics**. Service level metrics can help to measure overall application throughput and latency, or they might be tied to specific business scenarios.  
  
#### Create Test Cases  
 A test case is a specific sequence of events that helps you evaluate your metrics for a specific user scenario.  Test cases are created based on the scenarios and the profile mix identified in the previous steps. In general, the inputs for creating the test cases are performance objectives, workload characteristics, and the identified metrics. Each test case should mention the expected results in such a way that each test case can be marked as a pass or fail after execution.  
  
#### Simulate Load  
 This is when you would use your load testing application to simulate multiple users connecting to your site. Be sure to set up the tool to mimic the identified test cases. Using load generation tools, you can generate load for a number of users specified in the workload characteristics for the given scenario. You should begin your load testing with a small number of users distributed throughout your web site. Gradually increase the load. It is important to have sufficient time between each step of increasing number of users, so that the system gets time to stabilize before the next set of user connection executes the test case. Continue to increase the load, and record the behavior until you reach the threshold for the resources identified in your performance objectives.  
  
#### Analyze the Results  
 To analyze the data from your load tests, compare the test results against the metrics you have defined. Determine whether the performance of the application being tested shows a trend toward or away from the performance objectives. Analyze the measured metrics to diagnose potential bottlenecks. Additional metrics can be captured in subsequent test cycles if needed. For example, suppose that during the first iteration of load tests, the process shows a marked increase in the memory consumption, indicating a possible memory leak. In the subsequent iterations, additional memory counters related to generations can be captured to study the memory allocation pattern for the application.  
  
 Note that when load testing your site it is important not to load test against [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] without prior arrangement and negotiation with Microsoft.  The [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] servers have been load tested by Microsoft and there is no need to load test them yourself. The easiest way to ensure that you do not load test against the [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] servers is to comment the code that loads the map control or any other code that accesses the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] API.  
  
## Stress Testing  
 The purpose of stress testing is to make sure that if the system fails it will be able to recover gracefully. Stress testing tries to break the system under load by overwhelming its resources or by taking resources away from it. Stress testing can be done by using any one or combination of the following tactics:  
  
-   Significantly increase the baseline number of concurrent users and HTTP connections.  
  
-   If the web site uses a database then take it offline and then restart it.  
  
-   Run processes that consume resources, such as CPU, memory, disk, or network resources, on the servers.  
  
-   By stress testing you are able to see how the system reacts to failure. Things to look for include but are not limited to:  
  
-   Does the session state get saved or does it crash suddenly?  
  
-   Does the site freeze or does it fail gracefully?  
  
-   When restarted is the session able to recover to the last good state?  
  
-   Are meaningful error messages displayed?  
  
-   Is the security of the site compromised because of unexpected failures?