import React from 'react';
import { Navigate } from 'react-router-dom';
import { isAuthenticated } from '../utils/auth.js';

export const ProtectedRoute = ({ children }) => {
  if (!isAuthenticated()) {
    // 인증되지 않았다면 로그인 페이지로 리디렉션
    return <Navigate to="/login" />;
  }

  return children;
};
