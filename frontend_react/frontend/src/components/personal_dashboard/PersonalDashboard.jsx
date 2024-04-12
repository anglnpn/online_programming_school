import React, { useState, useEffect } from 'react';

import './personal.css'
import api from '../../api';

import PersonalHeader from '../personal_header/PersonalHeader'

import CourseCard from '../course_card/CourseCard'

const PersonalDashboard = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await api.get('materials/list/');
                setCourses(response.data.results);
            } catch (error) {
                console.error('Ошибка при загрузке списка курсов:', error);
            }
        };

        fetchCourses();
    }, []);

    return (
        <div>
        <PersonalHeader />
        <div className="title">КУРСЫ ДОСТУПНЫЕ ДЛЯ ПОКУПКИ</div>
          <div className="course-list">
            {courses.map(course => (
              <CourseCard key={course.id} course={course} />
            ))}
            </div>
        </div>
    );
};

export default PersonalDashboard;
