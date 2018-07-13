var weatherData = "final.csv"
var small = "convertercsv-small.geojson"


// get data
d3.csv(weatherData, function (weather) {
    //createFeatures(data.features);
    console.log(weather[0])
});

var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamVsaXphbG8iLCJhIjoiY2pneWI3b2szMDF6YzMzbXoxMGFpdnlzdSJ9.eFiZjkE9_VHob0oOHTauSQ");

var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamVsaXphbG8iLCJhIjoiY2pneWI3b2szMDF6YzMzbXoxMGFpdnlzdSJ9.eFiZjkE9_VHob0oOHTauSQ");

var lightMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamVsaXphbG8iLCJhIjoiY2pneWI3b2szMDF6YzMzbXoxMGFpdnlzdSJ9.eFiZjkE9_VHob0oOHTauSQ");

// Define base maps
var baseMaps = {
    "Light Map": lightMap,
    "Outdoors": outdoors,
    "Satellite": satellite
}

// var baseLayer = L.tileLayer(
//     'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
//       attribution: '...',
//       maxZoom: 18
//     }
//   );

//   var cfg = {
//     // radius should be small ONLY if scaleRadius is true (or small radius is intended)
//     // if scaleRadius is false it will be the constant radius used in pixels
//     "radius": 2,
//     "maxOpacity": .8, 
//     // scales the radius based on map zoom
//     "scaleRadius": true, 
//     // if set to false the heatmap uses the global maximum for colorization
//     // if activated: uses the data maximum within the current map boundaries 
//     //   (there will always be a red spot with useLocalExtremas true)
//     "useLocalExtrema": true,
//     // which field name in your data represents the latitude - default "lat"
//     latField: 'lat',
//     // which field name in your data represents the longitude - default "lng"
//     lngField: 'lng',
//     // which field name in your data represents the data value - default "value"
//     valueField: 'count'
//   };
  
//   var heatmapLayer = new HeatmapOverlay(cfg);

  
//   heatmapLayer.setData(weather);

var map = L.map("map", {
    center: [29.365721, -35.004062],
    zoom: 2,
    layers: Object.values(baseMaps)
});
// satellite.addTo(map)


 //Add layer control to map
L.control.layers(baseMaps, [outdoors], {
    collapsed: false
}).addTo(map);


//Create a marker layer (in the example done via a GeoJSON FeatureCollection)
var sliderControl = L.control.sliderControl({position: "topright", layer: lightMap});

//Make sure to add the slider to the map ;-)
map.addControl(sliderControl);

//And initialize the slider
sliderControl.startSlider();

// var testlayer = L.geoJson(json);
// var sliderControl = L.control.sliderControl({position: "topright", layer: testlayer});

// //Make sure to add the slider to the map ;-)
// map.addControl(sliderControl);

// //And initialize the slider
// sliderControl.startSlider();

    //  legend.addTo(myMap);

