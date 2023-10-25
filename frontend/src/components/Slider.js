const Slider = ({value, setValue}) => {
    return <div>
        <input type="range" id="busyness" name="volume" min="0" max="5"
               value={value} onChange={(ev) => {setValue(ev.target.value)}}
        />
    </div>
    
}

export default Slider;
