import {useState, useEffect} from "react";
import "./button.css";

const Button = ({callback, children}) => {
    return <div className="button" onClick={callback}>{children}</div>
}

export default Button;
