import { Box, Card, CardHeader, CardBody, Divider, FormLabel, Button } from '@chakra-ui/react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import ToDoList from './ToDoList';

function Dashboard() {
    const [userInfo, setUserInfo] = useState(null);
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('access_token');
        setUserInfo(null);
        navigate('/');
    }

    useEffect(() => {
        const fetchUserInfo = async () => {
            try {
                const token = localStorage.getItem('access_token');
                console.log('Token:', token);
                const response = await axios.get("http://127.0.0.1:5000/get_name", {
                    headers: { 'Authorization': `Bearer ${token}` }
                });
                setUserInfo(response.data)
                console.log('Response object:', response.data)
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        };
        fetchUserInfo();
    }, []);


    return (
        <Box display='flex' alignItems='center' justifyContent='center' bg="#B1AFFF" height='1200px'>
            <Card width='60%' p={5} fontSize='18px'>
                <CardHeader align='center' fontSize='30px'>
                    <h1>Dashboard</h1>
                </CardHeader>
                <Divider borderColor='#B1AFFF'></Divider>
                {userInfo ? (
                    <CardBody>
                        <h1>Welcome {userInfo?.First_name} ! </h1>
                    </CardBody>
                ) : (
                    <CardBody>
                        <p>Loading user information</p>
                    </CardBody>
                )}
                <Button width='20%' onClick={handleLogout} >Logout</Button>
                <br/>
                <section>
                    <ToDoList />
                </section>
            </Card>
        </Box>
    )
}

export default Dashboard;