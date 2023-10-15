import logo from './logo.svg';
import './App.css';

import Button from "./components/Button";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <p>This is a demo for how the frontend and backend can interact!</p>
                <div className="row">
                    <Button text={"Update building busyness"}/>
                </div>
            </header>
        </div>
    );
}

export default App;
