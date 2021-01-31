import React from 'react';

export const Card = ({cardId}: Props) => {
    return <div>{cardId}</div>;
}

interface Props {
    cardId: string;
}