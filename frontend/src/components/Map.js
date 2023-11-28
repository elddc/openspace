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

		map.current.on('load', () => {
			// Add a data source containing GeoJSON data.
			map.current.addSource('cif', {
			  'type': 'geojson',
			  'data': {
				'type': 'Feature',
				'geometry': {
				  'type': 'Polygon',
				  // These coordinates outline Maine.
				  'coordinates': [
					[
					  [-88.22879, 40.11262],
					  [-88.22779, 40.11262],
					  [-88.22779, 40.11231],
					  [-88.22879, 40.11231],
					  [-88.22879, 40.11262],
					]
				  ]
				}
			  }
			});
		  
			// Add a new layer to visualize the polygon.
			map.current.addLayer({
			  'id': 'cif',
			  'type': 'fill',
			  'source': 'cif', // reference the data source
			  'layout': {},
			  'paint': {
				'fill-color': '#ff3a17', // blue color fill
				'fill-opacity': 0.25
			  }
			});
			// Add a black outline around the polygon.
			map.current.addLayer({
			  'id': 'outline',
			  'type': 'line',
			  'source': 'cif',
			  'layout': {},
			  'paint': {
				'line-color': '#000',
				'line-width': 2
			  }
			});
		  });

	  });

 	return <div>
		<div className="map center" style={{width: 800}}>Map</div>
		<div ref={mapContainer} className="map-container" />
	</div>
  
};

export default Map;
