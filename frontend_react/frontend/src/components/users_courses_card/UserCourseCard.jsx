import React, { useState, useEffect } from 'react';
import styles from './UserCourseCard.module.css';
import api from '../../api';
import { useNavigate } from 'react-router-dom';

const CourseCard = ({ course }) => {
    const navigate = useNavigate(); // Инициализируем useNavigate
    const [isSubscribed, setIsSubscribed] = useState(false);

    useEffect(() => {
        setIsSubscribed(course.is_subscribed);
    }, [course.is_subscribed]);

    const handleCourseDetails = () => {

        navigate(`/course/${course.id}`);
    };

    const handleSubscribeToggle = () => {

        if (isSubscribed) {
            unsubscribe(course.id);
        } else {
            subscribe(course.id);
        }
    };

    const subscribe = async (courseId) => {
        try {
            const response = await api.post('/payments/subscribe/', { course_id: courseId });
            setIsSubscribed(true);
            console.log(response.data.message);
        } catch (error) {
            console.error('Ошибка при подписке на курс:', error);
        }
    };

    const unsubscribe = async (courseId) => {
        try {
            const response = await api.post('/payments/subscribe/', { course_id: courseId });
            setIsSubscribed(false);
            console.log(response.data.message);
        } catch (error) {
            console.error('Ошибка при отписке от курса:', error);
        }
    };

    return (
        <div className={styles.card}>
            <div className={styles.card__container}>
                <div className={styles.card__body}>
                    <img className={styles.card__img} src={course.image} alt="img" />
                    <div className={styles.card__title}>{course.name_course}</div>
                    <div className={styles.card__desc}>{course.description}</div>
                    <div className={styles.card__count}>Количество модулей: {course.modules_count}</div>

                    <button onClick={handleCourseDetails} className={styles.card__button}>ПРОЙТИ КУРС</button>
                    <button onClick={handleSubscribeToggle} className={styles.card__button}>
                        {isSubscribed ? 'ОТПИСАТЬСЯ' : 'ПОДПИСАТЬСЯ НА ОБНОВЛЕНИЯ'}
                    </button>
                </div>
            </div>
        </div>
    );
};

export default CourseCard;
