import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import styles from './Lesson.module.css';
import api from '../../api';
import { useNavigate } from 'react-router-dom';
import PersonalHeader from '../personal_header/PersonalHeader'

const Lesson = () => {
    const { lessonId } = useParams();
    const [lesson, setLesson] = useState();
    const history = useNavigate();
     useEffect(() => {
        const fetchLesson = async () => { // Заменяем fetchCourse на fetchLesson
            try {
                const response = await api.get(`/materials/lesson/${lessonId}/`);
                setLesson(response.data); // Устанавливаем данные курса

            } catch (error) {
                console.error('Ошибка при загрузке курса:', error);
            }
        };

        fetchLesson();
    }, [lessonId]);

    const handleGoBack = () => {
        history(-1); // Переход назад по истории
    };

    if (!lesson) {
        return <div>Loading...</div>;
    }
    return (
        <div>
            <PersonalHeader />
               <button onClick={handleGoBack} className={styles.card__button} >Назад к курсу</button> {/* Кнопка назад */}

                <div className={styles.card}>
                    <div className={styles.card__container}>
                        <div className={styles.card__body}>
                            <img className={styles.card__img} src={lesson.image} alt="Изображение урока" />
                            <div className={styles.video__player}>
                                <iframe width="560" height="315" src={lesson.link} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                            </div>
                            <div className={styles.card__title}>{lesson.name_lesson}</div>

                            <div className={styles.card__content}>{lesson.content}</div>
                        </div>
                    </div>
                </div>

        </div>
    );
};

export default Lesson;
