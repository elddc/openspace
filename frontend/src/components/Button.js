import {useState, useEffect} from "react";
import "./button.css";
import axios from "axios";

const Button = ({text}) => {
    const [busyness, setBusyness] = useState(1);

    // initial get request
    useEffect(() => {
        axios.get("http://127.0.0.1:5000/bar", {
            params: { "building": 0 }
        }).then(res => console.log(res))
    }, []);

    // update db every time busyness changes
    useEffect(() => {
        axios.post("http://127.0.0.1:5000/foo", {
            "building": 0,
            "busyness": busyness
        }).then(res => {
            console.log(res);
        }).catch(err => console.log(err));
    }, [busyness]);

    // increment busyness
    const updateBusyness = () => {
        setBusyness(busyness % 5 + 1);
    }

    return <div className="button" onClick={updateBusyness}>{text}: {busyness}</div>
}

export default Button;
