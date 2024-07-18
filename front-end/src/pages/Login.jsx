// import React, { useState } from "react";
// import { Link, useNavigate } from "react-router-dom";
// import {z} from "zod";
// import {zodResolver} from "@hook/resolver/zod";
// import toast from "react-hot-toast";
// import CatalogueVideo from "../components/CatalogueVideo.jsx";
// import '../index.css';

// const LoginSchema = z.object({
//   email: z.string().email().required(),
//   password: z.string().min(8).required(),
// });

// function Login() {
//   const [formData, setFormData] = useState({ email: "", password: "" });
//   const [isLoading, setIsLoading] = useState(false);
//   const navigate = useNavigate();

//   const handleChange = (e) => {
//     setFormData({
//       ...formData,
//       [e.target.name]: e.target.value,
//     });
//   };

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     setIsLoading(true);
 
//     setTimeout(() => {
//       console.log(formData);
//       setIsLoading(false);
//       navigate("/catalogue");
//     }, 2000);
//   };

//   return (
//     <div>
//       <CatalogueVideo />
//     <div className="container">
//       <div className="form-container sign-in">
//         <form onSubmit={handleSubmit}>
//           <h1>Login In</h1>
//           <input
//             type="email"
//             placeholder="Email"
//             name="email"
//             value={formData.email}
//             onChange={handleChange}
//             required
//           />
//           <input
//             type="password"
//             placeholder="Password"
//             name="password"
//             value={formData.password}
//             onChange={handleChange}
//             required
//           />
//           <Link to="#" className="forgot-password">
//             Forgot Your Password?
//           </Link>
//           <button type="submit" disabled={isLoading}>
//             {isLoading ? "Logging in..." : "Login"}
//           </button>
//         </form>
//       </div>
//       <TogglePanel />
//     </div>
//     </div>
//   );
// }
// function TogglePanel() {
//   return (
//     <div className="toggle-container">
//       <div className="toggle">
//         <div className="toggle-panel toggle-right">
//           <h1 >Welcome, Back!</h1>
//           <p>
//             Register with your personal details if you don't have an account,
//             create one to use all of the site's features.
//           </p>
//           <Link to="/register" className="btn btn-primary w-100">
//             Register
//           </Link>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default Login;
import { zodResolver } from '@hookform/resolvers/zod';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Controller, useForm } from 'react-hook-form';
import { z } from 'zod';
import { BASE_URL } from "../components/data/data.jsx";
import toast from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';

const schema = z.object({
	email: z
		.string()
		.email({ message: 'Enter a valid email address' })
		.min(1, { message: 'Email address is required' }),})

    export default function Login() {
      const form = useForm({
        resolver: zodResolver(schema),
        defaultValues: {
          email: '',
          password: '',
        },
      });
    
      const navigate = useNavigate();
    const onSubmit = async (values) => {
        await fetch(`${BASE_URL}/login`, {
          method: 'POST',
          body: JSON.stringify(values),
          headers: {
            'Content-Type': 'application/json',
          },
        })
    .then((res) => res.json())
          .then((data) => {
            if (data.status === 'fail') {
              toast.error(data.message);
            } else {
              const user = data.user;
              const accessToken = data.access_token;
    
              // save user session to local storage
              localStorage.setItem(
                'session',
                JSON.stringify({ user, accessToken })
              );
    toast.success(data.message);
    
              navigate('/');
            }
          })
          .catch((err) => console.log(err));
      };

    return (
        <div
          style={{
            padding: 40,
            display: 'flex',
            height: '100%',
            width: '100%',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <Form onSubmit={form.handleSubmit(onSubmit)}>
    <Controller
              control={form.control}
              name="email"
              render={({ field, fieldState }) => (
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control
                    {...field}
                    type="email"
                    placeholder="Enter email"
                  />
                  {fieldState.invalid && (
                    <Form.Text className="text-danger">
                      {fieldState.error.message}
                    </Form.Text>
                  )}
                </Form.Group>
              )}
            />
    <Controller
              control={form.control}
              name="password"
              render={({ field, fieldState }) => (
                <Form.Group
                  className="mb-3"
                  controlId="formBasicPassword"
                >
                  <Form.Label>Password</Form.Label>
                  <Form.Control
                    {...field}
                    type="password"
                    placeholder="Password"
                  />
                  {fieldState.invalid && (
                    <Form.Text className="text-danger">
                      {fieldState.error.message}
                    </Form.Text>
                  )}
                </Form.Group>
    )}
            />
    
            <Button
              variant="primary"
              type="submit"
              disabled={form.formState.isSubmitting}
            >
              {form.formState.isSubmitting ? 'Submitting...' : 'Submit'}
            </Button>
          </Form>
        </div>
      );
    }