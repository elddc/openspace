import "./slider.css";

const Slider = ({value, setValue}) => {
    return <div>
        <input className="slider" type="range" id="busyness" name="volume" min="0" max="5"
               value={Math.max(0, value)} onChange={(ev) => {setValue(ev.target.value)}}
               disabled={value < 0}
        />
    </div>

}

export default Slider;
