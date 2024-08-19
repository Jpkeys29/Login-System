import { useParams, useNavigate, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

const AccountConfirmation = () => {
    // const {token} = useParams();
    const location = useLocation();
    const navigate = useNavigate();

    const queryParams = new URLSearchParams(location.search);
    const token = queryParams.get('token');
    
    useEffect (() => {
        const confirmEmail = async () => {
            try{
                const response = await axios.get(`http://127.0.0.1:5000/api/confirm?token=${token}`);
                console.log('Token:', token);
                console.log('Response data:', response.data);

                if (response.data.success) {
                    console.log('Email confirmed, redirecting to dashboard...')
                    navigate(response.data.redirect_url);
                } else {
                    console.log('Email confirmation failed');
                }
            }catch (error) {
                console.log('Error extracting email',error)
            }
        };
        confirmEmail();
    }, [token, navigate]);

    return(
        <div>
            <h2>Confirming email...</h2>
        </div>
    )
}

export default AccountConfirmation;