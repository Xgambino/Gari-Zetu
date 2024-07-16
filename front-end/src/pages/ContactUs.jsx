// ContactUs.js

import React from 'react';
import '../ContactUs.css'; // Import CSS for ContactUs styling

const ContactUs = () => {
  return (
    <div className="contact-us">
      <div className="contact-header">
        <h1>Contact Us</h1>
        <p>If you have any questions or inquiries, please feel free to contact us using the information below:</p>
      </div>
      <div className="contact-info">
        <div className="contact-details">
          <h3>Contact Details</h3>
          <p>Email: info@yourcarcompany.com</p>
          <p>Phone: 123-456-7890</p>
          <p>Address: 123 Car Street, Cityville, State, Country</p>
        </div>
        <div className="contact-map">
          <h3>Our Location</h3>
          <iframe
            title="Company Location"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d23550.198731799675!2d-0.1276256351174794!3d51.50732132934852!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNTHCsDUyJzQwLjYiTiAwwrAyNic0Mi42Ilc!5e0!3m2!1sen!2suk!4v1588965902604!5m2!1sen!2suk"
            frameBorder="0"
            allowFullScreen=""
            aria-hidden="false"
            tabIndex="0"
          ></iframe>
        </div>
      </div>
    </div>
  );
};

export default ContactUs;
