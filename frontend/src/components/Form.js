import {useState, useEffect} from "react";
import Slider from "./Slider";
import Button from "./Button";
import axios from "axios";
// import {CircularProgressbar} from "react-circular-progressbar";
import { CircularProgressbarWithChildren } from 'react-circular-progressbar';
import "react-circular-progressbar/dist/styles.css";
import "./form.css";

const Form = ({text}) => {
    const [busyness, setBusyness] = useState(-1);
    const [progress, setProgress] = useState(-1);
    const [currentBuilding, setCurrentBuilding] = useState(null);
    const [buildings, setBuildings] = useState(null);

    // initial get request
    useEffect(() => {
        const controller = new AbortController();
        axios.get("http://127.0.0.1:5000/building", {
            signal: controller.signal
        }).then(res => {
            // console.log("buildings: " + res.data);
            // console.log("names: " + res.data.map(({name}) => name));
            setBuildings(res.data);
            setCurrentBuilding("CIF");
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
        const controller = new AbortController();
        if (busyness >= 0) {
            axios.post("http://127.0.0.1:5000/building", {
                name: currentBuilding,
                busyness
            }, {
                signal: controller.signal
            }).then(res => {
                // console.log("progress: " + res.data);
                setProgress(res.data);
            }).catch(err => console.log(err));
        }
        else {
            console.log("GET request in progress, please wait for the page to finish loading");
        }
        return () => {controller.abort()};
    }, [busyness]);

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
            <Slider id="busyness-slider" value={busyness} setValue={setBusyness}/>
            <div className="slider-label-container">
                <div>0%</div>
                <div>100%</div>
            </div>
        </div>
    </div>
}

export default Form;
