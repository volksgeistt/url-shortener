# 🔗 URL Shortener
A modern, responsive URL shortening service built with Flask and vanilla JavaScript. Transform long URLs into short, shareable links with a beautiful, animated user interface.
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)
--- 
### 🚀 **Core Functionality**
- **URL Shortening**: Convert long URLs to short, shareable links using TinyURL API
- **Real-time Validation**: Instant URL validation with helpful error messages
- **Smart URL Normalization**: Automatically adds protocol if missing
- **Copy to Clipboard**: One-click copying with visual feedback
- **Visit Links**: Direct link opening in new tabs
- **Statistics Tracking**: Real-time counter of total shortened URLs

### 💻 Technical Features
- **RESTful API:** Clean Flask backend with JSON endpoints
- Data Persistence:** Local JSON file storage for URL history
- Error Handling: Comprehensive error handling with user-friendly messages
- CORS Support: Cross-origin resource sharing enabled
- Keyboard Shortcuts: Ctrl/Cmd+K to focus input, Escape to clear results
---
## 🛠️ Tech Stack
### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Requests** - HTTP library for API calls
- **JSON** - Data storage format

### Frontend
- **HTML5** - Modern semantic markup
- **CSS3** - Advanced styling with custom properties and animations
- **Vanilla JavaScript** - ES6+ features with async/await
- **Inter Font** - Google Fonts integration

### APIs
- **TinyURL API** - URL shortening service
---
## 📁 Project Structure
```bash
url-shortener/
│
├── app.py                 # Flask backend application
├── url_data.json         # Data storage (auto-generated)
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── templates/           # Flask templates directory
    └── index.html       # Main HTML template
```
---
## Data Storage
URLs are stored in `url_data.json` with the following structure:
```json
{
  "urls": [
    {
      "original": "https://example.com/very-long-url",
      "shortened": "https://tinyurl.com/abc123",
      "created_at": "2024-01-01T12:00:00.000000"
    }
  ],
  "count": 1
}
```
---
## 🚀 API Documentation
### Endpoints
POST `/shorten`
- Shorten a URL
**Request Body:**
```json
{
  "url": "https://example.com/very-long-url"
}
```
**Response:**
```json
{
  "short_url": "https://tinyurl.com/abc123",
  "original_url": "https://example.com/very-long-url",
  "total_count": 42
}
```
**Error Response:**
```json
{
  "error": "Please enter a valid URL"
}
```
GET `/stats`
- Get statistics
**Response:**
```json
{
  "total_count": 42
}
```
GET `/`
- Serve the main application page
---
## 🌐 Testing URLs
The application handles various URL formats:
- https://example.com
- http://example.com
- example.com (auto-adds https://)
- www.example.com (auto-adds https://)
---
### ⭐ Star this repository if you found it helpful!




