import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import Select from "react-select";
import "./map.css";
import React, {useRef, useEffect, useState} from 'react';

//var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js')

mapboxgl.accessToken = 'pk.eyJ1Ijoib3BlbnNwYWNldWl1YyIsImEiOiJjbHBoY2lxbXUwNWxwMmtxcWtwbm00ZHd3In0.53dUgjuNw_jH0aN0lkjlCQ';

const Map = ({buildings, currentBuilding, setCurrentBuilding}) => {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng, setLng] = useState(-88.22829);
    const [lat, setLat] = useState(40.11247);
    const [zoom, setZoom] = useState(18);

	useEffect(() => {
        console.log(currentBuilding)
		if (currentBuilding === "CIF") {
			setLng(-88.22829);
			setLat(40.11247);
		}
	}, [currentBuilding]);

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
                                [-88.22875, 40.11262],
                                [-88.22779, 40.11262],
                                [-88.22779, 40.11239],
								[-88.22783, 40.11239],
								[-88.22783, 40.11231],
                                [-88.22879, 40.11231],
								[-88.22879, 40.11238],
								[-88.22875, 40.11238],
                                [-88.22875, 40.11262],
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

			// When a click event occurs on a feature in the states layer,
			// open a popup at the location of the click, with description
			// HTML from the click event's properties.
			map.current.on('click', 'cif', (e) => {
				// new mapboxgl.Popup()
				// .setLngLat(e.lngLat)
				// .setHTML(e.features[0].properties.name)
				// .addTo(map);
				setCurrentBuilding("Campus Instructional Facility (CIF)");
				map.current.flyTo({
					center: [-88.22829,40.11247],
					zoom: zoom
				});
				
			});
				
			// Change the cursor to a pointer when
			// the mouse is over the states layer.
			map.current.on('mouseenter', 'cif', () => {
				map.current.getCanvas().style.cursor = 'pointer';
			});
				
			// Change the cursor back to a pointer
			// when it leaves the states layer.
			map.current.on('mouseleave', 'cif', () => {
				map.current.getCanvas().style.cursor = '';
			});
        });

    }, []);

    return <div className="map center">
        {buildings &&
            <div className="dropdown">
                <Select
                    value={{value: currentBuilding, label: currentBuilding}}
                    onChange={({value}) => setCurrentBuilding(value)}
                    options={buildings.map(({name}) => ({value: name, label: name}))}
                    autoFocus
                    isSearchable
                />
            </div>
        }
        <div ref={mapContainer} className="map-container" />
    </div>

};

export default Map;
