import logo from './logo.svg';
import './App.css';

import Button from "./components/Button";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div className="row">
            <Button text={"Bananas"} />
            <Button text={"Apples"} />
        </div>
      </header>
    </div>
  );
}

export default App;
