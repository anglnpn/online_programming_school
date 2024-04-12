import React, { useState } from 'react';
import logo from './../../img/icons/logo.jpg';
import { Link, useNavigate } from 'react-router-dom';
import './personheader.css';

function PersonalHeader () {
    const history = useNavigate();
    const [showConfirmLogoutModal, setShowConfirmLogoutModal] = useState(false);

    const handleLogout = () => {
        setShowConfirmLogoutModal(true);
    };

    const handleLogoutConfirm = () => {
        localStorage.clear();
        sessionStorage.clear();
        history("/");
    };

    const handleLogoutCancel = () => {
        setShowConfirmLogoutModal(false);
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
                            <li><Link to="/search">Поисковик</Link></li>
                            <li><Link to="/user_courses">Мои курсы</Link></li>
                            <li><Link to="/user/profile/">Мой профиль</Link></li> {/* Измененная ссылка на профиль */}
                            <li><Link to="/">На главную</Link></li>
                            <li><button className="header__nav-btn" onClick={handleLogout}>ВЫЙТИ</button></li>
                        </ul>
                    </nav>
                </div>
            </div>
            {showConfirmLogoutModal && (
                <div className="confirm-logout-modal">
                    <div className="modal-content">
                        <p>Вы уверены, что хотите выйти?</p>
                        <div className="modal-buttons">
                            <button onClick={handleLogoutConfirm} className="logout-confirm">Да</button>
                            <button onClick={handleLogoutCancel} className="logout-cancel">Нет</button>
                        </div>
                    </div>
                </div>
            )}
        </header>
    );
}

export default PersonalHeader;
