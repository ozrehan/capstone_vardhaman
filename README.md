# Vardhaman College of Engineering - AI Chatbot Website

A modern college website with an integrated AI chatbot powered by Google's Gemini API, optimized for Vercel deployment.

## Features

- **Beautiful Login Interface**: Professional login page with Vardhaman College branding
- **Floating AI Chatbot**: Interactive chatbot with smooth animations and modern UI
- **Vercel Serverless Functions**: Backend API deployed as Vercel functions
- **Gemini AI Integration**: Powered by Google's Gemini API for intelligent responses
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern Animations**: Smooth transitions, hover effects, and micro-interactions

## 🚀 Vercel Deployment

### Quick Deploy (Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Ready for Vercel deployment"
   git push origin main
   ```

2. **Deploy on Vercel**:
   - Visit [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Connect your GitHub repository
   - Click "Deploy"

### Manual Deployment Steps

1. **Repository Structure**:
   ```
   srinidhi/
   ├── api/
   │   ├── index.py          # Vercel serverless function
   │   └── __init__.py       # Python package file
   ├── index.html             # Main HTML file
   ├── styles.css             # Complete styling
   ├── script.js              # JavaScript functionality
   ├── vercel.json           # Vercel configuration
   └── README.md             # This file
   ```

2. **Vercel Configuration** (`vercel.json`):
   - Routes `/api/*` to serverless functions
   - Routes all other requests to `index.html`
   - Python 3.9 runtime for API functions

3. **API Endpoint**:
   - Frontend calls `/api/chat` (no localhost needed)
   - CORS enabled for cross-origin requests
   - Intelligent fallback responses included

## 📁 Project Structure

```
├── api/
│   ├── index.py          # Serverless function for chat API
│   └── __init__.py       # Python package initializer
├── index.html             # Main website
├── styles.css             # Styling and animations
├── script.js              # Frontend JavaScript
├── vercel.json           # Vercel deployment config
└── README.md             # Documentation
```

## 🔧 API Configuration

The chatbot uses intelligent responses without requiring API keys in production:

- **Admission Queries**: Detailed admission process and contact info
- **Course Information**: Complete B.Tech program details
- **Fee Structure**: Comprehensive fee breakdown
- **Placement Data**: Top companies and salary packages
- **Campus Facilities**: Infrastructure and amenities
- **Contact Information**: Address, phone, email details

## 🌐 Deployment URLs

After deployment, your website will be available at:
- **Primary**: `https://your-project-name.vercel.app`
- **API Endpoint**: `https://your-project-name.vercel.app/api/chat`

## 🎨 Customization

### Changing the Background

Update the CSS in `styles.css`:

```css
.background-container {
    background-image: url('your-image-path.jpg');
}
```

### Modifying Chatbot Responses

Edit `api/index.py` in the `get_intelligent_response()` function:

```python
def get_intelligent_response(message):
    message_lower = message.lower()
    
    if 'your-keyword' in message_lower:
        return "Your custom response here"
```

### Color Scheme

Primary colors used:
- Primary: `#1a237e` (Deep Blue)
- Secondary: `#3949ab` (Lighter Blue)

## 📱 Browser Support

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support (with webkit prefixes)
- Mobile browsers: Full support

## 🔒 Security Notes

- No API keys exposed in frontend code
- Serverless functions handle backend logic
- CORS properly configured
- Input validation and error handling

## 🐛 Troubleshooting

### Deployment Issues
- Ensure `vercel.json` is in root directory
- Check `api/index.py` syntax and imports
- Verify all files are committed to Git

### Chatbot Not Responding
- Check Vercel function logs
- Verify `/api/chat` route is accessible
- Test with browser console for errors

### Styling Issues
- Clear browser cache
- Ensure CSS files are properly linked
- Check responsive design on different devices

## 📄 License

This project is for educational purposes. Please ensure you have proper rights to use any images or content.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For deployment issues:
- Check Vercel deployment logs
- Verify repository structure
- Ensure all dependencies are compatible

For chatbot issues:
- Test API endpoint directly
- Check browser console for errors
- Verify CORS configuration
