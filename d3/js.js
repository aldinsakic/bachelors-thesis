var i = 0;
var filters = [['BE'], ['FI'], ['FI', 'DK'], ['BE', 'DK'], ['BE', 'DK', 'SE', 'IT'], ['FI', 'DK', 'SE', 'IT']];
function onLoad(p) {
  // read the data
  d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/standardDateGEI.csv").then(function (data) {
    // get the time for start of filtration.
    localStorage.setItem("filterStartTime", localStorage.getItem("filterStartTime") + ', ' + Date.now())
    //clear for filtering
    document.getElementById('vizDiv').innerHTML = '';

    // set the dimensions and margins of the graph
    const margin = { top: 80, right: 25, bottom: 30, left: 50 },
      width = 800 - margin.left - margin.right,
      height = 800 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    const svg = d3.select("#vizDiv")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", `translate(${margin.left}, ${margin.top})`);

    // filter on p
    var groups = Array.from(new Set(data.filter(function (d) { return p.indexOf(d.group) >= 0 }).map(d => d.group)));
    var vars = Array.from(new Set(data.map(d => d.variable)))

    // Build X scales and axis:
    const x = d3.scaleBand()
      .range([0, width])
      .domain(groups)
    svg.append("g")
      .style("font-size", 15)
      .attr("transform", `translate(0, ${height})`)
      .call(d3.axisBottom(x).tickSize(0))
      .select(".domain").remove()

    // Build Y scales and axis:
    const y = d3.scaleBand()
      .range([height, 0])
      .domain(vars)
    svg.append("g")
      .style("font-size", 15)
      .call(d3.axisLeft(y).tickSize(0))
      .select(".domain").remove()

    // Build color scale
    const colorScale = d3.scaleSequential()
      .interpolator(d3.interpolateViridis)
      // TODO hard coded min and max values, change later
      .domain([48.6, 83.9])


    // create a tooltip
    const tooltip = d3.select("#vizDiv")
      .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")

    // Three function that change the tooltip when user hover / move / leave a cell
    const mouseover = function (event, d) {
      tooltip
        .style("opacity", 1)
      d3.select(this)
        .style("opacity", 1)
    }
    const mousemove = function (event, d) {
      tooltip
        .html("x: " + d.group + ", y: " + d.variable + ", z: " + d.value)
      // TODO doesnt move with the mouse, idk why
      // .style("left", (event.x)/2 + "px")
      // .style("top", (event.y)/2 + "px")
    }
    const mouseleave = function (event, d) {
      tooltip
        .style("opacity", 0)
    }

    // add the squares
    svg.selectAll()
      .data(data.filter(function (d) { return p.indexOf(d.group) >= 0 }), function (d) { return d.group + ':' + d.variable; })
      .join("rect")
      .attr("x", function (d) { return x(d.group) })
      .attr("y", function (d) { return y(d.variable) })
      .attr("width", x.bandwidth())
      .attr("height", y.bandwidth())
      .style("fill", function (d) { return colorScale(d.value) })
      .on("mouseover", mouseover)
      .on("mousemove", mousemove)
      .on("mouseleave", mouseleave)

    // Add title to graph
    svg.append("text")
      .attr("x", 100)
      .attr("y", -50)
      .style("font-size", "14px")
      .text("GEI in EU across all avaliable years, interactive heatmap");


    // similar idea as for plotly, wait 5 frames before measuring end.
    window.requestAnimationFrame(function () {
      window.requestAnimationFrame(function () {
        window.requestAnimationFrame(function () {
          window.requestAnimationFrame(function () {
            window.requestAnimationFrame(function () {
              localStorage.setItem("filterEndTime", localStorage.getItem("filterEndTime") + ', ' + Date.now())
              if (i < 5) {
                onLoad(filters[i]);
              }
              else {
                window.close();
              }
            });
          });
        });
      });
    });
  })
  i++;
}