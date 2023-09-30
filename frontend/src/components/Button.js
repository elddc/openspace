import {useState, useEffect} from "react";
import "./button.css";

const Button = ({text}) => {
    const [count, setCount] = useState(0);

    useEffect(() => {
        // alert("do API calls here");
        setCount(12);
    }, []);

    return <div className="button" onClick={() => setCount(count + 1)}>{text}: {count}</div>
}

export default Button;
