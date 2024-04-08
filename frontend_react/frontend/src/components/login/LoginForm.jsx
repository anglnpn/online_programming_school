import React, { useState } from 'react';
import axios from 'axios';
import '../login/login.css';

import RegistrationForm from '../registration/RegistrationForm';
import '../registration/register.css';

import PersonalDashboard from '../personal_dashboard/PersonalDashboard';


const LoginForm = ({ onLogin }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [showRegistrationForm, setShowRegistrationForm] = useState(false);

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post('http://127.0.0.1:8000/token/', {
            email: email,
            password: password
        })
        .then(response => {
            const token = response.data.token["access"];
            localStorage.setItem('token', token);
            onLogin(token);
        })
        .catch(error => {
            console.error('Ошибка входа:', error);
        });
    };

    const handleRegisterClick = () => {
        setShowRegistrationForm(true);
    };

    const handleRegisterSuccess = () => {
        setShowRegistrationForm(false);
    };

    return (
        <div>
            <div className="login-modal-content">
                <span className="close-btn">×</span>
                <h2 className="login-form-title">Вход</h2>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="login-form-input"
                        placeholder="Email"
                    />
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="login-form-input"
                        placeholder="Пароль"
                    />
                    <button type="submit" className="login-form-button">Войти</button>
                </form>
                <button onClick={handleRegisterClick} className="register-button">Зарегистрироваться</button>
                {showRegistrationForm && (
                    <div className="login-modal">
                        <div className="login-modal-content">
                            <RegistrationForm onRegistration={handleRegisterSuccess} />
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default LoginForm;