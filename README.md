# FastAPI Backend Service for Android Notifications

A backend service built with FastAPI that provides user authentication, database management, Firebase Cloud Messaging (FCM) notifications, and notification history for an Android device.

The backend exposes REST APIs that can be tested through Swagger UI. Users can register and log in using JWT authentication, send notifications to an Android device through Firebase Cloud Messaging, store notification details in the database, and retrieve previously sent notifications.

---

## Project Overview

This project provides a backend service for sending notifications from an API to an Android device.

The application handles the complete backend process including:

- User registration
- User authentication
- JWT token generation
- Protected API access
- Database operations
- Database migrations
- Firebase Cloud Messaging integration
- Sending notifications to an Android device
- Storing notification details
- Retrieving notification history
- API documentation using Swagger
- Containerized application setup using Docker

The backend is designed so that the application can be run locally or through Docker.

---

# Technologies and Software Used

## Python

Python is used as the main programming language for developing the backend.

Python provides a simple and maintainable environment for building the API and integrating the database and Firebase services.

## FastAPI

FastAPI is used as the backend web framework.

It is responsible for:

- Creating REST API endpoints
- Handling HTTP requests and responses
- Request validation
- Authentication integration
- API documentation
- Communication between the client, database, and Firebase

FastAPI automatically provides interactive Swagger documentation for the available API endpoints.

## Uvicorn

Uvicorn is used as the ASGI server to run the FastAPI application.

The application can be started using:

```bash
uvicorn app.main:app --reload
