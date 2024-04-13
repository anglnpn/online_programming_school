import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../search/search.css';
import logo from './../../img/icons/logo.jpg';
// импорт цвета текста
import '../../components/header/header.css';

import ResultCard from '../result_card/ResultCard';
import Header from '../header/Header';

import LoginForm from '../login/LoginForm';
import '../login/login.css';
import { Link, useNavigate } from 'react-router-dom';

const apiUrl = process.env.REACT_APP_API_URL;


const SearchForm = () => {
  const [searchResults, setSearchResults] = useState([]);
  const [error, setError] = useState(null);
  const [showLoginForm, setShowLoginForm] = useState(false);

  const handleLoginClick = () => {
        setShowLoginForm(true);
    };

    const handleLoginSuccess = () => {
        setShowLoginForm(false);
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
                        <span>OnlineSchool</span>
                    </div>
                    <nav className="header__nav">
                        <ul>
                            <div className="search-container">
                                <form onSubmit={handleSubmit}>
                                  <input type="search" name="q" placeholder="Поиск..." />
                                  <button type="submit">Найти</button>
                                </form>
                            </div>
                            <li><Link to="/search">Поисковик</Link></li>
                            <li><Link to="/">Домой</Link></li>
                            <li><Link to="#about">О нас</Link></li>
                            <li><button onClick={handleOpenLoginForm} className="header__nav-btn">Войти</button></li>
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
                <p>Результаты поиска отсутствуют</p>
              )}
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

export default SearchForm;

