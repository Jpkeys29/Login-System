import axios from "axios";
import { useState } from "react";
import { Box, Card, CardHeader, CardBody, Divider, FormLabel, Button } from '@chakra-ui/react';
import { useNavigate } from "react-router-dom";

function Login() {
    const [userLogin, setUserLogin] = useState({
        username: '',
        password: ''
    });
    
    const navigate = useNavigate();

    const handleChange = (event) => {
        setUserLogin({ ...userLogin, [event.target.name]: event.target.value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:5000/login', JSON.stringify(userLogin), { headers: { 'Content-Type': 'application/json' } })
            console.log("FROM REACT", response);
            localStorage.setItem("access_token", response.data.access_token);
            // alert("Login successful");

            if (response.status === 200){
                navigate('/dashboard');
            } else {
                console.error('No dashboard for you!')
                alert('No dashboard for you!')
            }
        } catch (error) {
            console.log('Invalid username or email', error);
            alert("Invalid username or email. Please try again")
        }
    };
    return (
        <div>
            <form method="post">
                <FormLabel textColor='white' fontSize='20px'>Username:</FormLabel>
                <input type="text" name="username" value={userLogin.username} onChange={handleChange} />
                <FormLabel textColor='white' fontSize='20px'>Password:</FormLabel>
                <input type="password" value={userLogin.password} name="password" onChange={handleChange} />
                <br /> <br />
                <Button type="submit" onClick={handleSubmit} >Log In</Button>
            </form>
        </div>
    );
};

export default Login;

