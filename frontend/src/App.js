import './App.css';

import Button from "./components/Button";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <p>CIF</p>
                <div className="row">
                    <Button text={"Update building busyness"}/>
                    <Button text={"Update building busyness"}/>
                </div>
            </header>
        </div>
    );
}

export default App;
