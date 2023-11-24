import React, { useState } from 'react';
import '../../css/LoginPage.css';
import { login } from '../../../../api/auth.js';

function LoginForm() {
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const res = await login(id, password);
        console.log(res.error);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <input
                    value={id}
                    onChange={(e) => setId(e.target.value)}
                    className="login-input"
                    placeholder='id'
                />
            </div>
            <div>
                <input
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="login-input"
                    placeholder='password'
                    type='password'
                />
            </div>
            <div className="login-button-container">
                <button type="submit" className="login-button">
                    LOGIN
                </button>
            </div>
        </form>
    );
}

export default LoginForm;