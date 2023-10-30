import React, { useState } from 'react';
import '../loginPage.css';


function LoginForm() {
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('ID:', id, 'Password:', password);
        // 여기에 로그인 로직을 추가할 수 있습니다.
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="w-[315px] h-[60px] absolute left-[563px] top-[528px]">
                <input
                    value={id}
                    onChange={(e) => setId(e.target.value)}
                    className="w-[315px] h-[60px] absolute left-[-1px] top-[-1px] rounded-[5px] bg-[#f2f5f6] pl-8"
                    placeholder='id'
                />
            </div>
            <div className="w-[315px] h-[60px] absolute left-[563px] top-[603px]">
                <input
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-[315px] h-[60px] absolute left-[-1px] top-[-1px] rounded-[5px] bg-[#f2f5f6] pl-8"
                    placeholder='password'
                    type='password'
                />
            </div>
            <div className="w-[315px] h-[60px] absolute left-[563px] top-[702px]">
                <button type="submit" className="w-[315px] h-[60px] absolute left-[-1px] top-[-1px] rounded-[5px] bg-[#4880ee] text-base font-bold text-center text-white flex items-center justify-center">
                    LOGIN
                </button>
            </div>
        </form>
    );
}

export default LoginForm;