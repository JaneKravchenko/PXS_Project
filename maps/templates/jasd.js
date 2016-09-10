/**
 * Created by jane on 10.09.16.
 */

var lon = 135.0658519;
var lat = 48.466571;
var zoom = 16;
var options = {
	projection: new OpenLayers.Projection("EPSG:900913"),
	displayProjection: new OpenLayers.Projection("EPSG:4326"),
	maxExtent: new OpenLayers.Bounds(-20037508.34, -20037508.34, 20037508.34, 20037508.34)
};
function inizialize() {
    map = new OpenLayers.Map('map5', options);


    var layer = new OpenLayers.Layer.Google(
        "GoogleSoft", {
            type: G_SATELLITE_MAP,
            numZoomLevels: 20,
            'sphericalMercator': true
        });
    map.addLayer(layer);

    var myKML = new OpenLayers.Layer.GML(
        "KML",
        "test.kml", {
            format: OpenLayers.Format.KML,
            projection: map.displayProjection
        });
    map.addLayer(myKML);

    var proj = new OpenLayers.Projection("EPSG:4326");
    var point = new OpenLayers.LonLat(lon, lat);
    map.setCenter(point.transform(proj, map.getProjectionObject()), zoom);
}