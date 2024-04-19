import React from 'react';
import './ConfirmLogoutModal.css'; // импорт стилей

const ConfirmLogoutModal = ({ onConfirm, onCancel }) => {
    return (
        <div className="confirm-logout-modal">
            <div className="modal-content">
                <p>Вы точно хотите выйти?</p>
                <button onClick={onConfirm} className="confirm-button-yes">Да</button>
                <button onClick={onCancel} className="cancel-button-no">Нет</button>
            </div>
        </div>
    );
};

export default ConfirmLogoutModal;
