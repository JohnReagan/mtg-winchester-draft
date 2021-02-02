import React from 'react';
import { useSelector } from 'react-redux';
import { Pile } from './Pile';

export const UserPile = () => {
    // @ts-ignore
    const userCardIds = useSelector(state => state.game.cardPool)
    
    return <Pile cardIds={userCardIds} />; 
}