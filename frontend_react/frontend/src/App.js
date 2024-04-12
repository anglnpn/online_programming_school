import React, { Component } from 'react';

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import axios from 'axios';

import './App.css';

import Home from './components/one/One';

import LoginForm from './components/login/LoginForm.jsx';

import PersonalDashboard from './components/personal_dashboard/PersonalDashboard.jsx';

import UserCourses from './components/user_courses/UserCourses'

import CourseDetail from './components/course_detail/CourseDetail.jsx';

import Lesson from './components/lesson/Lesson.jsx';

import UserProfile from './components/user_profile/UserProfile.jsx';


function App() {
    return (

      <div className="App">
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/personal" element={<PersonalDashboard />} />
            <Route path="/user_courses" element={<UserCourses />} />
            <Route path="/course/:courseId" element={<CourseDetail />} />
            <Route path="/materials/lesson/:lessonId" element={<Lesson />} />
            <Route path="/user/profile/" element={<UserProfile />} />
        </Routes>
      </div>

    );
}


export default App;