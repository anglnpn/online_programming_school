import React from 'react';
import styles from './CourseCard.module.css';
import api from '../../api';
import img from './../../img/course/course.jpg';

const CourseCard = ({ course }) => {

    const handlePayment = async () => {
        try {
              // Выполняем запрос к API для совершения оплаты
              const response = await api.post('payments/create/', {
                payment_course: course.id,
                payment_method:'transfer'
              })
              const responseData = response.data;

                // Преобразовываем строку с данными в объект
              const paymentSessionString = responseData.payment_session_id;
              const regex = /'payment_url':\s*'([^']+)'/;
              const match = paymentSessionString.match(regex);
              const paymentUrl = match && match[1];
              // Перенаправление пользователя на страницу оплаты Stripe
              window.location.href = paymentUrl;



        } catch (error) {
            console.error('Ошибка:', error);
        }
    };

    return (
    <div className={styles.card}>
        <div className={styles.card__container}>
            <div className={styles.card__body}>
            <img className={styles.card__img} src={img} alt="img" />
                <div className={styles.card__title}>{course.name_course}</div>
                <div className={styles.card__desc}>{course.description}</div>
                <div className={styles.card__count}>Количество образовательных модулей: {course.modules_count}</div>
                <div className={styles.card__price}>Цена курса: {course.price} руб.</div>
                <button onClick={handlePayment} className={styles.card__button}>КУПИТЬ</button>
            </div>
        </div>
    </div>
    );
};

export default CourseCard;
