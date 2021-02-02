import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getCardAsync } from './api';
import { addCard } from './Cards/slice';


export const Card = ({cardId}: Props) => {
    // @ts-ignore
    const card = useSelector(state => state.cards[cardId]);
    const dispatch = useDispatch();
    React.useEffect(() => {
        const getCard = async () => {
            const card = await getCardAsync(cardId);
            dispatch(addCard(card));
        }
        getCard();
    }, [dispatch])
    return <div>{card ? <img style={{height: '200px'}} src={`https://api.scryfall.com/cards/${card.scryfallId}?format=image`} /> : cardId}</div>;
}

interface Props {
    cardId: string;
}