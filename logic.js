// var weather = final.csv
// var hurricane = convertcsv-small.geojson

// get data
d3.csv("final.csv", function(data) {
    //createFeatures(data.features);
    console.log(data[0])
});

// define map

function createMap(layers) {

    // Define map layers
    var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamVsaXphbG8iLCJhIjoiY2pneWI3b2szMDF6YzMzbXoxMGFpdnlzdSJ9.eFiZjkE9_VHob0oOHTauSQ");
  
    var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamVsaXphbG8iLCJhIjoiY2pneWI3b2szMDF6YzMzbXoxMGFpdnlzdSJ9.eFiZjkE9_VHob0oOHTauSQ");

    var lightMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamVsaXphbG8iLCJhIjoiY2pneWI3b2szMDF6YzMzbXoxMGFpdnlzdSJ9.eFiZjkE9_VHob0oOHTauSQ");
    
      // Define base maps
    var baseMaps = {
        "Light Map": lightMap,
        "Outdoors": outdoors,
        "Satellite": satellite
  
    }};

    // map =

    // map.addSource('hurricane', {
    //     type: 'geojson',
    //     data: 'csvconvert1.geojson'
    // });
    // map.addLayer({
    //     id: 'hurricane',
    //     source: 'hurricane',
    //     type: 'heatmap'
    // });

    // var hurricane = new L.LayerGroup();

    // var overlayMaps = {
    //     "Temperature": data,
    //     "Hurricane": hurricane
    // };

    var map = L.map("map", {
        center: [40.7128, -74.0059],
        zoom: 11
      });

    function gatherDataPoints(hurricane){

        L.geoJson(hurricane).addTo(map);
      };
    
      $.getJSON("convertcsv-small.geojson", gatherDataPoints);
     
     // $.getJSON("convertcsv2.geojson", gatherDataPoints);

    //  //Add layer control to map
    //  L.control.layers(baseMaps, overlayMaps, {
    //     collapsed: false
    // }).addTo(myMap);


    //  legend.addTo(myMap);

    