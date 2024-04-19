import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../search/search.css';
import logo from './../../img/icons/logo.jpg';
// импорт цвета текста
import '../../components/header/header.css';

import ResultCard from '../result_card/ResultCard';
import Header from '../header/Header';
import Footer from '../info_form/InfoForm.jsx';

import LoginForm from '../login/LoginForm';
import '../login/login.css';
import { Link, useNavigate } from 'react-router-dom';
import '../personal_header/personheader.css';

const apiUrl = process.env.REACT_APP_API_URL;


const SearchForm = () => {
  const [searchResults, setSearchResults] = useState([]);
  const [error, setError] = useState(null);
  const [showLoginForm, setShowLoginForm] = useState(false);
  const [showConfirmLogoutModal, setShowConfirmLogoutModal] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const history = useNavigate();


  useEffect(() => {
        // Проверяем, есть ли токен в localStorage
        const token = localStorage.getItem('token');
        setIsLoggedIn(!!token); // Устанавливаем состояние аутентификации в зависимости от наличия токена
    }, []);

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

  const handleLoginClick = () => {
        setShowLoginForm(true);
    };

    const handleLoginSuccess = () => {
        setShowLoginForm(false);
    };

    const handleLogoutClick = () => {
        setShowConfirmLogoutModal(true); // Показываем модальное окно при выходе
    };

    const handleOpenLoginForm = () => {
        setShowLoginForm(true);
    };

    const handleCloseLoginForm = () => {
        setShowLoginForm(false);
    };


  const handleSubmit = async (event) => {
    event.preventDefault();
    const query = event.target.elements.q.value;

    try {
      const response = await axios.post(`${apiUrl}/search_engine/text/search/`, { query });
      setSearchResults(response.data.hits);
      console.log('Response:', response.data.hits);
      setError(null);
    } catch (error) {
      console.error('Ошибка при выполнении поиска:', error);
      setSearchResults([]);
    }
  };

  console.log('Search Results:', searchResults); // Логирование результатов поиска

    return (
        <header className="header">
            <div className="container">
                <div className="header__row">
                    <div className="header__logo">
                        <img src={logo} alt="Logo" />

                    </div>
                    <nav className="header__nav">
                        <ul>
                            <div className="search-container">
                                <form onSubmit={handleSubmit}>
                                  <input type="search" name="q" placeholder="Поиск..." />
                                  <button type="submit">Найти</button>
                                </form>
                            </div>

                            <li><Link to="/">На главную</Link></li>

                            {isLoggedIn && (

                                <li><a href="/user_courses">Мои курсы</a></li>

                            )}

                            <li><Link to="#about">О нас</Link></li>

                            {isLoggedIn ? (
                                <li><button onClick={handleLogoutClick} className="header__nav-btn">Выйти</button></li>
                            ) : (
                                <li><button onClick={handleLoginClick} className="header__nav-btn">Войти</button></li>
                            )}
                        </ul>
                    </nav>
                </div>
            </div>
            <hr className="divider" />
            <div>
              {searchResults.length > 0 ? (
                <ul>
                  <div className="course-list">
                    {searchResults.map(result => (
                      <ResultCard key={result.id} result={result} />
                    ))}
                  </div>
                </ul>
              ) : (
                <div className="error-message">
                    <p>Результаты поиска отсутствуют</p>
                </div>
              )}
            </div>
            {showLoginForm && (
                <div className="login-modal">
                    <div className="login-modal-content">
                        <LoginForm onLogin={handleLoginSuccess} />
                    </div>
                </div>
            )}
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
        <Footer />
        </header>



    );
}

export default SearchForm;