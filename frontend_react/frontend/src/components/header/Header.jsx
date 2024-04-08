import logo from './../../img/icons/logo.jpg';


// импорт цвета текста
import './header.css';

import React, { useState } from 'react';
import LoginForm from '../login/LoginForm';
import '../login/login.css';

function Header() {
    const [showLoginForm, setShowLoginForm] = useState(false);

    const handleLoginClick = () => {
        setShowLoginForm(true);
    };

    const handleLoginSuccess = () => {
        setShowLoginForm(false);
    };

    return (
        <header className="header">
            <div className="container">
                <div className="header__row">
                    <div className="header__logo">
                        <img src={logo} alt="Logo" />
                        <span>OnlineSchool</span>
                    </div>
                    <nav className="header__nav">
                        <ul>
                            <li><a href="#home">Home</a></li>
                            <li><a href="#about">About</a></li>
                            <li><button onClick={handleLoginClick} className="header__nav-btn">SIGN UP</button></li>
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
        </header>
    );
}

export default Header;
