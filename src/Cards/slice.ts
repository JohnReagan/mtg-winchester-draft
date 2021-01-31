import { createSlice, PayloadAction } from '@reduxjs/toolkit';

const SLICE_NAME = 'cards';

export interface Card {
    id: string;
    scryfallId: string;
    text: string;
}

export interface State {
    [id: string]: Card
}

const slice = createSlice({
    name: SLICE_NAME,
    initialState: {} as State,
    reducers: {
        addCard: (state, action: PayloadAction<Card>) => {
            const card = action.payload;
            state[card.id] = card;
        }
    } 
});

export const { addCard } = slice.actions;
export const { reducer } = slice;