import React, { useState, useEffect } from 'react';

import './courses.css';
import api from '../../api';

import UserCourseCard from '../users_courses_card/UserCourseCard'
import PersonalHeader from '../personal_header/PersonalHeader'

const UserCourses = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await api.get('materials/list_user/');
                setCourses(response.data);
            } catch (error) {
                console.error('Ошибка при загрузке списка курсов:', error);
            }
        };

        fetchCourses();
    }, []);

    return (
        <div>
        <PersonalHeader />
        <div className="title">ВАШИ КУРСЫ</div>
          <div className="course-list">
            {courses.map(course => (
              <UserCourseCard key={course.id} course={course} />
            ))}
            </div>
        </div>
    );
};

export default UserCourses;