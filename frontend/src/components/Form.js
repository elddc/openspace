import {useState, useEffect, useRef} from "react";
import Slider from "./Slider";
import Button from "./Button";
import axios from "axios";
import debounce from "debounce";
import { CircularProgressbarWithChildren } from 'react-circular-progressbar';
import "react-circular-progressbar/dist/styles.css";
import "./form.css";

const Form = ({text}) => {
    const [busyness, setBusyness] = useState(-1);
    const [progress, setProgress] = useState(-1);
    const [currentBuilding, setCurrentBuilding] = useState(null);
    const [buildings, setBuildings] = useState(null);
    const debounceUpdate = useRef();

    // initial get request
    useEffect(() => {
        const controller = new AbortController();
        axios.get("http://127.0.0.1:5000/building", {
            signal: controller.signal
        }).then(res => {
            console.log("buildings: " + res.data);
            console.log("names: " + res.data.map(({name}) => name));
            setBuildings(res.data);
            setCurrentBuilding("CIF");
            debounceUpdate.current = debounce(updateBusyness, 10);
        }).catch(err => console.log(err));
        return () => {controller.abort()};
    }, []);

    useEffect(() => {
        const controller = new AbortController();
        if (currentBuilding) {
            axios.get("http://127.0.0.1:5000/building", {
                params: { "name": currentBuilding },
                signal: controller.signal
            }).then(res => {
                console.log("busyness: " + res.data);
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
                setProgress(res.data);
            }).catch(err => {
                console.log(err);
                console.log("cancelled " + busyness);
            });
        }
        else {
            console.log("GET request in progress, please wait for the page to finish loading");
        }
    }, [busyness]);

    const updateBusyness = (val) => {
        setBusyness(val);
    }

    return <div className="form center">
        <div className="box center mb-row">
            <h1>{currentBuilding || "Loading..."}</h1>
            <div className="progress-container">
                {progress < 0 ||
                    <CircularProgressbarWithChildren
                        value={progress * 20}
                        // text={progress * 20 + "%"}
                        strokeWidth={12}
                    >
                        <div className="progress-percent">{progress * 20}%</div>
                        FULL
                    </CircularProgressbarWithChildren>
                }
            </div>
        </div>
        <br />
        <div className="box">
            <label htmlFor="busyness-slider">How full would you consider the building to be?</label>
            <Slider id="busyness-slider" value={busyness} setValue={debounceUpdate.current}/>
            <div className="slider-label-container">
                <div>0%</div>
                <div>100%</div>
            </div>
            <button onClick={() => console.log(busyness)}>Busyness</button>
            <button onClick={() => console.log(progress)}>Progress</button>
        </div>
    </div>
}

export default Form;
