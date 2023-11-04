import {useState, useEffect} from "react";
import Slider from "./Slider";
import Button from "./Button";
import axios from "axios";
import "./form.css";

const Form = ({text}) => {
    const [busyness, setBusyness] = useState(-1);
    const [inProgress, setInProgress] = useState(true);
    const [building, setBuilding] = useState("CIF");

    // initial get request
    useEffect(() => {
        setInProgress(true);
        axios.get("http://127.0.0.1:5000/building", {
            params: { "name": building }
        }).then(res => {
            console.log(res)
            setBusyness(res.data);
            setInProgress(false);
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
        <Slider value={busyness} setValue={setBusyness}/>
        <br />
        <div className="card">
            <Button callback={() => setBusyness(Math.max(busyness - 1, 0))}>Decrease busyness</Button>
            <Button callback={() => setBusyness(Math.min(busyness + 1, 5))}>Increase busyness</Button>
        </div>
    </div>
}

export default Form;
