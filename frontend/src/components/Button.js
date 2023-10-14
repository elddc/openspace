import {useState, useEffect} from "react";
import "./button.css";
import axios from "axios";

const Button = ({text}) => {
    const [count, setCount] = useState(0);

    useEffect(() => {
        // setCount(12);
        axios.get("http://127.0.0.1:5000/bar").then(res => console.log(res))
    }, []);

    const foo = () => {
        axios.post("http://127.0.0.1:5000/foo", {"a": "b"})
            .then(res => console.log(res))
            .catch(err => console.log(err));
    }

    return <div className="button" onClick={foo}>{text}: {count}</div>
}

export default Button;
