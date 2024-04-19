import React, { useState } from 'react';
import axios from 'axios';

import '../registration/register.css';

const RegistrationForm = ({ onRegistration }) => {
    const [username, setUsername] = useState('');
    const [surname, setSurname] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [passwordsMatch, setPasswordsMatch] = useState(true); // Состояние для проверки совпадения паролей

    const handleClick = () => {
        window.location.href = '/';
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        // Проверяем совпадение паролей
        if (password !== confirmPassword) {
            setPasswordsMatch(false);
            return;
        }

        axios.post('http://127.0.0.1:8000/user/create/', {
            email: email,
            password: password,
            name: username,
            surname: surname,
        })
        .then(response => {
            // Проверяем, что сервер вернул код 201 (Created)
            if (response.status === 201) {
                // Вызываем функцию обратного вызова для уведомления родительского компонента о завершении регистрации
                onRegistration();
                console.log('Регистрация прошла успешно');
            } else {
                console.error('Ошибка при регистрации:', response.data);
            }
        })
        .catch(error => {
            console.error('Ошибка при регистрации:', error);
        });
    };

    return (
        <form onSubmit={handleSubmit} className="registration-form">
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Имя пользователя" className="registration-form-input" />
            <input type="text" value={surname} onChange={(e) => setSurname(e.target.value)} placeholder="Фамилия" className="registration-form-input" />
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Электронная почта" className="registration-form-input" />
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Пароль" className="registration-form-input" />
            <input type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} placeholder="Подтвердите пароль" className="registration-form-input" />
            {!passwordsMatch && <p className="error-message">Пароли не совпадают</p>} {/* Отображаем сообщение об ошибке */}
            <button type="submit" className="registration-form-button">Зарегистрироваться</button>
            <button onClick={handleClick} className="close-btn">x</button>
        </form>
    );
};

export default RegistrationForm;
