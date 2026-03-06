from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

# Your Gemini API key
GEMINI_API_KEY = 'AIzaSyDHYPg84NaVENwxyQD-g2buStPs-Rvbo3Y'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'

def get_intelligent_response(message):
    """Provide intelligent responses for college-related questions"""
    message_lower = message.lower()
    
    # Admission related
    if any(word in message_lower for word in ['admission', 'join', 'apply', 'get admission', 'how to join']):
        return "🎓 **Admission Information:**\n\nTo get admission at Vardhaman College of Engineering:\n\n• **B.Tech Programs:** CSE, ECE, EEE, Civil, Mechanical\n• **Eligibility:** 10+2 with Mathematics, Physics, Chemistry\n• **Process:** EAMCET/Management Quota\n• **Contact:** admissions@vce.ac.in | +91-40-2401-2345\n\n📍 **Campus Address:**\nVardhaman College of Engineering\nShamshabad, Hyderabad - 501218\n\nVisit our website for detailed admission guidelines!"
    
    # Courses related
    elif any(word in message_lower for word in ['courses', 'branches', 'programs', 'departments', 'what courses', 'subjects']):
        return "📚 **Courses Offered at VCE:**\n\n**Undergraduate Programs (B.Tech):**\n\n• **Computer Science Engineering (CSE)**\n  - AI/ML, Data Science, Cyber Security\n\n• **Electronics & Communication Engineering (ECE)**\n  - VLSI, Embedded Systems, IoT\n\n• **Electrical & Electronics Engineering (EEE)**\n  - Power Systems, Control Systems\n\n• **Civil Engineering**\n  - Structural Engineering, Transportation\n\n• **Mechanical Engineering**\n  - Thermal Engineering, Design Engineering\n\n**Duration:** 4 Years (8 Semesters)\n**Intake:** 180 per branch (approx.)"
    
    # Fees related
    elif any(word in message_lower for word in ['fees', 'fee structure', 'cost', 'payment', 'tuition']):
        return "💰 **Fee Structure:**\n\n**B.Tech Program Fees (Annual):**\n\n• **Tuition Fee:** ₹95,000 - ₹1,20,000\n• **Hostel Fee:** ₹60,000 - ₹80,000\n• **Mess Fee:** ₹40,000 - ₹50,000\n• **Other Fees:** ₹15,000 - ₹20,000\n\n**Total Annual Cost:** ₹2,10,000 - ₹2,70,000\n\n**Scholarships Available:**\n• Merit-based scholarships\n• EWS scholarships\n• Government scholarships\n\n*Note: Fees are subject to change. Contact office for exact amounts.*"
    
    # Placement related
    elif any(word in message_lower for word in ['placement', 'job', 'career', 'salary', 'package', 'companies']):
        return "🚀 **Placement & Career:**\n\n**VCE Placement Highlights:**\n\n• **Highest Package:** ₹12 LPA\n• **Average Package:** ₹4.5 LPA\n• **Placement Rate:** 85%+\n\n**Top Recruiters:**\n• Tech: TCS, Infosys, Wipro, HCL, Cognizant\n• Core: BHEL, BEL, ECIL, DRDO\n• Startups: Many MNCs and startups\n\n**Training & Development:**\n• Aptitude & Technical Training\n• Soft Skills Development\n• Mock Interviews\n• Industry Expert Sessions\n\n**Contact Placement Cell:**\nplacement@vce.ac.in | +91-40-2401-2346"
    
    # Campus/Facilities related
    elif any(word in message_lower for word in ['campus', 'facilities', 'infrastructure', 'library', 'sports', 'hostel']):
        return "🏫 **Campus & Facilities:**\n\n**Campus Area:** 30+ acres with lush greenery\n\n**Academic Facilities:**\n• Modern classrooms with smart boards\n• Well-equipped laboratories\n• Central library with 50,000+ books\n• Computer centers with high-speed internet\n\n**Campus Life:**\n• Separate hostels for boys & girls\n• Sports: Cricket, Football, Basketball, Volleyball\n• Gymnasium and indoor games\n• Cafeteria with hygienic food\n• 24/7 medical facility\n• Transportation service\n\n**Location Advantage:**\n• Near Hyderabad International Airport\n• Well-connected by public transport\n• Safe and secure environment"
    
    # Contact/Location related
    elif any(word in message_lower for word in ['contact', 'phone', 'email', 'address', 'location', 'where', 'reach']):
        return "📞 **Contact Information:**\n\n**Vardhaman College of Engineering**\n📍 **Address:**\nKacharam, Shamshabad\nHyderabad - 501218\nTelangana, India\n\n**📧 Email:**\n• General: info@vce.ac.in\n• Admissions: admissions@vce.ac.in\n• Placements: placement@vce.ac.in\n\n**📞 Phone:**\n• Office: +91-40-2401-2345\n• Admissions: +91-40-2401-2346\n• Placements: +91-40-2401-2347\n\n**🌐 Website:** www.vce.ac.in\n\n**📍 How to Reach:**\n• 15 km from Hyderabad Airport\n• 25 km from Secunderabad Railway Station\n• Well-connected by TSRTC buses"
    
    # Default response
    else:
        return "👋 **Welcome to Vardhaman College of Engineering!**\n\nI'm here to help you with information about:\n\n• 🎓 **Admissions** - How to join VCE\n• 📚 **Courses** - B.Tech programs offered\n• 💰 **Fees** - Fee structure and scholarships\n• 🚀 **Placements** - Career opportunities\n• 🏫 **Campus** - Facilities and infrastructure\n• 📞 **Contact** - How to reach us\n\nPlease feel free to ask me anything about VCE! What would you like to know?"

@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    # Handle CORS preflight request
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'success'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Use intelligent responses
        response = get_intelligent_response(message)
        
        # Create response with CORS headers
        response = jsonify({
            'response': response,
            'success': True
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        
        return response
        
    except Exception as e:
        print(f"Error: {str(e)}")
        # Create error response with CORS headers
        response = jsonify({
            'error': str(e),
            'fallback': 'I apologize, but I encountered an error. Please try again later.'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        
        return response, 500

# For Vercel serverless functions
def handler(request):
    return app(request.environ, lambda status, headers: None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
