import Cookie from 'js-cookie';

export const isAuthenticated = () => {
    if(Cookie.get('access_token') == null || Cookie.get('refresh_token') == null){
        return false;
    }
        return true;
};