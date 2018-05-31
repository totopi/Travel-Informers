// All the scripts!

// Use the route /city to populate our dropdown menu for cities
let citySelect = document.querySelector("#citySelect");
d3.json("/city", function(error, cities) {
    if (error) throw error;
    let longness = cities.length;
    for (let i = 0; i < longness; i++) {
        if (cities[i]["country"] === "United States") {
            let city = d3.select("#selCity").append("option").attr("value", cities[i]["city_name"]).text(cities[i]["city_name"]);
        }
    }
})

// Set up the dropdown menus for month and type
let monthText = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let monthValue = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"];
let monthSelect = document.querySelector("#monthSelect");
for (let i = 0; i < 12; i++) {
    let month = d3.select("#selMonth").append("option").attr("value", monthValue[i]).text(monthText[i]);
}
let typeText = ["Temperature", "Wind Speed", "Humidity"];
let typeValue = ["temp", "wind", "humidity"];
let typeSelect = document.querySelector("#typeSelect");
for (let i = 0; i < 3; i++) {
    let types = d3.select("#selType").append("option").attr("value", typeValue[i]).text(typeText[i]);
}

// Update things every time something changes - looking at the docs, Plotly.react is about as good as restyle but we can just feed it all of our new data instead of just what's changed
// Which is a lot.
function somethingChanged() {
    let thisCity = document.querySelector("#selCity").value;
    let thisMonth = document.querySelector("#selMonth").value;
    let thisType = document.querySelector("#selType").value;
    url = `/${thisCity}/${thisMonth}/${thisType}`;
    let timeSeries = document.querySelector("#first_graph");
    let scatter = document.querySelector("#second_graph");
    let donut = document.querySelector("#third_graph");
    d3.json(url, function(data) {
        Plotly.react(timeSeries, data[0], data[3]);
        Plotly.react(scatter, data[1], data[4]);
        Plotly.react(donut, data[2], data[5]);
    })
    renderPics(thisCity);
}

// Initialize our graphs
function initGraphs() {
    let url = `/Portland/01/temp`;

    d3.json(url, function(error, json) {
        if (error) throw error;
        // First Graph
        Plotly.react('first_graph', json[0], json[3]);

        // Second Graph 
        Plotly.react('second_graph', json[1], json[4]);

        // Third Plot
        Plotly.react("third_graph", json[2], json[5]);
    });

    // It took far too long to get this stuff to cooperate, I'm sure there's a better way, but thanks for the code Corey!
    d3.json('/city_pics/Portland', function (err, urlData) {
        if (err) throw err;
        let picSpots = d3.select('#collage').selectAll('div')
                        .data(urlData)
                        .enter()
                        .append('div')
                        .classed('w3-container', true)
                        .classed('w3-cell', true)
                        .classed('cover', true)
                        .html(function(d){
                            return `<img src="${d}" style="height: 300px; width: 200px; object-fit: cover;">`
                        })
    });
}
initGraphs();

function renderPics(city){
    // this stuff is for when it's actually in the main page and can grab city
    // let city = document.querySelector("#selCity").value; // idk why but I'd prefer to have city called as an argument -Kevin
    d3.select('#collage').selectAll('div').remove();
    let picUrl = `/city_pics/${city}`;
    d3.json(picUrl, function (err, urlData) {
        if (err) throw err;
        console.log(urlData);
        let picSpots = d3.select('#collage').selectAll('div').data(urlData);
        picSpots.enter()
                .append('div')
                .classed('w3-container', true)
                .classed('w3-cell', true)
                .classed('cover', true)
                .html(d => `<img src="${d}" style="height: 300px; width: 200px; object-fit: cover;">`)
    });
};