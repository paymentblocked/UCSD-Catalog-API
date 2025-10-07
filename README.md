# UCSD Course Catalog API

A lightweight, read-only REST API providing access to UCSD course catalog information. Skip the scraping and integrate course data directly into your applications.

**Base URL:** `https://ucsd-catalogue-api.onrender.com`

**Current Data:** Fall Quarter 2025

## Overview

This API provides structured access to UCSD course catalog data including departments, courses, and sections. Perfect for building course planners, student data collection tools, or any class-related applications without the hassle of web scraping.

### Key Features
- Simple REST endpoints
- No authentication required
- JSON responses
- Read-only access
- Lightweight and fast
- Ready for immediate integration

## Quick Start

Make your first request to check API health:

```bash
curl https://ucsd-catalogue-api.onrender.com/health
```

Response:
```json
{
  "status": "ok"
}
```

Get all departments:
```bash
curl https://ucsd-catalogue-api.onrender.com/departments
```

## API Endpoints

### Health Check
**GET** `/health`

Simple health check endpoint (exempt from rate limiting).

**Response:**
```json
{
  "status": "ok"
}
```

---

### List All Departments
**GET** `/departments`

Returns all available departments with their IDs, names, and codes.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Computer Science and Engineering",
    "code": "CSE"
  },
  {
    "id": 2,
    "name": "Data Science",
    "code": "DSC"
  }
]
```

---

### Get Department by Code
**GET** `/departments/by-code/<dept_code>`

Lookup a specific department by its code (case-insensitive).

**Example:**
```bash
curl https://ucsd-catalogue-api.onrender.com/departments/by-code/CSE
```

**Response:**
```json
{
  "id": 1,
  "name": "Computer Science and Engineering",
  "code": "CSE"
}
```

**Error Response (404):**
```json
{
  "error": "department not found"
}
```

---

### List Courses by Department Code
**GET** `/departments/code/<dept_code>/courses`

Get all courses for a specific department using its code.

**Example:**
```bash
curl https://ucsd-catalogue-api.onrender.com/departments/code/DSC/courses
```

**Response:**
```json
[
  {
    "id": 101,
    "course_number": "10",
    "title": "Principles of Data Science"
  },
  {
    "id": 102,
    "course_number": "20",
    "title": "Programming and Basic Data Structures for Data Science"
  }
]
```

---

### List Course Sections
**GET** `/departments/code/<dept_code>/courses/<course_number>/sections`

Get all sections for a specific course. If multiple course entries exist with the same course number, sections from all matching courses will be returned with their `course_id` for distinction.

**Example:**
```bash
curl https://ucsd-catalogue-api.onrender.com/departments/code/CSE/courses/11/sections
```

**Response:**
```json
[
  {
    "id": 501,
    "course_id": 105,
    "meeting_type": "LE",
    "section": "A00",
    "days": "MWF",
    "time": "10:00-10:50",
    "building": "PCYNH",
    "room": "106",
    "instructor": "Cao, Y.",
    "section_id": "CSE11-A00"
  }
]
```

---

### Search Courses
**GET** `/search?q=<search_term>`

Search across course titles and department names.

**Example:**
```bash
curl https://ucsd-catalogue-api.onrender.com/search?q=data
```

**Response:**
```json
[
  {
    "course_id": 101,
    "course_number": "10",
    "title": "Principles of Data Science",
    "department": "Data Science"
  },
  {
    "course_id": 102,
    "course_number": "20",
    "title": "Programming and Basic Data Structures for Data Science",
    "department": "Data Science"
  }
]
```

**Error Response (400):**
```json
{
  "error": "query param q is required"
}
```

## Rate Limiting

To ensure fair usage and API stability:

- **Limit:** 60 requests per 60 seconds per IP address
- **Response when exceeded:** HTTP 429 (Too Many Requests)
- **Exempt endpoint:** `/health` is not rate limited

**Best Practices:**
- Cache responses when possible
- Implement exponential backoff on 429 errors
- Consider batching requests when building applications

## Response Format

### Success Response
All successful responses return JSON with HTTP status 200.

### Error Responses

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Missing required parameters |
| 404 | Not Found - Resource doesn't exist |
| 405 | Method Not Allowed - Only GET requests accepted (read-only API) |
| 429 | Too Many Requests - Rate limit exceeded |

**Error Response Format:**
```json
{
  "error": "description of error"
}
```

## Example Use Cases

### Building a Course Planner
Fetch all departments, let users select courses, and display available sections with times and locations.

### Student Survey Tool
Query course information to help students find specific classes or gather data about course offerings.

### Schedule Conflict Checker
Pull section times to help students identify scheduling conflicts when planning their quarters.

### Department Browser
Create a searchable interface for exploring courses across different departments.

## Data Freshness

- **Current Term:** Fall Quarter 2025 (UCSD)
- **Update Frequency:** Quarterly (approximately every 3 months)
- Data is read-only and reflects the official UCSD course catalog at the time of the last update

## CORS Support

Cross-Origin Resource Sharing (CORS) is enabled, allowing you to make requests from web browsers across different domains.

## Integration Examples

### JavaScript (Fetch API)
```javascript
fetch('https://ucsd-catalogue-api.onrender.com/departments/code/CSE/courses')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### Python (requests)
```python
import requests

response = requests.get('https://ucsd-catalogue-api.onrender.com/search?q=data')
courses = response.json()
print(courses)
```

### cURL
```bash
curl -X GET "https://ucsd-catalogue-api.onrender.com/departments/code/DSC/courses/10/sections"
```

## Terms of Use

### Acceptable Use
- Use for personal projects and applications
- Build tools that help students
- Educational and research purposes
- Reasonable request rates within limits

### Prohibited Use
- Excessive scraping or abuse of the API
- Attempting to bypass rate limits
- Using the API for malicious purposes
- Redistributing data in violation of UCSD policies

**Note:** This API provides publicly available course catalog information. Users are responsible for ensuring their use complies with UCSD policies and applicable laws.

## Support & Contact

Having issues or questions?

- **GitHub:** Open an issue on the project repository
- **Discord:** `rmgmt`

Please include:
- The endpoint you're trying to use
- Your request example
- The error message or unexpected behavior

## Notes

- This is a **read-only API** - only GET requests are accepted
- All requests must use HTTPS
- The API uses SQLite for lightweight, efficient data storage
- Response times are typically under 100ms for most queries

---