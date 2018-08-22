---
title: "Driving Route using Tolerances Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 40a5f078-0231-47ae-b206-e0866d3b2afc
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Driving Route using Tolerances Example
The following example shows how to request a driving route between two locations and specifies tolerances so that subsets of route points that meet those tolerances are returned. Each tolerance returns a subset of route points in the response. The route path defined by the subset of route path points approximates the route path defined by the full set of route points within the tolerance provided. The response to this request is the same as are shown for both XML and JSON formats.  
  
 This example is the same as the request that is described in the [Driving Route with Route Path Example](../examples/driving-route-with-route-path-example.md) with the addition of tolerances. Examples of the additional content that is returned when tolerances are specified are shown below in JSON and XML formats.  
  
```  
http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=44.979035,-93.26493&wp.1=44.943828508257866,-93.09332862496376&optmz=distance&rpo=Points&tl=0.00000344978,0.0000218840,0.000220577,0.00188803,0.0169860,0.0950130,0.846703&key=BingMapsKey  
```  
  
 **JSON Response**  
  
 The following route path generalization collections are returned with the route path points in Route resource in the response. Each route path generalization specifies a subset of route path points and the associated tolerance (latLongTolerance). The route path points are specified by an index value. Route path points are assigned integer index values that start with 0.  
  
 These generalizations would be added to the complete response shown in [Driving Route with Route Path Example](../rest-services/driving-route-with-route-path-example.md).  
  
```  
{  
   "routePath":{  
        -- route path points --  
      "generalizations":[  
         {  
            "latLongTolerance":3.44978E-06,  
            "pathIndices":[  
            0,2,3,4,5,6,7,8,9,10,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,  
            33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,  
            60,61,62,63,64,65,66]  
         },  
         {  
            "latLongTolerance":2.1884E-05,  
            "pathIndices":[  
             0,2,4,5,6,7,8,9,10,11,14,15,17,18,20,21,22,23,24,25,26,27,28,29,30,31,  
             32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,  
             58,59,60,63,66  
            ]  
          },  
         {  
            "latLongTolerance":0.000220577,  
            "pathIndices":[  
             0,2,8,11,15,18,22,24,25,26,28,30,32,33,35,38,41,43,47,52,57,58,60,63,66  
            ]  
         },  
         {  
            "latLongTolerance":0.00188803,  
            "pathIndices":[  
               0,15,25,30,41,47,66  
            ]  
         },  
         {  
            "latLongTolerance":0.016986,  
            "pathIndices":[  
               0,66  
            ]  
         },  
         {  
            "latLongTolerance":0.095013,  
            "pathIndices":[  
               0,66  
            ]  
         },  
         {  
            "latLongTolerance":0.846703,  
            "pathIndices":[  
               0,66  
            ]  
         }  
      ]  
   }  
}  
```  
  
 **XML Response**  
  
 You receive the following XML version of the route path generalizations when the output=xml parameter is set in the request.  
  
```  
<RoutePath>  
   – route path points --  
  <RoutePathGeneralization>  
    <Index>0</Index>  
    <Index>2</Index>  
    <Index>3</Index>  
    <Index>4</Index>  
    <Index>5</Index>  
    <Index>6</Index>  
    <Index>7</Index>  
    <Index>8</Index>  
    <Index>9</Index>  
    <Index>10</Index>  
    <Index>11</Index>  
    <Index>13</Index>  
    <Index>14</Index>  
    <Index>15</Index>  
    <Index>17</Index>  
    <Index>18</Index>  
    <Index>19</Index>  
    <Index>20</Index>  
    <Index>21</Index>  
    <Index>22</Index>  
    <Index>23</Index>  
    <Index>24</Index>  
    <Index>25</Index>  
    <Index>26</Index>  
    <Index>27</Index>  
    <Index>28</Index>  
    <Index>29</Index>  
    <Index>30</Index>  
    <Index>31</Index>  
    <Index>32</Index>  
    <Index>33</Index>  
    <Index>34</Index>  
    <Index>35</Index>  
    <Index>36</Index>  
    <Index>37</Index>  
    <Index>38</Index>  
    <Index>39</Index>  
    <Index>40</Index>  
    <Index>41</Index>  
    <Index>42</Index>  
    <Index>43</Index>  
    <Index>44</Index>  
    <Index>45</Index>  
    <Index>46</Index>  
    <Index>47</Index>  
    <Index>48</Index>  
    <Index>49</Index>  
    <Index>50</Index>  
    <Index>51</Index>  
    <Index>52</Index>  
    <Index>53</Index>  
    <Index>54</Index>  
    <Index>55</Index>  
    <Index>56</Index>  
    <Index>57</Index>  
    <Index>58</Index>  
    <Index>59</Index>  
    <Index>60</Index>  
    <Index>61</Index>  
    <Index>62</Index>  
    <Index>63</Index>  
    <Index>64</Index>  
    <Index>65</Index>  
    <Index>66</Index>  
    <LatLongTolerance>3.44978E-06</LatLongTolerance>  
  </RoutePathGeneralization>-<RoutePathGeneralization>  
    <Index>0</Index>  
    <Index>2</Index>  
    <Index>4</Index>  
    <Index>5</Index>  
    <Index>6</Index>  
    <Index>7</Index>  
    <Index>8</Index>  
    <Index>9</Index>  
    <Index>10</Index>  
    <Index>11</Index>  
    <Index>14</Index>  
    <Index>15</Index>  
    <Index>17</Index>  
    <Index>18</Index>  
    <Index>20</Index>  
    <Index>21</Index>  
    <Index>22</Index>  
    <Index>23</Index>  
    <Index>24</Index>  
    <Index>25</Index>  
    <Index>26</Index>  
    <Index>27</Index>  
    <Index>28</Index>  
    <Index>29</Index>  
    <Index>30</Index>  
    <Index>31</Index>  
    <Index>32</Index>  
    <Index>33</Index>  
    <Index>34</Index>  
    <Index>35</Index>  
    <Index>36</Index>  
    <Index>37</Index>  
    <Index>38</Index>  
    <Index>39</Index>  
    <Index>41</Index>  
    <Index>42</Index>  
    <Index>43</Index>  
    <Index>44</Index>  
    <Index>45</Index>  
    <Index>46</Index>  
    <Index>47</Index>  
    <Index>48</Index>  
    <Index>49</Index>  
    <Index>50</Index>  
    <Index>51</Index>  
    <Index>52</Index>  
    <Index>53</Index>  
    <Index>54</Index>  
    <Index>55</Index>  
    <Index>57</Index>  
    <Index>58</Index>  
    <Index>59</Index>  
    <Index>60</Index>  
    <Index>63</Index>  
    <Index>66</Index>  
    <LatLongTolerance>2.1884E-05</LatLongTolerance>  
  </RoutePathGeneralization>-<RoutePathGeneralization>  
    <Index>0</Index>  
    <Index>2</Index>  
    <Index>8</Index>  
    <Index>11</Index>  
    <Index>15</Index>  
    <Index>18</Index>  
    <Index>22</Index>  
    <Index>24</Index>  
    <Index>25</Index>  
    <Index>26</Index>  
    <Index>28</Index>  
    <Index>30</Index>  
    <Index>32</Index>  
    <Index>33</Index>  
    <Index>35</Index>  
    <Index>38</Index>  
    <Index>41</Index>  
    <Index>43</Index>  
    <Index>47</Index>  
    <Index>52</Index>  
    <Index>57</Index>  
    <Index>58</Index>  
    <Index>60</Index>  
    <Index>63</Index>  
    <Index>66</Index>  
    <LatLongTolerance>0.000220577</LatLongTolerance>  
  </RoutePathGeneralization>-<RoutePathGeneralization>  
    <Index>0</Index>  
    <Index>15</Index>  
    <Index>25</Index>  
    <Index>30</Index>  
    <Index>41</Index>  
    <Index>47</Index>  
    <Index>66</Index>  
    <LatLongTolerance>0.00188803</LatLongTolerance>  
  </RoutePathGeneralization>-<RoutePathGeneralization>  
    <Index>0</Index>  
    <Index>66</Index>  
    <LatLongTolerance>0.016986</LatLongTolerance>  
  </RoutePathGeneralization>-<RoutePathGeneralization>  
    <Index>0</Index>  
    <Index>66</Index>  
    <LatLongTolerance>0.095013</LatLongTolerance>  
  </RoutePathGeneralization>-<RoutePathGeneralization>  
    <Index>0</Index>  
    <Index>66</Index>  
    <LatLongTolerance>0.846703</LatLongTolerance>  
  </RoutePathGeneralization>  
</RoutePath>  
  
```  
  
## See Also  
 [Using the REST Services with .NET](../using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../json-data-contracts.md)