// Chatbot functionality
const chatbotBubble = document.getElementById('chatbotBubble');
const chatbotWindow = document.getElementById('chatbotWindow');
const closeChatbot = document.getElementById('closeChatbot');
const sendMessage = document.getElementById('sendMessage');
const userInput = document.getElementById('userInput');
const chatMessages = document.getElementById('chatMessages');

// Toggle chatbot window
chatbotBubble.addEventListener('click', () => {
    chatbotWindow.classList.add('active');
});

closeChatbot.addEventListener('click', () => {
    chatbotWindow.classList.remove('active');
});

// Gemini API configuration
const GEMINI_API_KEY = 'AIzaSyDHYPg84NaVENwxyQD-g2buStPs-Rvbo3Y'; // Replace with your actual API key
const GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent';

// Function to send message to Gemini API via local server
async function sendToGemini(message) {
    try {
        console.log('Sending message:', message);
        const response = await fetch('http://localhost:5000/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message
            })
        });

        console.log('Response status:', response.status);
        
        if (!response.ok) {
            throw new Error(`Server Error: ${response.status}`);
        }

        const data = await response.json();
        console.log('Response data:', data);
        
        if (data.success && data.response) {
            return data.response;
        } else if (data.fallback) {
            return data.fallback;
        } else {
            throw new Error('Invalid server response');
        }
    } catch (error) {
        console.error('Error calling chat API:', error);
        
        // Fallback responses for common college questions
        const fallbackResponses = {
            'admission': 'For admission to Vardhaman College of Engineering, please visit our official website or contact the admissions office. We offer various B.Tech programs in CSE, ECE, EEE, Civil, and Mechanical Engineering.',
            'courses': 'VCE offers B.Tech programs in Computer Science Engineering, Electronics & Communication Engineering, Electrical & Electronics Engineering, Civil Engineering, and Mechanical Engineering.',
            'fees': 'For detailed fee structure, please contact the college administration or check the official website.',
            'placement': 'VCE has excellent placement records with top companies visiting campus. For detailed statistics, please contact the placement cell.',
            'contact': 'You can contact Vardhaman College of Engineering at our campus in Shamshabad, Hyderabad - 501218.',
            'location': 'VCE is located in Shamshabad, Hyderabad - 501218, near the international airport.',
            'default': 'I apologize, but I\'m having trouble connecting to my AI service right now. For detailed information about Vardhaman College of Engineering, please visit our official website or contact the college administration.'
        };
        
        const lowerMessage = message.toLowerCase();
        for (const [key, response] of Object.entries(fallbackResponses)) {
            if (lowerMessage.includes(key)) {
                return response;
            }
        }
        
        return fallbackResponses.default;
    }
}

// Function to add message to chat
function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    
    const messageContent = document.createElement('p');
    messageContent.textContent = message;
    
    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Function to show typing indicator
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message typing-indicator';
    typingDiv.id = 'typingIndicator';
    
    const typingContent = document.createElement('p');
    typingContent.innerHTML = '<span class="typing-dots">•</span><span class="typing-dots">•</span><span class="typing-dots">•</span>';
    
    typingDiv.appendChild(typingContent);
    chatMessages.appendChild(typingDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Function to remove typing indicator
function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

// Function to handle user message
async function handleUserMessage() {
    const message = userInput.value.trim();
    
    if (message === '') return;
    
    // Add user message
    addMessage(message, true);
    
    // Clear input
    userInput.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    
    // Send to Gemini and get response
    const response = await sendToGemini(message);
    
    // Remove typing indicator
    removeTypingIndicator();
    
    // Add bot response
    addMessage(response);
}

// Event listeners
sendMessage.addEventListener('click', handleUserMessage);

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleUserMessage();
    }
});

// Login form handling
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Get form values
    const username = loginForm.querySelector('input[type="text"]').value;
    const password = loginForm.querySelector('input[type="password"]').value;
    
    // Simple validation (in real app, this would be server-side)
    if (username && password) {
        // Show success message
        const successMessage = document.createElement('div');
        successMessage.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #4caf50;
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 10000;
            animation: slideIn 0.3s ease;
        `;
        successMessage.textContent = 'Login successful! Welcome to VCE Portal.';
        document.body.appendChild(successMessage);
        
        // Remove message after 3 seconds
        setTimeout(() => {
            successMessage.remove();
        }, 3000);
        
        // Reset form
        loginForm.reset();
    }
});

// Add typing animation CSS
const style = document.createElement('style');
style.textContent = `
    .typing-indicator .typing-dots {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #1a237e;
        margin: 0 2px;
        animation: typing 1.4s infinite ease-in-out;
    }
    
    .typing-indicator .typing-dots:nth-child(1) {
        animation-delay: -0.32s;
    }
    
    .typing-indicator .typing-dots:nth-child(2) {
        animation-delay: -0.16s;
    }
    
    @keyframes typing {
        0%, 80%, 100% {
            transform: scale(0.8);
            opacity: 0.5;
        }
        40% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);

// Welcome message when chatbot opens
chatbotBubble.addEventListener('click', () => {
    setTimeout(() => {
        if (chatMessages.children.length === 1) {
            addMessage('Welcome to Vardhaman College of Engineering! I\'m here to help you with information about admissions, courses, facilities, and more. What would you like to know?');
        }
    }, 500);
});

// Auto-resize textarea for longer messages
userInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 100) + 'px';
});
