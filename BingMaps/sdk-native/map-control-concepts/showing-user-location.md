
# Showing the user location on the MapView

User location is controlled by two properties: UserLocationTrackingMode and UserLocationVisible. UserLocationVisible controls whether to display the user location on the map and UserLocationTrackingMode allows the developer to have the map track the user location either always or in an interruptible manner that allows the user to stop tracking by interacting with the map to change the view.

## Examples

### Toggle tracking the user location

**Android**

In AndroidManifest.xml use the permissions ACCESS_COARSE_LOCATION and ACCESS_FINE_LOCATION:

>```java
><uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />  
><uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
>```

Add some Java code to handle OnRequestPermissionsResultCallback and to enable user location tracking:

>```java
>public void toggleMyLocation()
>{
>  boolean visibility = !mMap.getUserLocationVisible();
>  LocationStatus status = mMap.setUserLocationVisible(visibility, 1);
>  if (status != LocationStatus.SUCCESS)
>  {
>    mMap.setUserLocationTrackingMode(UserLocationTrackingMode.INTERRUPTIBLE_CENTERED_ON_USER);
>  }
>  else
>  {
>    // handle error.
>  }
>}
>
>// Elsewhere in code, our Activity class needs to implement ActivityCompat.OnRequestPermissionsResultCallback. 
>@Override
>public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults)
>{
>  if (requestCode == 1)
>  {
>    boolean permissionGranted = false;
>    for (int grantResult : grantResults)
>    {
>      if (grantResult == PackageManager.PERMISSION_GRANTED)
>      {
>        permissionGranted = true;
>      }
>    }
>    // If at least one new permission was granted toggle on my location.
>    if (permissionGranted)
>    {
>      toggleMyLocation();
>    }
>  }
>}
>```
