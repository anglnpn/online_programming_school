import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import LoginForm from '../login/LoginForm';
import ConfirmLogoutModal from './ConfirmLogoutModal'; // Импортируем компонент подтверждения
import logo from './../../img/icons/logo.jpg';
import '../login/login.css';
import './header.css';

function Header() {
    const [showLoginForm, setShowLoginForm] = useState(false);
    const [showConfirmLogoutModal, setShowConfirmLogoutModal] = useState(false); // Состояние для отображения модального окна
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        // Проверяем, есть ли токен в localStorage
        const token = localStorage.getItem('token');
        setIsLoggedIn(!!token); // Устанавливаем состояние аутентификации в зависимости от наличия токена
    }, []);

    const handleLoginClick = () => {
        setShowLoginForm(true);
    };

    const handleLogoutClick = () => {
        setShowConfirmLogoutModal(true); // Показываем модальное окно при выходе
    };

    const handleConfirmLogout = () => {
        localStorage.removeItem('token'); // Удаляем токен из localStorage
        setIsLoggedIn(false); // Устанавливаем состояние аутентификации как false
        setShowConfirmLogoutModal(false); // Закрываем модальное окно
        navigate('/'); // Редирект на главную страницу
    };

    const handleCancelLogout = () => {
        setShowConfirmLogoutModal(false); // Закрываем модальное окно
    };

    const handleLoginSuccess = () => {
        setShowLoginForm(false);
        setIsLoggedIn(true); // Устанавливаем состояние аутентификации как true
    };

    const handleHomeClick = () => {
        navigate('/personal'); // Редирект в личный кабинет
    };

    return (
        <header className="header">
            <div className="container">
                <div className="header__row">
                    <div className="header__logo">
                        <img src={logo} alt="Logo" />

                    </div>
                    <nav className="header__nav">
                        <ul>
                            <li><a href="/search">Поисковик</a></li>
                            {isLoggedIn && (
                                <li><a href="/personal">Домой</a></li>

                            )}

                            {isLoggedIn ? (
                                <li><button onClick={handleLogoutClick} className="header__nav-btn">Выйти</button></li>
                            ) : (
                                <li><button onClick={handleLoginClick} className="header__nav-btn">Войти</button></li>
                            )}
                        </ul>
                    </nav>
                </div>
            </div>
            {showLoginForm && (
                <div className="login-modal">
                    <div className="login-modal-content">
                        <LoginForm onLogin={handleLoginSuccess} />
                    </div>
                </div>
            )}
            {showConfirmLogoutModal && (
                <ConfirmLogoutModal onConfirm={handleConfirmLogout} onCancel={handleCancelLogout} /> // Показываем модальное окно подтверждения при выходе
            )}
        </header>
    );
}

export default Header;
