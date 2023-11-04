import "./slider.css";

const Slider = ({value, setValue}) => {
    return <div>
        <input className="slider" type="range" id="busyness" name="volume" min="0" max="5"
               value={value || 0} onChange={(ev) => {setValue(ev.target.value)}}
               disabled={!value}
        />
    </div>

}

export default Slider;
