# Vardhaman College of Engineering - AI Chatbot Website

A modern college website with an integrated AI chatbot powered by Google's Gemini API.

## Features

- **Beautiful Login Interface**: Professional login page with Vardhaman College branding
- **Floating AI Chatbot**: Interactive chatbot with smooth animations and modern UI
- **Gemini AI Integration**: Powered by Google's Gemini API for intelligent responses
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern Animations**: Smooth transitions, hover effects, and micro-interactions

## Setup Instructions

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 2. Configure the API Key

Open `script.js` and replace `YOUR_GEMINI_API_KEY` with your actual API key:

```javascript
const GEMINI_API_KEY = 'your-actual-api-key-here'; // Replace with your actual API key
```

### 3. Run the Website

Simply open `index.html` in your web browser, or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js (if you have http-server installed)
npx http-server

# Then visit http://localhost:8000
```

## File Structure

```
srinidhi/
├── index.html          # Main HTML file
├── styles.css          # Complete styling
├── script.js           # JavaScript functionality
└── README.md          # This file
```

## Chatbot Features

- **Smart Responses**: AI-powered responses about college information
- **Typing Indicators**: Shows when the bot is "thinking"
- **Message History**: Maintains conversation context
- **Smooth Animations**: Professional chat interface
- **Mobile Friendly**: Works on all device sizes

## Customization

### Changing the Background

To use your own college building image, update the CSS in `styles.css`:

```css
.background-container {
    background-image: url('your-image-path.jpg');
}
```

### Modifying Chatbot Behavior

Edit the prompt in `script.js` to customize the chatbot's personality:

```javascript
text: `You are a helpful assistant for Vardhaman College of Engineering. 
        Provide helpful, accurate, and professional responses about the college, 
        courses, facilities, admission process, and general information. 
        Be friendly and concise. User message: ${message}`
```

### Color Scheme

The primary colors used are:
- Primary: `#1a237e` (Deep Blue)
- Secondary: `#3949ab` (Lighter Blue)

## Browser Support

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support (with webkit prefixes)
- Mobile browsers: Full support

## Security Notes

- Keep your Gemini API key secure and never commit it to version control
- For production use, consider implementing server-side API calls
- Add rate limiting to prevent API abuse

## Troubleshooting

### Chatbot Not Responding
1. Check if your Gemini API key is correctly set
2. Ensure you have internet connection
3. Check browser console for error messages

### Styling Issues
1. Clear browser cache
2. Ensure all files are in the same directory
3. Check browser compatibility

## License

This project is for educational purposes. Please ensure you have proper rights to use any images or content.

## Support

For issues or questions, please check the browser console for error messages first.
