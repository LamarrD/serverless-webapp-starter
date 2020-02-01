import React from "react";
import logo from "./logo.svg";
import "./App.css";

function doThing() {
  fetch("https://d5mxv1cxfb.execute-api.us-east-1.amazonaws.com/dev/hello")
    .then(response => response.json())
    .then(data => alert(data.message));
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code> src / App.js </code> and save to reload.{" "}
        </p>{" "}
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React{" "}
        </a>{" "}
        <button onClick={doThing}> Do Thing</button>{" "}
      </header>{" "}
    </div>
  );
}

export default App;