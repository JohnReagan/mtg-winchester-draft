import {createSlice, PayloadAction} from '@reduxjs/toolkit';

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

interface SetDraftPilePayload {
    cardIds: string[],
    pileId: number
}

const slice = createSlice({
    name: 'game',
    initialState,
    reducers: {
        setDraftPile: (state, action: PayloadAction<SetDraftPilePayload[]>) => {
            const piles = action.payload;
            piles.forEach(({pileId, cardIds}) => {
                state.draftPiles[pileId] = cardIds;
            });
        },
        setIsMyTurn: (state, action: PayloadAction<boolean>) => {
            state.isMyTurn = action.payload;
        },
        setCardPool: (state, action: PayloadAction<string[]>) => {
            state.cardPool = action.payload;
        },
        addToCardPool: (state, action: PayloadAction<string[]>) => {
            state.cardPool.push(...action.payload);
        },
        setOpponentCardPool: (state, action: PayloadAction<string[]>) => {
            state.opponentCardPool = action.payload;
        }, 
        setGameState: (state, action: PayloadAction<GameState>) => {
            state.gameState = action.payload;
        }
    }
});

export const {setDraftPile, addToCardPool} = slice.actions;
export const {reducer} = slice; 