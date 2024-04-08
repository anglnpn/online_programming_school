import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PersonalDashboard = () => {
    const [courses, setCourses] = useState([]);

    const token = localStorage.getItem('token');

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/materials/list/',
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                });
                setCourses(response.data);
            } catch (error) {
                console.error('Ошибка при загрузке списка курсов:', error);
            }
        };

        fetchCourses();
    }, []);

    return (
        <div>
            <h2>Личный кабинет</h2>
            <h3>Список курсов:</h3>
            <ul>
                {courses.map(course => (
                    <li key={course.course_name}>{course.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default PersonalDashboard;
