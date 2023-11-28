import "./map.css";
import React, { useRef, useEffect, useState } from 'react';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax

//var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js')
 
mapboxgl.accessToken = 'pk.eyJ1Ijoib3BlbnNwYWNldWl1YyIsImEiOiJjbHBoY2lxbXUwNWxwMmtxcWtwbm00ZHd3In0.53dUgjuNw_jH0aN0lkjlCQ';

const Map = () => {
	const mapContainer = useRef(null);
	const map = useRef(null);
	const [lng, setLng] = useState(-88.22829);
	const [lat, setLat] = useState(40.11247);
	const [zoom, setZoom] = useState(18);

	useEffect(() => {
		if (map.current) return; // initialize map only once
		map.current = new mapboxgl.Map({
		  container: mapContainer.current,
		  style: 'mapbox://styles/mapbox/streets-v12',
		  center: [lng, lat],
		  zoom: zoom
		});
	  });

 	return <div>
		<div className="map center" style={{width: 800}}>Map</div>
		<div ref={mapContainer} className="map-container" />
	</div>
  
};

export default Map;
