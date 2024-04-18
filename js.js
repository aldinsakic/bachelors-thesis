// set the dimensions and margins of the graph
const margin = {top: 30, right: 30, bottom: 30, left: 30},
  width = 400 - margin.left - margin.right,
  height = 700 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#my_dataviz")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

  // Labels of row and columns
  const myGroups = ["2013", "2015", "2017", "2019", "2020", "2021", "2022", "2023"];
  const myVars = ["BE","BG","CZ","DK","DE","EE","IE","EL","ES","FR","HR","IT","CY","LV","LT","LU","HU","MT","NL","AT","PL","PT","RO","SI","SK","FI","SE"];
  
  
  // Build X scales and axis:
  const x = d3.scaleBand()
  .range([ 0, width ])
  .domain(myGroups)
  .padding(0.01);
  svg.append("g")
  .attr("transform", `translate(0, ${height})`)
  .call(d3.axisBottom(x))
  
// Build X scales and axis:
const y = d3.scaleBand()
  .range([ height, 0 ])
  .domain(myVars)
  .padding(0.01);
svg.append("g")
  .call(d3.axisLeft(y));

// Build color scale
const myColor = d3.scaleSequential().domain([45,100])
  .interpolator(d3.interpolateViridis);
//svg.selectAll(".secondrow").data(data).enter().append("circle").attr("cx", function(d,i){return 30 + i*60}).attr("cy", 250).attr("r", 19).attr("fill", function(d){return myColor(d) })

// const tooltip = d3.select("#my_dataviz")
//   .append("div")
//   .style("opacity", 0)
//   .attr("class", "tooltip")
//   .style("background-color", "white")
//   .style("border", "solid")
//   .style("border-width", "2px")
//   .style("border-radius", "5px")
//   .style("padding", "5px")


//Read the data
d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/GEI.csv").then( function(data) {
  console.log(data);

  const value = d3.select("#my_dataviz")
    .append("p")

  const mouseover = function(event,d) {
    let thisX = console.log(event.target.attributes[0].nodeValue);
    let thisY = console.log(event.target.attributes[1].nodeValue);
    value
      //.style("margin", Math.round(thisX)+"px")
      .style("opacity", 1)
      //.append("text")
      .html(d.value)
        
    //   .style("opacity", 1)
    // d3.select(this)
    //   .style("stroke", "black")
    //   .style("opacity", 1)
    //console.log(d.value);
  }
  const mousemove = function(event,d) {
    value
      //.html(d.value)
      //.style("left", (event.x)/2 + "px")
      //.style("top", (event.y)/2 + "px")
    console.log(d);
      
  }
  const mouseleave = function(event,d) {
    value
      .style("opacity", 0)
    // d3.select(this)
    //   .style("stroke", "none")
    //   .style("opacity", 0.8)
  }


  //svg.selectAll()
  svg.selectAll()
  .data(data, function(d) {return d.group+':'+d.variable;})
  .enter()
  .append("rect")
    .attr("x", function(d) { return x(d.group)+1 })
    .attr("y", function(d) { return y(d.variable)+1 })
    .attr("width", x.bandwidth()-2 )
    .attr("height", y.bandwidth()-2 )
    .style("fill", function(d) { return myColor(d.value)} )
    .style("stroke-width", 1)
    .style("stroke", "none")
    .style("opacity", 1)
    .on("mouseover", mouseover)
    //.on("mousemove", mousemove)
    .on("mouseleave", mouseleave)
  // .append("text").attr("x", 500).attr("y", 599).text("variable A").style("font-size", "15px").attr("alignment-baseline","middle")
})