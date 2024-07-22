import axios from "axios";
import { useState } from "react";

function Login() {
    const [userLogin, setUserLogin] = useState({
        username: '',
        password: ''
    });

    const handleChange = (event) => {
        setUserLogin({ ...userLogin, [event.target.name]: event.target.value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        
        try {
            const response = await axios.post('http://127.0.0.1:5000/login', JSON.stringify(userLogin), { headers: { 'Content-Type': 'application/json' }})
            localStorage.setItem("access_token", response.data.access_token);
            alert("Login successful");
        } catch (error) {
            console.log('Error registering user:', error);
        }
    };
    return (
        <div>
            <form method="post">
                <input type="text" id="" placeholder="username" name="username" value={userLogin.username} onChange={handleChange} />
                <input type="password" placeholder="password" value={userLogin.password} name="password" onChange={handleChange} />
            </form>
            <button type="submit" onClick={handleSubmit} >Log In</button>
        </div>
    );
};

export default Login;

