import { Card } from "./Cards/slice";

export const getDraftPilesAsync = async (gameId: number): Promise<{pileId: number, cardIds: string[]}[]> => {
    // todo implement
    await stall();
    return [
        { pileId: 1, cardIds: ['1', '1']},
        { pileId: 2, cardIds: ['1', '1']},
        { pileId: 3, cardIds: ['1', '1']},
        { pileId: 4, cardIds: ['1', '1']}
    ];
};

export const getCardAsync = async (cardId: string): Promise<Card> => {
    // todo implement
    await stall();
    return dummyCard;
}

async function stall(stallTime = 200) {
    await new Promise(resolve => setTimeout(resolve, stallTime));
};

const dummyCard = {
    name: 'Axgard Braggart',
    scryfallId: '4de5ff64-6fe7-4fc5-be27-cdbaa14545ab',
    id: '1',
    text: 'lorem ipsum'
}