# Anchoring MapIcons

One of the most common issues developers come across when using custom MapIcons is that when they zoom the map it appears as if their MapIcon is drifting to or from the location it is meant to be anchored to. This is due to an incorrect anchor point value in the pushpin options. The anchor point specifies which pixel coordinate of the image, relative to the top left corner of the image, should overlap the pushpins location coordinate.
  
For example, consider the following MapIcon, which is 24 pixels wide and 36 pixels tall. For this pushpin we would want the bottom point of the pushpin to align with the pushpins location coordinate which in this case would need an x offset that is half the wide and a y offset equal to the height of the image. This would require an anchor point of (0.5, 1.0):

![MapIcon Dimensions](media/bmv8-anchoring-pushpins-dimensions.png)

Here are some additional MapIcon images and anchor values that can be used to properly position the image.  

![Aligned with Center](media/bmv8-anchoring-pushpins-align-center.png)  
Align with Center Anchor: (0.5f, 0.5f)  

![Aligned with Point](media/bmv8-anchoring-pushpins-align-with-point.png)  
Align with Point Anchor: (0.2f, 1.0f)  

![Aligned Pushpin](media/bmv8-anchoring-pushpins-align-pushpin.png)  
Align with Point Anchor: (0.2f, 1.0f)
