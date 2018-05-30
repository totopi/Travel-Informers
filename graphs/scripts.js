let url = "json.json"
d3.json(url, function(json) {
  
    // First Graph
    let trace1 = {
        x: json[0][0]['x'],
        y: json[0][0]['y'],
        name: json[0][0]['name'],
        type: json[0][0]['type'],
        mode: json[0][0]['mode'],
        marker: { color : '#226CC1' }
    };
    let trace2 = {
        x: json[0][1]['x'],
        y: json[0][1]['y'],
        name: json[0][1]['name'],
        type: json[0][1]['type'],
        mode: json[0][1]['mode'],
        marker: { color : '#83727E' }
    };
    let trace3 = {
        x: json[0][2]['x'],
        y: json[0][2]['y'],
        name: json[0][2]['name'],
        type: json[0][2]['type'],
        mode: json[0][2]['mode'],
        marker: { color : '#5AC523' }
    };
    let data = [trace1, trace2, trace3];
    let layout = {
        title: "Temperature vs Date", 
        xaxis: {
            title: "Dates",
        },
        yaxis: {
            title: "Temperature, Degrees Fahrenheit"
        },
        paper_bgcolor:'rgba(90, 197, 35, 0.5)',
        plot_bgcolor:'rgba(90, 197, 35, 0)'

    };
    Plotly.newPlot('first_graph', data, layout);

    // Second Graph 

    // Debug: console.log(json[1][0]['type'])

    let trace = {
        x: json[1][0]['x'],
        y: json[1][0]['y'],
        name: json[1][0]['name'],
        mode: json[1][0]['mode'],
        type: json[1][0]['type'],
        text: json[1][0]['text'],
        marker: json[1][0]['marker']
    };
    let data2 = [trace];
    let layout2 = {
        title: "Temperature vs Number of Airport Delays",
        xaxis: {
            title: "Temperature"
        },
        yaxis: {
            title: "Number of Airport Delays"
        },
        paper_bgcolor:'rgba(90, 197, 35, 0.5)',
        plot_bgcolor:'rgba(90, 197, 35, 0)'
    };

    Plotly.newPlot('second_graph', data2, layout2);

    // Third Plot
    // Debug: console.log(json[2][0]['values'])
    let pie_trace = {
        values:json[2][0]['values'],
        labels:json[2][0]['labels'],
        type: json[2][0]['type'],
        hole: json[2][0]['hole'],
        marker: json[2][0]['marker'],
        textinfo: json[2][0]['textinfo'],
        name: json[2][0]['name']
    };
    let pie_data = [pie_trace]
    let pie_layout = {
        title: "Something vs Weather Conditions",
        height: 700,
        width: 800,
        paper_bgcolor:'rgba(90, 197, 35, 0.5)',
        plot_bgcolor:'rgba(90, 197, 35, 0)'
    };
    Plotly.newPlot("third_graph", pie_data, pie_layout)
});