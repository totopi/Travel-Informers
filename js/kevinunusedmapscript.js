// A test map script when I thought we might be doing a scrape and map project
// It turns out our project changed form because things are never as free and plentiful as one would hope..

// Get the data from the route I set up in the flask app
d3.json("/city", function(data) {
    // Go to this function and get things
    makeMap(data);
})

function makeMap(data) {
    // Takes in data, makes a map out of it
    
    // Let's look at that juicy data
    console.log(data);

    // Make an empty list to later pushulate (not populate because pop removes things)
    let markers = [];
    // Loop through the data to pull out the stuff we want from each index
    for (let i = 0, ii = data.length; i < ii; i++) {
        // Singular of data is..
        let datum = data[i];

        // Pushulate, not populate, the empty list
        markers.push(
            L.marker([datum.lat, datum.lon], {
                draggable: false,
                title: datum.city_name
            }).bindPopup(`<strong>${datum.city_name}, ${datum.country}</strong><hr>`)
        )
    }

    // Start zoomed out over the US probably
    let startCoords = [34.052231, -118.243683];
    let startZoom = 6;

    // Maps are more fun with options, but after making this I discovered the joy of the v4 mapbox maps...
    let streetMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoidG90b3BpIiwiYSI6ImNqaDFhaGh6ejAxcW4yeHJ5aDl4bjZ2YngifQ.ssPdnszdafCcNm4753AVJA");
    let darkMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoidG90b3BpIiwiYSI6ImNqaDFhaGh6ejAxcW4yeHJ5aDl4bjZ2YngifQ.ssPdnszdafCcNm4753AVJA");

    // Typical leaflet layer control type things
    let cityLayer = L.layerGroup(markers);

    let baseMaps = {
        "Street Map": streetMap,
        "Dark Map": darkMap
    };

    let overlayMaps = {
        "Cities": cityLayer
    };

    let myMap = L.map('map', {
        center: startCoords,
        zoom: startZoom,
        layers: [streetMap, cityLayer]
    });
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);

}

// Making maps is fun, but this is not the direction we ended up going in.  So far...