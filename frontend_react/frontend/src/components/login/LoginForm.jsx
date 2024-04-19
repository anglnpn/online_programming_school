import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../login/login.css';

import RegistrationForm from '../registration/RegistrationForm';
import '../registration/register.css';

const apiUrl = process.env.REACT_APP_API_URL;

const LoginForm = ({ onLogin }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const history = useNavigate();
    const [showRegistrationForm, setShowRegistrationForm] = useState(false);
    const [error, setError] = useState('');

    const handleRegisterClick = () => {
        setShowRegistrationForm(true);
    };

    const handleRegisterSuccess = () => {
        setShowRegistrationForm(false);
    };

    const handleClick = () => {
        window.location.href = '/';
    };

    const handleLoginButtonClick = () => {
        axios.post(`${apiUrl}/token/`, {
            email: email,
            password: password
        })
        .then(response => {
            const token = response.data.access;
            localStorage.setItem('token', token);
            onLogin(token);
            setError('');
            // Выполняем редирект на страницу личного кабинета
            history('/');
        })
        .catch(error => {
            console.error('Ошибка входа:', error);
            setError('Неправильный логин или пароль');
        });
    };

    return (
        <div>
            <div className="login-modal-content">
                <h2 className="login-form-title">Вход</h2>
                <form>
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
                    <button type="button" onClick={handleLoginButtonClick} className="login-form-button">Войти</button>
                    {error && <p className="error-message">{error}</p>}
                </form>
                <button onClick={handleRegisterClick} className="register-button">Зарегистрироваться</button>
                <button onClick={handleClick} className="close-btn">x</button>
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
