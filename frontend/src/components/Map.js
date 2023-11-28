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

		// CIF
        map.current.on('load', () => {
            // Add a data source containing GeoJSON data.
            map.current.addSource('cif', {
                'type': 'geojson',
                'data': {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Polygon',
                        // These coordinates outline CIF.
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
                'id': 'cif_outline',
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

		//Illini Union
		map.current.on('load', () => {
            // Add a data source containing GeoJSON data.
            map.current.addSource('union', {
                'type': 'geojson',
                'data': {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Polygon',
                        // These coordinates outline the Union.
                        'coordinates': [
                            [
								[-88.2277333, 40.1089115],
								[-88.227736 , 40.1092459],
								[-88.2275268, 40.109248],
								[-88.2275294, 40.1095208],
								[-88.2277413, 40.1095229],
								[-88.2277494, 40.1096582],
								[-88.2278004, 40.1096603],
								[-88.2278004, 40.1097301],
								[-88.2277521, 40.109728],
								[-88.2277548, 40.10986750],
								[-88.2275402, 40.10986961],
								[-88.2275321, 40.10980192],
								[-88.2273173, 40.10980394],
								[-88.2273186, 40.10985775],
								[-88.2271382, 40.10986086],
								[-88.2271361, 40.10980647],
								[-88.2269196, 40.10980868],
								[-88.2269209, 40.10987989],
								[-88.2266972, 40.10988260],
								[-88.2266955, 40.10953391],
								[-88.2269074, 40.10953392],
								[-88.2268999, 40.10898663],
								[-88.2275118, 40.10897855],
								[-88.2275124, 40.10891086],
								[-88.2277333, 40.1089115],

                            ]
                        ]
                    }
                }
            });

            // Add a new layer to visualize the polygon.
            map.current.addLayer({
                'id': 'union',
                'type': 'fill',
                'source': 'union', // reference the data source
                'layout': {},
                'paint': {
                    'fill-color': '#ff3a17', // red color fill
                    'fill-opacity': 0.25
                }
            });
            // Add a black outline around the polygon.
            map.current.addLayer({
                'id': 'union_outline',
                'type': 'line',
                'source': 'union',
                'layout': {},
                'paint': {
                    'line-color': '#000',
                    'line-width': 2
                }
            });

			// When a click event occurs on a feature in the states layer,
			// open a popup at the location of the click, with description
			// HTML from the click event's properties.
			map.current.on('click', 'union', (e) => {
				// new mapboxgl.Popup()
				// .setLngLat(e.lngLat)
				// .setHTML(e.features[0].properties.name)
				// .addTo(map);
				setCurrentBuilding("Illini Union");
				map.current.flyTo({
					center: [-88.22717958465586, 40.10938652028243],
					zoom: zoom
				});
				
			});
				
			// Change the cursor to a pointer when
			// the mouse is over the states layer.
			map.current.on('mouseenter', 'union', () => {
				map.current.getCanvas().style.cursor = 'pointer';
			});
				
			// Change the cursor back to a pointer
			// when it leaves the states layer.
			map.current.on('mouseleave', 'union', () => {
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
