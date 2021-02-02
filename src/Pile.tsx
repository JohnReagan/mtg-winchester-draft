import React from 'react';
import { Card } from './Card';

export const Pile = ({cardIds, onClick}: Props) => {
    return <div onClick={() => onClick && onClick(cardIds)}>
        {cardIds.map(cardId => <Card cardId={cardId}/>)}
    </div>;
}

interface Props {
    cardIds: string[];
    onClick?(cardIds: string[]): void;
}