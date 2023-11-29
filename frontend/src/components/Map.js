import React, {useRef, useEffect, useState} from 'react';
import Select from "react-select";
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import "./map.css";
import 'mapbox-gl/dist/mapbox-gl.css';

//var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js')

mapboxgl.accessToken = 'pk.eyJ1Ijoib3BlbnNwYWNldWl1YyIsImEiOiJjbHBoY2lxbXUwNWxwMmtxcWtwbm00ZHd3In0.53dUgjuNw_jH0aN0lkjlCQ';

const Map = ({buildings, currentBuilding, setCurrentBuilding}) => {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng, setLng] = useState(-88.22829);
    const [lat, setLat] = useState(40.11247);
    const [zoom, setZoom] = useState(18);

    useEffect(() => {
        if (currentBuilding && map.current) {
            const location = buildings[currentBuilding].location;
            if (location) {
                map.current.flyTo({
                    center: JSON.parse(location)[0],
                    zoom: zoom
                });
            }
        }
    }, [currentBuilding]);

    useEffect(() => {
        console.log("update buildings");

        if (buildings && map.current) {
            for (const {name, location, busyness} of Object.values(buildings)) {
                if (location) {
                    map.current.getSource(name).setData({
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Polygon',
                            'coordinates': [JSON.parse(location)[1]]
                        },
                        'properties': {
                            'busyness': parseInt(busyness)
                        }
                    });
                }
            }
        }

        else if (buildings && !map.current) {
            map.current = new mapboxgl.Map({
                container: mapContainer.current,
                style: 'mapbox://styles/mapbox/streets-v12',
                center: [lng, lat],
                zoom: zoom
            });

            for (const {name, location, busyness} of Object.values(buildings)) {
                if (location) {
                    map.current.on('load', () => {
                        // Add a data source containing GeoJSON data
                        map.current.addSource(name, {
                            'type': 'geojson',
                            'data': {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Polygon',
                                    'coordinates': [JSON.parse(location)[1]],
                                },
                                'properties': {
                                    'busyness': busyness
                                }
                            }
                        });

                        // Add a new layer to visualize the polygon
                        map.current.addLayer({
                            'id': name,
                            'type': 'fill',
                            'source': name, // reference the data source
                            'layout': {},
                            'paint': {
                                'fill-color': {
                                    'property': 'busyness',
                                    'stops': [[0, '#0f0'], [2, '#ff0'], [5, '#f00']]
                                },
                                'fill-opacity': 0.25
                            }
                        });

                        // Add a black outline around the polygon
                        map.current.addLayer({
                            'id': name + '_outline',
                            'type': 'line',
                            'source': name,
                            'layout': {},
                            'paint': {
                                'line-color': '#000',
                                'line-width': 2
                            }
                        });

                        // When a click event occurs on a feature in the states layer,
                        // change the current building
                        map.current.on('click', name, (e) => {
                            // new mapboxgl.Popup()
                            // .setLngLat(e.lngLat)
                            // .setHTML(e.features[0].properties.name)
                            // .addTo(map);
                            setCurrentBuilding(name);
                        });

                        // Change the cursor to a pointer when
                        // the mouse is over the states layer
                        map.current.on('mouseenter', name, () => {
                            map.current.getCanvas().style.cursor = 'pointer';
                        });

                        // Change the cursor back to a pointer
                        // when it leaves the states layer
                        map.current.on('mouseleave', name, () => {
                            map.current.getCanvas().style.cursor = '';
                        });

                    });
                }
            }
        }
    }, [buildings]);

    return <div className="map center">
        {buildings &&
            <div className="dropdown">
                <Select
                    value={{value: currentBuilding, label: currentBuilding}}
                    onChange={({value}) => setCurrentBuilding(value)}
                    options={Object.keys(buildings).map(name => ({value: name, label: name}))}
                    autoFocus
                    isSearchable
                />
            </div>
        }
        <div ref={mapContainer} className="map-container" />
    </div>

};

export default Map;
