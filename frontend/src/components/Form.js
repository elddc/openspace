import {useState, useEffect} from "react";
import Slider from "./Slider";
import Button from "./Button";
import axios from "axios";
import {CircularProgressbar} from "react-circular-progressbar";
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
            <CircularProgressbar
                value={progress * 20}
                text={progress * 20 + "%"}
                strokeWidth={20}
            />
        </div>
        <br />
        <div className="box">
            <Slider value={busyness} setValue={setBusyness}/>
            <br />
            <Button callback={() => setBusyness(Math.max(busyness - 1, 0))}>Decrease busyness</Button>
            <Button callback={() => setBusyness(Math.min(busyness + 1, 5))}>Increase busyness</Button>
        </div>
    </div>
}

export default Form;
