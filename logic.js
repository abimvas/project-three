var weather = []

// get data
d3.csv("final.csv", function(data) {
    createFeatures(data.features);
    console.log(weather)
});

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

    map.addSource('earthquakes', {
        type: 'geojson',
        data: 'earthquakes.geojson'
    });
    map.addLayer({
        id: 'earthquakes',
        source: 'earthquakes',
        type: 'heatmap'
    });

    