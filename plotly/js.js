function onLoad(p) {
    Plotly.d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/standardDateGEI.csv", function(allData){
        console.log(allData);
        // console.log(allData);

        // var xValues = ['A', 'B', 'C', 'D', 'E'];

        // var yValues = ['W', 'X', 'Y', 'Z'];

        // var zValues = [
        // [0.00, 0.00, 0.75, 0.75, 0.00],
        // [0.00, 0.00, 0.75, 0.75, 0.00],
        // [0.75, 0.75, 0.75, 0.75, 0.75],
        // [0.00, 0.00, 0.00, 0.75, 0.00]
        // ];
        //var xValues = new Array();
        // var yValues = new Array();
        // var xValues = ["2013", "2015", "2017", "2019", "2020", "2021", "2022", "2023"];
        // var groups = ["2013", "2015", "2017", "2019", "2020", "2021", "2022", "2023"];
        // var yValues = ["BE","BG","CZ","DK","DE","EE","IE","EL","ES","FR","HR","IT","CY","LV","LT","LU","HU","MT","NL","AT","PL","PT","RO","SI","SK","FI","SE"];
        // var countries = ["BE","BG","CZ","DK","DE","EE","IE","EL","ES","FR","HR","IT","CY","LV","LT","LU","HU","MT","NL","AT","PL","PT","RO","SI","SK","FI","SE"];
        // var zValues = new Array();
        // for (var i=0; i<allData.length; i++) {
        //     // filter, 0 = all
        //     row = allData[i];
        //     if (p==0) {
        //     //     // console.log(row);
        //         xValues.push(row['group']);
        //         yValues.push(row['variable']);
        //     //     // zValues.push(Array.of(row['group'], row['variable'], row['value'],));
        //         zValues[i]=row['value'];
        //     }
        //     else{
        //         if ((row['group'] == p) || (row['variable'] == p)) {
        //             xValues.push(row['group']);
        //             yValues.push(row['variable']);
        //             zValues.push(row['value']);
        //             // groups=''
        //         }
        //     }

        //     // console.log(xValues, yValues, zValues);
        //   }
        //   console.log(xValues, yValues, zValues);
        // xValues = allData.filter(function(d){ return d.group != p }).map(d => d.group);
        // if (p!=0) {
        var xValues = Array.from(allData.filter(function(d){ return p.indexOf(d.group) >= 0 } ).map(d => d.group));
        // }
        // else{
            // xValues = allData.map(d => d.group);
        // }
        var yValues = Array.from(allData.map(d => d.variable));
        // var zValues = Array.from(allData.map(d => d.value));
        var zValues = Array.from(allData.filter(function(d){ return p.indexOf(d.group) >= 0 } ).map(d => d.value));

        
        console.log(xValues, yValues, zValues);

        // var colorscaleValue = ['Viridis'];

        var data = [{
            x: xValues,
            y: yValues,
            z: zValues,
            type: 'heatmap',
            colorscale: 'Viridis',
            showscale: false,
            // transforms: [{
            //     type: 'filter',
            //     target: 'yValues',
            //     operation: '>',
            //     value: 3
            //   }]
        }];

        var layout = {
        title: 'GEI in EU across all avaliable years, interactive heatmap',
        // automargin: false,
        autosize: true,
        height: 800,
        width: 800,
        automargin: false,
        // xref: 10000,
        // update_layout: {yaxis_scaleanchor:"x"},
        // size:'dummy_column_for_size',
        // size_max:15,
        // margin: {
            //     dictt:100, b:0, l:80, r:0
            // },
            //annotations: [],
            // cells: {
            //     height: 10,
            //     width: 10,
            // },
        xaxis: {
            // tickformat: '%d %B (%a)<br>%Y'
            // showgrid:true,
            // ticks:"outside",
            // tickson:"boundaries",
            // ticklen:20
            // tickmode : 'array',
            // tickvals : [0,1,2,3,4,5,6,7],
            // ticktext : groups,
            // range: groups,
            // tickmode: 'auto',
            // ticktext: groups,    
            // tickvals: [1, 3, 5, 7, 9, 11],
            // constrain: 'domain',
            // ticks: '',
            // ticksuffix: ' ',
            //width: 700,
            //height: 700,
            // autosize: true
        },
        yaxis: {
        // tickmode : 'array',
        // tickvals : [0,1,2,3,4,5,6,7],
        // ticktext : groups,
        //ticks: '',
        //ticksuffix: ' ',
        //width: 700,
        //height: 700,
        // autosize: true
        }
        };

        // for ( var i = 0; i < yValues.length; i++ ) {
        // for ( var j = 0; j < xValues.length; j++ ) {
        //     var currentValue = zValues[i][j];
        //     if (currentValue != 0.0) {
        //     var textColor = 'white';
        //     }else{
        //     var textColor = 'black';
        //     }
        //     var result = {
        //     xref: 'x1',
        //     yref: 'y1',
        //     x: xValues[j],
        //     y: yValues[i],
        //     text: zValues[i][j],
        //     font: {
        //         family: 'Arial',
        //         size: 12,
        //         color: 'rgb(50, 171, 96)'
        //     },
        //     showarrow: false,
        //     font: {
        //         color: textColor
        //     }
        //     };
        //     layout.annotations.push(result);
        // }
        // }

        Plotly.newPlot('viz', data, layout, {displayModeBar: false})
    })
}
