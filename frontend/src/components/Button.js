import {useState, useEffect} from "react";
import "./button.css";

const Button = ({callback, children}) => {
    return <button onClick={callback}>{children}</button>
}

export default Button;
