import React from 'react';
import styles from './ModCard.module.css';
import { useNavigate } from 'react-router-dom';

const ModCard = ({ module }) => {
    const navigate = useNavigate(); // Инициализируем useNavigate

    const handleLessonDetails = (lessonId) => {
        // Перенаправляем пользователя на страницу с деталями урока
        navigate(`/materials/lesson/${lessonId}`);
    };

    return (
        <div className={styles.card}>
            <div className={styles.card__container}>
                <div className={styles.card__body}>
                    <img className={styles.card__img} src={module.image} alt="Изображение модуля" />
                    <div className={styles.cars__numb}>Модуль №{module.sequence_number}</div>
                    <div className={styles.card__title}>{module.name_module}</div>
                    <div className={styles.card__desc}>{module.description}</div>
                    <div className={styles.card__lessons}>
                        {module.lessons.map(lesson => (
                            <div key={lesson.id} className={styles.card__lesson}>
                                <img className={styles.lesson_image} src={lesson.image} alt="Изображение урока" />
                                <div className={styles.lesson__details}>
                                    <div className={styles.lesson__title}>{lesson.name_lesson}</div>
                                    <div className={styles.lesson__desc}>{lesson.description}</div>
                                    <button onClick={() => handleLessonDetails(lesson.id)} className={styles.lesson__button}>ПРОЙТИ УРОК</button>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ModCard;
