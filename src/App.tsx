import React from 'react';
import {Provider} from 'react-redux';
import { combineReducers, configureStore } from '@reduxjs/toolkit';
import './App.css';
import { reducer as gameReducer } from './Game/slice'
import { reducer as cardsReducer } from './Cards/slice';
import { UserPile } from './UserPile';
import { DraftPiles } from './DraftPiles';

const store = configureStore({
  reducer: combineReducers({game: gameReducer, cards: cardsReducer}),
});

function App() {
  return (
    <Provider store={store}>
      <div style={{display: 'flex', justifyContent: 'space-between'}}>
      <DraftPiles />
      <UserPile />
      </div>
    </Provider>
  );
}

export default App;
