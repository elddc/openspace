import axios from "axios";
import {useEffect, useState} from "react";

import Form from "./components/Form";
import Map from "./components/Map";
import './global.css';

function App() {
    const [busyness, setBusyness] = useState(-1);
    const [progress, setProgress] = useState(-1);
    const [buildings, setBuildings] = useState(null);
    const [currentBuilding, setCurrentBuilding] = useState(null);

    // initial get request, gets all building data
    useEffect(() => {
        document.title = "OpenSpace";

        const controller = new AbortController();
        axios.get("http://127.0.0.1:5000/building", {
            signal: controller.signal
        }).then(res => {
            console.log("buildings:", res.data);
            setBuildings(res.data);
            setCurrentBuilding("Campus Instructional Facility (CIF)"); // default
        }).catch(err => console.log(err));
        return () => {controller.abort()};
    }, []);

    // get busyness for a single building
    useEffect(() => {
        const controller = new AbortController();
        if (currentBuilding) {
            axios.get("http://127.0.0.1:5000/building", {
                params: { "name": currentBuilding },
                signal: controller.signal
            }).then(res => {
                // console.log("busyness: " + res.data);
                setBusyness(res.data);
                setProgress(res.data);
            }).catch(err => console.log(err));
        }
        else {
            console.log("GET request in progress, please wait for the page to finish loading");
        }
        return () => {controller.abort()};
    }, [currentBuilding]);

    // update db every time busyness changes
    useEffect(() => {
        if (busyness >= 0) {
            axios.post("http://127.0.0.1:5000/building", {
                name: currentBuilding,
                busyness
            }).then(res => {
                console.log("progress: " + res.data);
                setProgress(res.data)
                console.log(busyness);
                setBuildings({
                    ...buildings,
                    [currentBuilding]: {...buildings[currentBuilding], busyness}
                })
            }).catch(err => {
                console.log(err);
                console.log("cancelled " + busyness);
            });
        }
        else {
            console.log("GET request in progress, please wait for the page to finish loading");
        }
    }, [busyness]);

    return (
        <main className="mb-col">
            <Form
                currentBuilding={currentBuilding}
                progress={progress}
                busyness={busyness}
                setBusyness={setBusyness}
            />
            <Map
                buildings={buildings}
                currentBuilding={currentBuilding}
                setCurrentBuilding={setCurrentBuilding}
            />
        </main>
    );
}

export default App;
