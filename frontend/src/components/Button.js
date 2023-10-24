import {useState, useEffect} from "react";
import "./button.css";
import axios from "axios";

const Button = ({text, callback}) => {
    return <div className="button" onClick={callback}>{text}</div>
}

export default Button;
