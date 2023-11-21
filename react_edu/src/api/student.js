import axios from 'axios';

const BASE_URL = `${process.env.REACT_APP_EDU_PROTOCOL}://${process.env.REACT_APP_EDU_URL}:${process.env.REACT_APP_EDU_PORT}/api`;
const Authorization = `Basic ${process.env.REACT_APP_EDU_FRONT_ID} ${process.env.REACT_APP_EDU_FRONT_CLIENT_SECRET}`

const login = async (username, password) => {

    console.log('aaa')
    try {
        const response = await axios.post(`${BASE_URL}/login/`, {
            username,
            password
        }, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': Authorization
                // CSRF 토큰은 필요한 경우에만 추가
                // 'X-CSRFToken': 'your-csrf-token-here'
            }
        });

        console.log(response)

        return response.data; // 여기서는 응답 데이터를 반환합니다.
    } catch (error) {
        console.error('Login error', error);
        return null; // 오류 발생 시 null 반환
    }
};

export { login };