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
    const [progress, setProgress] = useState(4);
    const [building, setBuilding] = useState("CIF");

    // initial get request
    useEffect(() => {
        axios.get("http://127.0.0.1:5000/building", {
            params: { "name": building }
        }).then(res => {
            console.log(res)
            setBusyness(res.data);
            setProgress(res.data);
        }).catch(err => console.log(err));
    }, []);

    // update db every time busyness changes
    useEffect(() => {
        console.log(busyness)
        if (busyness >= 0) {
            axios.post("http://127.0.0.1:5000/building", {
                name: building,
                busyness
            }).then(res => {
                console.log(res);
                
                setProgress(res.data);
            }).catch(err => console.log(err));
        }
        else {
            console.log("GET request in progress, please wait for the page to finish loading");
        }
    }, [busyness]);

    return <div className="form center">
        <h1>{building}</h1>
        <h3>{busyness < 0 ? '-' : (busyness * 20)}% full</h3>
        <div className="box progress-container">
            <CircularProgressbarWithChildren
                value={progress * 20}
                // text={progress * 20 + "%"}
                strokeWidth={12}
            >
                <div className="progress-percent">{progress * 20}%</div>
                FULL
            </CircularProgressbarWithChildren>
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
