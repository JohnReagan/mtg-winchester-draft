import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDraftPilesAsync } from "./api";
import { setDraftPile, addToCardPool } from "./Game/slice";
import { Pile } from "./Pile";

export const DraftPiles = () => {
    const dispatch = useDispatch();
    React.useEffect(() => {
      // todo start on game start and via thunk
      const updateState = async () => {
        const piles = await getDraftPilesAsync(1);
        dispatch(setDraftPile(piles));
      }
  
      updateState();
    }, [dispatch]);
    const onPileClick = React.useMemo(() => (cardIds: string[]) => dispatch(addToCardPool(cardIds)), [dispatch]);
    // @ts-ignore
    const piles: {[pileId: number]: string[]} = useSelector(state => state.game.draftPiles)
    return <div style={{display: 'flex'}}>{Object.values(piles).map(cardIds => <Pile cardIds={cardIds} onClick={onPileClick} />)}</div>
  }