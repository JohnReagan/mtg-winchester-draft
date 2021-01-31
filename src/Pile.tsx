import React from 'react';
import { Card } from './Card';

export const Pile = ({cardIds}: Props) => {
    return <div>
        {cardIds.map(cardId => <Card cardId={cardId}/>)}
    </div>;
}

interface Props {
    cardIds: string[];
}