import React from 'react';
import style from '../result_card/ResultCard.module.css';

const ResultCard = ({ result }) => {
  return (
    <div className={style['results-container']}>
      <div className={style['card__result']}>
        <h3>Рубрика: {result.Рубрика}</h3>
        <p>Тема: {result.Тема}</p>
        <p>Текст: {result.Текст}</p>
      </div>
    </div>
  );
};

export default ResultCard;
