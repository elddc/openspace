import {useState, useEffect, useRef} from "react";
import Select from 'react-select';
import Slider from "./Slider";
import Button from "./Button";
import axios from "axios";
import debounce from "debounce";
import { CircularProgressbarWithChildren } from 'react-circular-progressbar';
import "react-circular-progressbar/dist/styles.css";
import "./form.css";

const Form = ({currentBuilding, progress, busyness, setBusyness}) => {
    const debounceUpdate = useRef();

    useEffect(() => {
        debounceUpdate.current = debounce(updateBusyness, 10);
    }, [setBusyness]);

    // debounced update function to prevent overwrites
    const updateBusyness = (val) => {
        setBusyness(val);
    }

    return <div className="form">
        <div className="box">
            <div className="center mb-row">
                <h1>{currentBuilding || "Loading..."}</h1>
                <div className="progress-container">
                    {progress < 0 ||
                        <CircularProgressbarWithChildren
                            value={progress * 20}
                            strokeWidth={12}
                        >
                            <div className="progress-percent">{progress * 20}%</div>
                            FULL
                        </CircularProgressbarWithChildren>
                    }
                </div>
            </div>
            <div>
                <div className="info">
                    <i>This is the average of the responses recorded in the last hour</i>
                </div>
            </div>
        </div>
        <br />
        <div className="box">
            <label htmlFor="busyness-slider">How full would you consider the building to be?</label>
            <Slider id="busyness-slider" value={busyness} setValue={debounceUpdate.current}/>
            <div className="slider-label-container">
                <div>empty</div>
                <div>packed</div>
            </div>
        </div>
    </div>
}

export default Form;
