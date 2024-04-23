// ==UserScript==
// @name        New script plotly-server.local
// @namespace   Violentmonkey Scripts
// @match       http://plotly-server.local/*
// @grant       none
// @version     1.0
// @author      -
// @description 4/23/2024, 7:27:07 PM
// ==/UserScript==
window.addEventListener("load", (event) => {
    onLoad(['BE']);
    onLoad(['DE']);
    onLoad(['BE', 'DK']);
    onLoad(['ES', 'CZ', 'EL','ES','FR','HR','IT','CY','LV','LT','LU','EE']);
    onLoad(['FI', 'SE', 'DK']);
    window.close();
  });