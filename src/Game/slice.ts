import {createSlice} from '@reduxjs/toolkit';

enum GameState {
    NotStarted,
    InProgress,
    Complete
}

interface State {
    cardPool: string[];
    draftPiles: {
        [id: number]: string[]
    },
    opponentCardPool: string[];
    isMyTurn: boolean;
    gameState: GameState;
}

const initialState: State = {
    cardPool: [],
    isMyTurn: false,
    opponentCardPool: [],
    gameState: GameState.NotStarted,
    draftPiles: {}
};

const slice = createSlice({
    name: 'game',
    initialState,
    reducers: {
        
    }
})