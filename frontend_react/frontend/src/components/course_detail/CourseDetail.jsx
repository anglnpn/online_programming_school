import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './course_detail.css';
import api from '../../api';
import PersonalHeader from '../personal_header/PersonalHeader';
import ModCard from '../mod_card/ModCard';

const CourseDetail = () => {
    const { courseId } = useParams(); // Получаем id курса из параметров маршрута
    const [course, setCourse] = useState(null);
    const [modules, setModules] = useState([]);

    useEffect(() => {
        const fetchCourse = async () => {
            try {
                const response = await api.get(`materials/course/${courseId}/`);
                setCourse(response.data); // Устанавливаем данные курса
                setModules(response.data.modules); // Устанавливаем данные модулей курса
            } catch (error) {
                console.error('Ошибка при загрузке курса:', error);
            }
        };

        fetchCourse();
    }, [courseId]);

    if (!course) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <PersonalHeader />
            <div className="title">{course.name_course}</div>
            <div className="course-list">
                {modules.map(module => (
                    <ModCard key={module.id} module={module} />
                ))}
            </div>
        </div>
    );
};

export default CourseDetail;
