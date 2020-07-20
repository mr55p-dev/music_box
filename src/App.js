import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";
import CardArea from "./components/cardArea.js";
import Nav from "./components/navigation.js";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch("/time")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTime(data.currentTime);
      });
  }, []);


  return (
    <div className="App">
      <Nav />
      <CardArea />
    </div>
  );
}

export default App;
