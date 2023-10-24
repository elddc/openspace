import {useState, useEffect} from "react";
import "./button.css";
import axios from "axios";

const Button = ({text}) => {
    const [busyness, setBusyness] = useState(1);
    const [inProgress, setInProgress] = useState(true)

    // initial get request
    useEffect(() => {
        setInProgress(true);
        axios.get("http://127.0.0.1:5000/building", {
            params: { "name": "CIF" }
        }).then(res => {
            setBusyness(res.data);
            setInProgress(false);
        })
    }, []);

    // update db every time busyness changes
    useEffect(() => {
        if (!inProgress) {
            axios.patch("http://127.0.0.1:5000/patch", {
                name: "CIF",
                busyness
            }).then(res => {
                console.log(res);
            }).catch(err => console.log(err));
        }
    }, [busyness, inProgress]);

    // increment busyness
    const updateBusyness = () => {
        setBusyness(busyness % 5 + 1);
    }

    return <div className="button" onClick={updateBusyness}>{text}: {busyness}</div>
}

export default Button;
