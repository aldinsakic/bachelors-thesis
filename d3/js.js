function onLoad(p) {
  //clear for filtering
  document.getElementById('vizDiv').innerHTML = '';
  // // import {legend} from "@d3/color-legend"

// // set the dimensions and margins of the graph
// const margin = {top: 30, right: 30, bottom: 30, left: 30},
//   width = 600 - margin.left - margin.right,
//   height = 600 - margin.top - margin.bottom;

// // append the svg object to the body of the page
// const svg = d3.select("#vizDiv")
// .append("svg")
//   .attr("width", width + margin.left + margin.right)
//   .attr("height", height + margin.top + margin.bottom)
// .append("g")
//   .attr("transform", `translate(${margin.left},${margin.top})`);

//   // Labels of row and columns
//   const groups = ["2023", "2022", "2021", "2020", "2019", "2017", "2015", "2013"];
//   const vars = ["BE","BG","CZ","DK","DE","EE","IE","EL","ES","FR","HR","IT","CY","LV","LT","LU","HU","MT","NL","AT","PL","PT","RO","SI","SK","FI","SE"];
  
  
//   // Build X scales and axis:
//   const x = d3.scaleBand()
//   .range([width, 0])
//   .domain(groups)
//   //.padding(0.01);
//   svg.append("g")
//   .attr("transform", `translate(0, ${height})`)
//   .call(d3.axisBottom(x))
  
//   // Build y scales and axis:
//   const y = d3.scaleBand()
//   .range([height, 0])
//   .domain(vars)
//   //.padding(0.01);
//   svg.append("g")
//   .call(d3.axisLeft(y));


// //svg.selectAll(".secondrow").data(data).enter().append("circle").attr("cx", function(d,i){return 30 + i*60}).attr("cy", 250).attr("r", 19).attr("fill", function(d){return myColor(d) })

// // const tooltip = d3.select("#vizDiv")
// //   .append("div")
// //   .style("opacity", 0)
// //   .attr("class", "tooltip")
// //   .style("background-color", "white")
// //   .style("border", "solid")
// //   .style("border-width", "2px")
// //   .style("border-radius", "5px")
// //   .style("padding", "5px")

// const mouseleave = function(event,d) {
//   value
//     .style("opacity", 0)
//   // d3.select(this)
//   //   .style("stroke", "none")
//   //   .style("opacity", 0.8)
// }

// const value = d3.select("#vizDiv")
//   .append("p")

// const mouseover = function(event,d) {
//   // let thisX = event.target.attributes[0].nodeValue;
//   // let thisY = event.target.attributes[1].nodeValue;
//   value
//     //.style("margin", Math.round(thisX)+"px")
//     .style("opacity", 1)
//     //.append("text")
//     .html(d.value)
//   //   .style("opacity", 1)
//   // d3.select(this)
//   //   .style("stroke", "black")
//   //   .style("opacity", 1)
//   //console.log(d.value);
// }
// //Read the data
// d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/standardDateGEI.csv").then( function(data) {
  

//   // const mousemove = function(event,d) {
//   //   value
//   //     //.html(d.value)
//   //     //.style("left", (event.x)/2 + "px")
//   //     //.style("top", (event.y)/2 + "px")
//   //   console.log(d);
      
//   // }
  
//   // figure out the max and min values, to be used in the color scale
//   let tmpArray = [];
//   for (var i=0; i<data.length; i++) {
//     row = data[i];
//     tmpArray.push(row['value'])
//   }
//   const maxValue = Math.max.apply(null, tmpArray);
//   const minValue = Math.min.apply(null, tmpArray);
//   // Build color scale
//   const myColor = d3.scaleSequential().domain([minValue,maxValue]).interpolator(d3.interpolateViridis);
  
//   //svg.selectAll()
//   // this is so borked, fix time 
//   svg.selectAll()
//   .data(data, function(d) {return d})
//   .enter()
//   .append("rect")
//     .attr("x", function(d) { return x(d.group)})
//     .attr("y", function(d) { return y(d.variable)})
//     .attr("width", x.bandwidth() )
//     .attr("height", y.bandwidth() )
//     .style("fill", function(d) { return myColor(d.value)} )
//     //.style("stroke-width", 1)
//     //.style("stroke", "none")
//     //.style("opacity", 1)
//     .on("mouseover", mouseover)
//     //.on("mousemove", mousemove)
//     .on("mouseleave", mouseleave)
//   // .append("text").attr("x", 500).attr("y", 599).text("variable A").style("font-size", "15px").attr("alignment-baseline","middle")
// })

// set the dimensions and margins of the graph
const margin = {top: 80, right: 25, bottom: 30, left: 50},
  width = 800 - margin.left - margin.right,
  height = 800 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#vizDiv")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

//Read the data
d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/standardDateGEI.csv").then(function(data) {

  // Labels of row and columns -> unique identifier of the column called 'group' and 'variable'
  // const groups = Array.from(new Set(data.map(d => d.group)))
  // const vars = Array.from(new Set(data.map(d => d.variable)))
  // var xValues = new Array();
  // var yValues = new Array();
  // var zValues = new Array();
  // var newData = new Array();
  // for (var i=0; i<data.length; i++) {
    // filter, 0 = all
    // row = data[i];
    // if (p==0) {
    //     // console.log(row);
        // xValues.push(row['group']);
        // yValues.push(row['variable']);
    //     // zValues.push(Array.of(row['group'], row['variable'], row['value'],));
        // zValues[i]=row['value'];
        // newData.group = row['group'];
        // newData.variable = row['variable'];
    // }
    // else{
        // if ((row['group'] == p) || (row['variable'] == p)) {
            // xValues.push(row['group']);
            // yValues.push(row['variable']);
            // zValues.push(row['value']);
            // groups=''
        // }
    // }
    // else if (row['group'] == p) {
      // data.filter(function(d){ return d.group == p })
    // }
    // else{
      // data.filter(function(d){ return d.group == p })
      // console.log(data);
    // }

    // console.log(xValues, yValues, zValues);
  // }
  // newData.push(xValues, yValues, zValues)
  // console.log(newData);
  if (p != 0) {
    var groups = data.filter(function (d) { return p.indexOf(d.group) <= 0 }).map(d => d.group);
  }
  else {
    var groups = Array.from(new Set(data.map(d => d.group)));
  }
  // filter where name is not like p
  // const groups = Array.from(new Set(data.filter(function(d){ return d.group != p }).map(d => d.group)))
  const vars = Array.from(new Set(data.map(d => d.variable)))
  // console.log(groups, vars);

    // figure out the max and min values, to be used in the color scale
  // let tmpArray = [];
  // for (var i=0; i<data.length; i++) {
  //   row = data[i];
  //   tmpArray.push(row['value'])
  // }
  // const maxValue = Math.max.apply(null, tmpArray);
  // const minValue = Math.min.apply(null, tmpArray);
  // console.log(maxValue, minValue);
  // Build color scale
  //const myColor = d3.scaleSequential().domain([minValue,maxValue]).interpolator(d3.interpolateViridis);

  // Build X scales and axis:
  const x = d3.scaleBand()
    .range([ 0, width ])
    .domain(groups)
    // .padding(0.05);
  svg.append("g")
    .style("font-size", 15)
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x).tickSize(0))
    .select(".domain").remove()

  // Build Y scales and axis:
  const y = d3.scaleBand()
    .range([ height, 0 ])
    .domain(vars)
    // .padding(0.05);
  svg.append("g")
    .style("font-size", 15)
    .call(d3.axisLeft(y).tickSize(0))
    .select(".domain").remove()

  // Build color scale
  const myColor = d3.scaleSequential()
    .interpolator(d3.interpolateViridis)
    // hard coded min and max values, change later
    .domain([48.6, 83.9])


  // create a tooltip
  const tooltip = d3.select("#vizDiv")
    .append("div")
    .style("opacity", 0)
    .attr("class", "tooltip")
    .style("background-color", "white")
    // .style("border", "solid")
    // .style("border-width", "2px")
    // .style("border-radius", "5px")
    // .style("padding", "5px")

  // Three function that change the tooltip when user hover / move / leave a cell
  const mouseover = function(event,d) {
    tooltip
      .style("opacity", 1)
    d3.select(this)
      // .style("stroke", "black")
      .style("opacity", 1)
  }
  const mousemove = function(event,d) {
    tooltip
      .html("Value: " + d.value + ", Date: " + d.variable + ", Country: " + d.group)
      .style("left", (event.x)/2 + "px")
      .style("top", (event.y)/2 + "px")
  }
  const mouseleave = function(event,d) {
    tooltip
      .style("opacity", 0)
    d3.select(this)
      // .style("stroke", "none")
      // .style("opacity", 0.8)
  }

  // add the squares
  svg.selectAll()
    .data(data, function(d) {return d.group+':'+d.variable;})
    .join("rect")
      .attr("x", function(d) { return x(d.group) })
      .attr("y", function(d) { return y(d.variable) })
      // .attr("rx", 4)
      // .attr("ry", 4)
      .attr("width", x.bandwidth() )
      .attr("height", y.bandwidth() )
      .style("fill", function(d) { return myColor(d.value)} )
      // .style("stroke-width", 4)
      .style("stroke", "none")
      // .style("opacity", 0.8)
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave)
})

// Add title to graph
svg.append("text")
        .attr("x", 0)
        .attr("y", -50)
        .attr("text-anchor", "left")
        .style("font-size", "14px")
        .text("GEI in EU across all avaliable years, interactive heatmap");

// Add subtitle to graph
// svg.append("text")
        // .attr("x", 0)
        // .attr("y", -20)
        // .attr("text-anchor", "left")
        // .style("font-size", "14px")
        // .style("fill", "grey")
        // .style("max-width", 400)
        // .text("A short description of the take-away message of this chart.");
}
