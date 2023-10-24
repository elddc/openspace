import {useState, useEffect} from "react";
import "./button.css";
import axios from "axios";

const Button = ({text}) => {
    const [busyness, setBusyness] = useState(false);
    const [inProgress, setInProgress] = useState(true)

    // initial get request
    useEffect(() => {
        setInProgress(true);
        axios.get("http://127.0.0.1:5000/building", {
            params: { "name": "CIF" }
        }).then(res => {
            console.log(res)
            setBusyness(res.data);
            setInProgress(false);
        }).catch(err => console.log(err));
    }, []);

    // update db every time busyness changes
    useEffect(() => {
        if (busyness) {
            axios.post("http://127.0.0.1:5000/update", {
                name: "CIF",
                busyness
            }).then(res => {
                console.log(res);
            }).catch(err => console.log(err));
        }
        else {
            console.log("GET request in progress, please wait for the page to finish loading");
        }
    }, [busyness]);

    // increment busyness
    const updateBusyness = () => {
        setBusyness(busyness % 5 + 1);
    }

    return <div className="button" onClick={updateBusyness}>{text}: {busyness}</div>
}

export default Button;
