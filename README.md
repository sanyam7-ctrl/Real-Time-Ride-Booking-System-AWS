# Real-Time Ride Booking System using AWS Serverless Architecture

> A cloud-native, serverless ride booking system built using AWS services to automate ride requests, driver assignment, data storage, and real-time notifications.

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-success)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
---

# Project Overview

The Real-Time Ride Booking System is a serverless cloud application developed using Amazon Web Services (AWS). The project simulates the backend workflow of modern ride-hailing platforms by automating ride requests, assigning drivers, storing ride details, and sending instant notifications.

The application is built entirely using AWS managed services, eliminating the need to manage physical or virtual servers while ensuring scalability, availability, and cost efficiency.

---

# Objectives

- Develop a real-time ride booking backend.
- Implement serverless computing using AWS Lambda.
- Store ride information in DynamoDB.
- Send real-time notifications using Amazon SNS.
- Demonstrate Event-Driven Architecture.
- Build a scalable cloud-native application.

---

# Key Features

✅ Real-Time Ride Booking

✅ Automatic Driver Assignment

✅ Unique Ride ID Generation

✅ REST API using API Gateway

✅ Serverless Backend

✅ NoSQL Database

✅ Email Notification to Driver

✅ Event-Driven Workflow

---

# AWS Services Used

| AWS Service | Purpose |
|-------------|---------|
| AWS Lambda | Executes backend business logic |
| Amazon API Gateway | Receives HTTP requests and triggers Lambda |
| Amazon DynamoDB | Stores ride details and ride status |
| Amazon SNS | Sends real-time email notifications |
| AWS IAM | Provides secure permissions between AWS services |

---

# System Architecture

```
                  User
                    │
          HTTP Request (POST)
                    │
                    ▼
          Amazon API Gateway
                    │
             Trigger Request
                    │
                    ▼
              AWS Lambda
          (Business Logic)
            │           │
            │           │
            ▼           ▼
 Amazon DynamoDB     Amazon SNS
(Store Ride Data)   (Notification)
            │
            ▼
     Ride Information
```

---

# Project Workflow

1. User submits a ride request.

2. Amazon API Gateway receives the request.

3. API Gateway invokes AWS Lambda.

4. Lambda generates a unique Ride ID.

5. Lambda assigns an available driver.

6. Ride details are stored in DynamoDB.

7. Lambda publishes a notification to SNS.

8. SNS sends an email notification to the driver.

9. API returns the assigned driver and ride details.

---

# Database Structure

 DynamoDB Table : `Rides`

| Attribute | Description |
|-----------|-------------|
| ride_id | Unique Ride Identifier |
| user_id | User requesting ride |
| driver_id | Assigned Driver |
| status | Ride Status |

---

# Project Structure

```
Real-Time-Ride-Booking-System-AWS
│
├── lambda_function.py
├── README.md
├── Project_Report.pdf
├── Project_Presentation.pptx
├── Architecture_Diagram.png
│
├── screenshots
│   ├── lambda.png
│   ├── api_gateway.png
│   ├── dynamodb.png
│   ├── sns.png
│   ├── email_notification.png
│
└── assets
```

---

# Screenshots

 AWS Lambda

<img width="1600" height="623" alt="image" src="https://github.com/user-attachments/assets/2d08f222-79ca-405a-84c6-45fc0ace3e71" />


---

## Amazon API Gateway

<img width="1600" height="675" alt="image" src="https://github.com/user-attachments/assets/5fa65833-3faa-4baf-9176-56d60483b364" />


---

## Amazon DynamoDB

<img width="945" height="462" alt="image" src="https://github.com/user-attachments/assets/5936d0f6-ef99-4b4d-867d-86b92fce6134" />


---

## Amazon SNS

<img width="1600" height="615" alt="image" src="https://github.com/user-attachments/assets/d6be1dab-19ee-4e2a-85f8-0d96c59bfe99" />


---

## Email Notification

<img width="630" height="244" alt="image" src="https://github.com/user-attachments/assets/99b1bc3e-84c8-4d66-afa2-1e1b6b3035b7" />


---

# Security

The project follows basic cloud security practices.

- IAM Roles for secure access
- Least Privilege Principle
- Managed AWS Services
- Controlled API access through API Gateway

---

# Performance & Availability

- Fully Serverless Architecture
- Automatic Scaling
- Low-Latency Data Access
- Highly Available AWS Managed Services
- Event-Driven Processing

---

# Testing

The project was tested using:

- AWS Lambda Test Events
- API Gateway Endpoint
- DynamoDB Record Verification
- SNS Email Notification

---

# Future Enhancements

- User Authentication
- Driver Authentication
- Live GPS Tracking
- Ride Cancellation
- Payment Gateway Integration
- Mobile Application
- Admin Dashboard
- Ride History
- Driver Availability Management

---

# Technologies Used

- Python
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SNS
- IAM
- REST API
- Cloud Computing
- Serverless Architecture

---

# Learning Outcomes

This project helped in understanding:

- Serverless Computing
- Event-Driven Architecture
- REST APIs
- AWS Cloud Services
- NoSQL Database Design
- IAM Roles & Permissions
- Cloud Application Deployment

---

# Author

**Sanyam**

B.Tech Computer Science Engineering

Cloud Computing | AWS | Python | Backend Development

---

# ⭐ If you found this project useful, consider giving it a Star!
