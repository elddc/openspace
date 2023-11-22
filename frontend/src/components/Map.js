import Select from "react-select";
import "./map.css";

const Map = ({buildings, currentBuilding, setCurrentBuilding}) => {
	console.log(currentBuilding)

	return <div className="map center">
		{buildings &&
			<div className="dropdown">
				<Select
					value={{value: currentBuilding, label: currentBuilding}}
					onChange={({value}) => setCurrentBuilding(value)}
					options={buildings.map(({name}) => ({value: name, label: name}))}
					autoFocus
					isSearchable
				/>
			</div>
		}
		Todo :D
	</div>;
};

export default Map;
