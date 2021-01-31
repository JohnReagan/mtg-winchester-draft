import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Pile } from './Pile';

function App() {
  return (
    <div><Pile cardIds={[1,2,3].map(String)}/></div>
  );
}

export default App;
