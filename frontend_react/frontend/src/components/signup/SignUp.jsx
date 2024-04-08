import React, { useState } from 'react';
import LoginForm from '../login/LoginForm';
import RegistrationForm from '../registration/RegistrationForm';


const SignUp = () => {
    const [isLoginFormVisible, setIsLoginFormVisible] = useState(true);
    const [isRegistrationFormVisible, setIsRegistrationFormVisible] = useState(false);

    const handleLogin = () => {
        setIsLoginFormVisible(true);
        setIsRegistrationFormVisible(false);
    };

    const handleRegister = () => {
        setIsLoginFormVisible(false);
        setIsRegistrationFormVisible(true);
    };

    return (
        <div>
            {isLoginFormVisible && (
                <LoginForm onLogin={handleLogin} onRegister={handleRegister} />
            )}
            {isRegistrationFormVisible && (
                <RegistrationForm onRegister={handleRegister} />
            )}
        </div>
    );
};

export default SignUp;