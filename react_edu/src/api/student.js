const BASE_URL = process.env.REACT_APP_EDU_URL;

export const login = async (credentials) => {
    try {
        const response = await fetch(`${BASE_URL}/${endpoint}`, options);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return await response.json();
      } catch (error) {
        console.error('API call failed:', error);
        throw error;
      }
};
