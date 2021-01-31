import { State } from "./slice";


export const getCardById = (state: State, { cardId }: {cardId: number}) => state[cardId];