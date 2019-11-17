import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {


  componentDidMount() {

    fetch('http://localhost:3000/', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    })
      .then(result=>result)
      .then(item=>console.log(item))
      .catch(e=>{
        console.log(e);
        return e;
      })
}

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Output
        </p>
        
      
      </header>
    </div>
  );
}

export default App;
