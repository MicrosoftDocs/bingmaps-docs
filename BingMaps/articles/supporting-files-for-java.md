---
title: "Supporting Files for Java | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f4837996-952b-44c3-92c0-fe5bfa015c03
caps.latest.revision: 18
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Supporting Files for Java
> [!NOTE]
>  The Bing Maps Token Service is no longer available. Use Bing Maps Keys to authenticate your [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] application as described in [Getting a Bing Maps Key](../getting-started/getting-a-bing-maps-key.md). Information about transaction accounting provided by Bing Maps Keys is in [Understanding Bing Maps Transactions](../getting-started/understanding-bing-maps-transactions.md).  
  
 The process for implementing [!INCLUDE[ve_platform_cust_id](../articles/includes/ve-platform-cust-id-md.md)] requires that you execute a web service call on the server to retrieve a token. If you are using Java technologies to retrieve the token, then you will need to generate proxy files and use the code described in this topic.  
  
 For an overview of the Customer Identification feature and detailed steps about implementing Customer Identification, see the [Implementing Customer Identification](../articles/implementing-customer-identification.md) article.  
  
## Prerequisites  
 This topic assumes that you know how to create a Java project and also know how to compile and execute Java code using the following systems:  
  
-   J2SE 5.0 or higher - The code in this topic was developed against J2SE 5.0.09.  
  
-   JDK 5.0 or higher - Portions of the JDK are needed to compile and execute the code.  
  
-   [Axis 1.4](http://ws.apache.org/axis) - The web service portion of the sample code was developed with Axis1.4.  Other web service libraries may be used, but the specific development steps may be particular to your web service library.  
  
-   [Jakarta Commons HttpClient](http://hc.apache.org/httpclient-3.x/) - The Jakarta Commons HttpClient is required to provide support for digest authentication through Axis1.4.  
  
-   [Apache XMLRPC](http://www.apache.org/dyn/closer.cgi/ws/xmlrpc/) - This library is a prerequisite for Axis.  
  
-   Container for Java Web Application - Any suitable Java capable Web Server will work.  
  
## Generate the Proxy Files  
 If you have used Axis, you should be familiar with the wsdl2java.exe application, which will generate proxy classes for any web service.  The command is typically:  
  
```  
java org.apache.axis.wsdl.WSDL2Java -U <your user name> -P <your password> https://staging.common.virtualearth.net/find-30/common.asmx  
```  
  
 This will generate proxy files for:  
  
-   CommonService.java  
  
-   CommonServiceSoap.java  
  
-   CommonServiceSoapStub.java  
  
-   CommonServiceSoapSkeleton.java  
  
-   TokenSpecification.java  
  
 You will need to compile these files and include them in the classpath for your servlet code.  
  
## Configure Your web.xml File  
 The servlet retrieves your username and password from the web application configuration file.  Edit your web\WEB-INF\web.xml to set your username and password as follows:  
  
```  
<env-entry>  
  <env-entry-name>UserName</env-entry-name>  
  <env-entry-type>java.lang.String</env-entry-type>  
  <env-entry-value>UserName</env-entry-value>  
</env-entry>  
<env-entry>  
  <env-entry-name>Password</env-entry-name>  
  <env-entry-type>java.lang.String</env-entry-type>  
  <env-entry-value>Password</env-entry-value>  
</env-entry>  
```  
  
## Retrieving the Token  
 The following code, found in Step 3 in the [Implementing Customer Identification](../articles/implementing-customer-identification.md) article, shows how to retrieve a token from the [Bing Maps Token Service](https://common.virtualearth.net/find-30/common.asmx) using Java and the proxy files you generated earlier.  
  
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
  
 To run this code, you will need the project files described in the following sections.  
  
## Project Files  
 Your Java project should contain four files that do the work:  
  
-   /web/js/Ajax.js – This file contains the AJAX enabling JavaScript required to make the call to request the client certificate and process the results.  
  
-   /web/index.jsp – This file is the main client facing Java Server Page.  This page displays a basic map.  
  
-   /src/net/virtualearth/dev/token/TokenServlet – This file is the Servlet that handles the request for the client token.  This servlet creates a new instance of ClientToken.java to generate the token.  
  
-   /src/net/virtualearth/dev/token/ClientToken – This file actually makes the web service call to request the token.  
  
 You will need to package these four files and the auto-generated proxy files into a web application and deploy the application to your web server.  
  
### Ajax.js  
  
```  
[JavaScript]  
//XMLHttpRequest object  
var xmlhttp = false;  
  
/* Make an AJAX call to the servlet, set servletHandler as the callback function*/  
function CallServlet()  
{  
    InitXmlHttp();  
    xmlhttp.onreadystatechange=servletHandler;      
    xmlhttp.open("GET", "TokenServlet", true );  
    xmlhttp.send(null);  
}  
  
/* Initialize the xmlHttp object */  
function InitXmlHttp() {  
    // Attempt to initialize xmlhttp object  
    try  
    {  
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");  
    }  
    catch (e)  
    {  
        // Try to use different activex object  
        try  
        {  
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");  
        }  
        catch (E)  
        {  
            xmlhttp = false;  
        }  
    }  
    // If not initialized, create XMLHttpRequest object  
    if (!xmlhttp && typeof XMLHttpRequest!='undefined')  
      {       
            xmlhttp = new XMLHttpRequest();  
      }  
      // Define function call for when Request obj state has changed  
      xmlhttp.onreadystatechange=servletHandler;  
}  
  
/* Handles and evals the Response from Servlet */  
function servletHandler()  
{  
    if (xmlhttp.readyState==4)  
    {  
        try  
        {  
            //Evaluate the response if AJAX call was successful  
            eval( xmlhttp.responseText);  
            alert("The following VE call was made: " + xmlhttp.responseText);  
        }  
        catch (E)  
        {              
            alert("error: " + E );  
        }  
    }  
}  
```  
  
### Index.jsp  
  
```  
<%@page contentType="text/html"%>  
<%@page pageEncoding="UTF-8"%>  
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  
   "http://www.w3.org/TR/html4/loose.dtd">  
  
   <!-- VE Java Authentication Sample, Copyright 2007 Microsoft Corporation.-->  
<html>  
    <head>  
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  
        <title>Java VE Authentication Sample Code</title>  
        <script type="text/javascript" src="http://dev.virtualearth.net/mapcontrol/mapcontrol.ashx?v=6"></script>  
        <script type="text/javascript" src="js/Ajax.js"></script>  
        <script type="text/javascript">  
          var map = null;  
  
          function GetMap()  
          {  
             //Load the VE Client Token before rendering any VE elements  
             CallServlet();  
             map = new VEMap('myMap');  
             map.LoadMap();  
          }     
          </script>  
    </head>  
    <body onload="GetMap();">  
    <h1>Java VE Authentication Sample Code</h1>  
    <div id='myMap' style="position:relative; width:400px; height:400px;"></div>  
    </body>  
</html>  
```  
  
### TokenServlet.java  
  
```  
[Java]  
package net.virtualearth.dev.token;  
import java.io.*;  
import java.net.*;  
import javax.servlet.*;  
import javax.servlet.http.*;  
  
/**  
 * Copyright 2007 by Microsoft Corporation.  
 * VE Token Servlet  
 * The following override is necessary to enable digest authentication in the client-config.wsdd  
 * required by the Common Service.    
 * <transport name="https" pivot="java:org.apache.axis.transport.http.CommonsHTTPSender"/>  
 * The Jakarta Commons HttpClient libraries are included in the project.  
 * The VirtualEarthService project contains a build.xml which can be built (eg: using Ant)   
 * to compile the VirtualEarthService.jar used in the VEClientToken libraries.  
 */  
public class TokenServlet extends HttpServlet {  
  
    /** Creates and outputs VE Client Tokens used for transaction tracking  
     * @param request servlet request  
     * @param response servlet response  
     */  
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)  
    throws ServletException, IOException{  
  
        response.setContentType("text/html;charset=UTF-8");  
        PrintWriter out = response.getWriter();  
        ClientToken myToken = new ClientToken();  
        try  
        {  
            myToken.SetClientToken(request.getRemoteHost());  
        }  
        catch (Exception ex)  
        {  
            System.err.println(ex);  
        }  
        out.println(String.format("map.SetClientToken(\"%s\")",myToken.GetClientToken()));  
        out.close();  
    }  
  
    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">  
    /** Handles the HTTP <code>GET</code> method.  
     * @param request servlet request  
     * @param response servlet response  
     */  
    protected void doGet(HttpServletRequest request, HttpServletResponse response)  
    throws ServletException, IOException {  
        processRequest(request, response);  
    }  
  
    /** Handles the HTTP <code>POST</code> method.  
     * @param request servlet request  
     * @param response servlet response  
     */  
    protected void doPost(HttpServletRequest request, HttpServletResponse response)  
    throws ServletException, IOException {  
        processRequest(request, response);  
    }  
  
}  
```  
  
### ClientToken.java  
  
```  
[Java]  
package net.virtualearth.dev.token;  
import net.mappoint.s.mappoint_30.*;   
import org.apache.axis.*;  
import java.net.*;  
import javax.xml.rpc.*;  
import javax.naming.*;  
import org.apache.tools.ant.taskdefs.Java;  
  
/**  
 * Copyright 2007 by Microsoft Corporation.  
 * VE Token Generator  
 */  
public class ClientToken {  
  
        CommonServiceSoapStub commonStub;  
        TokenSpecification tokenSpec;  
        Context env;  
        String UserName;  
        String Password;  
  
/**  
 * Public constructor  
 */          
    public ClientToken()   
    {  
    }  
  
/**  
 * Sets the VE Common Service credentials and VE Client Token for authentication  
 * @param clientIP  The IP of the client requesting the VE map  
 * @throws AxisFault  
 * @throws java.net.MalformedURLException  If the Common Service URL does not exist  
 * @throws javax.naming.NamingException  If the properties do not exist in the web.xml configuration file  
 */      
    public void SetClientToken(String clientIP) throws AxisFault, java.net.MalformedURLException, javax.naming.NamingException  {  
        tokenSpec = new TokenSpecification();   
        commonStub = new CommonServiceSoapStub(new URL("https://staging.common.virtualearth.net/find-30/common.asmx"),null );  
        env = (Context) new InitialContext().lookup("java:comp/env");  
        UserName = (String) env.lookup("UserName");  
        Password = (String) env.lookup("Password");  
        commonStub.setUsername(UserName);  
        commonStub.setPassword(Password);  
        tokenSpec.setClientIPAddress(clientIP);  
  
        // The maximum allowable token duration is 480 minutes (8 hours).  
        tokenSpec.setTokenValidityDurationMinutes(480);       
    }  
/** Gets the VE Client Token from the VE Common Service  
 * @return  The String representation of the VE Client Token  
 * @throws java.rmi.RemoteException  If the VE Client Token cannot be retrieved from the Common Service  
 */      
    public String GetClientToken() throws java.rmi.RemoteException  
    {  
        try{  
            return commonStub.getClientToken(tokenSpec);  
        }  
        catch(Exception ex)  
        {  
            System.err.println(ex);  
            return null;  
        }  
    }  
}  
```