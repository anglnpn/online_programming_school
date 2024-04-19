import React, { useState, useEffect } from 'react';
import api from '../../api';
import './profile.css'; // Импорт стилей
import PersonalHeader from '../personal_header/PersonalHeader';
import { useNavigate } from 'react-router-dom';

const UserProfile = () => {
    const [userData, setUserData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [showEditModal, setShowEditModal] = useState(false);
    const [showConfirmDeleteModal, setShowConfirmDeleteModal] = useState(false);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [surname, setSurname] = useState('');
    const [country, setCountry] = useState('');
    const [city, setCity] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await api.get('/user/profile/');
                setUserData(response.data);
                setName(response.data.name); // Устанавливаем начальные значения имени и электронной почты
                setEmail(response.data.email);
                setSurname(response.data.surname);
                setCountry(response.data.country);
                setCity(response.data.city);
                setPassword(response.data.password);
                setLoading(false);
            } catch (error) {
                console.error('Ошибка при загрузке данных пользователя:', error);
            }
        };

        fetchUserData();
    },[]);

    const handleUpdateProfile = async () => {
        try {
            const response = await api.put(`/user/update/${userData.id}/`, {
                name, surname, email, password, country, city,
            });
            console.log('Профиль успешно обновлен:', response.data);
            // Обновляем информацию о пользователе после успешного обновления профиля
            setUserData(response.data);
            setShowEditModal(false); // Закрываем модальное окно после успешного обновления
        } catch (error) {
            console.error('Ошибка при обновлении профиля:', error);
        }
    };

    const handleDeleteProfile = async () => {
        setShowConfirmDeleteModal(true);
    };

    const handleDeleteConfirm = async () => {
        try {
            await api.delete(`/user/delete/${userData.id}/`);
            console.log('Профиль успешно удален');
            localStorage.removeItem('token'); // Удаление токена из localStorage
            navigate('/'); // Перенаправление на главную страницу
        } catch (error) {
            console.error('Ошибка при удалении профиля:', error);
        }
    };

    return (
        <div>
            <PersonalHeader />
            <div className="user-profile">
                <h2>Профиль пользователя</h2>
                {userData && (
                    <div className="user-profile-info">
                        <p>Имя: {userData.name}</p>
                        <p>Фамилия: {userData.surname}</p>
                        <p>Email: {userData.email}</p>
                        <p>Страна: {userData.country}</p>
                        <p>Город: {userData.city}</p>
                        <button onClick={() => setShowEditModal(true)} className="button" >Редактировать профиль</button>
                        <button onClick={handleDeleteProfile} className="button">Удалить профиль</button>
                    </div>
                )}
            </div>

            {/* Модальное окно для редактирования профиля */}
            {showEditModal && (
                <div className="modal">
                    <div className="modal-content">
                        <h3>Редактировать профиль</h3>
                        <label>
                            Имя:
                            <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                        </label>
                        <label>
                            Email:
                            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                        </label>
                        <label>
                            Фамилия:
                            <input type="text" value={surname} onChange={(e) => setSurname(e.target.value)} />
                        </label>
                        <label>
                            Страна:
                            <input type="text" value={country} onChange={(e) => setCountry(e.target.value)} />
                        </label>
                        <label>
                            Город:
                            <input type="text" value={city} onChange={(e) => setCity(e.target.value)} />
                        </label>
                        <button onClick={() => setShowEditModal(false)}>Закрыть</button>
                        <button onClick={handleUpdateProfile}>Сохранить</button>
                    </div>
                </div>
            )}

            {/* Модальное окно для подтверждения удаления профиля */}
            {showConfirmDeleteModal && (
                <div className="modal">
                    <div className="modal-content">
                        <h3>Вы уверены, что хотите удалить профиль?</h3>
                        <button onClick={handleDeleteConfirm}>Да</button>
                        <button onClick={() => setShowConfirmDeleteModal(false)}>Нет</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default UserProfile;
