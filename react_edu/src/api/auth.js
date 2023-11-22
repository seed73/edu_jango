import axios from 'axios';
import Cookie from 'js-cookie';

const BASE_URL = `${process.env.REACT_APP_EDU_PROTOCOL}://${process.env.REACT_APP_EDU_URL}:${process.env.REACT_APP_EDU_PORT}/api`;
const LoginAuthorization = btoa(`Basic ${process.env.REACT_APP_EDU_FRONT_ID} ${process.env.REACT_APP_EDU_FRONT_CLIENT_SECRET}`)

const login = async (username, password) => {
    try {
        const response = await axios.post(`${BASE_URL}/login/`, {
            username,
            password
        }, {
            headers: {
                'Content-Type': 'application/json',
                'LoginAuthorization': LoginAuthorization
            }
        });
        if (response.status === 200){
            response.error = false;
            setToken(response.data);
        }
        return response; // 여기서는 응답 데이터를 반환합니다.
    } catch (error) {
        console.error('Login error', error);
        return null; // 오류 발생 시 null 반환
    }
};



const setToken = (data) => {
  //max-age는 expires 옵션의 대안으로, 쿠키 만료 기간을 설정할 수 있게 해줍니다. 현재부터 설정하고자 하는 만료일시까지의 시간을 초로 환산한 값을 설정합니다.
  const hour = 1 / 24; // 1일 (24시간)
  Cookie.set('access_token', data.access_token, { expires: hour });
  Cookie.set('refresh_token', data.refresh_token, { expires: hour });
}


export { login };