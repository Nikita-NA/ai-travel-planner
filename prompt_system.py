import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class TravelPlannerPromptSystem:
    def __init__(self):
        # Get API key from environment variable
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError(
                "Please set your Google API key in the .env file. "
                "You can get a free API key from https://makersuite.google.com/app/apikey"
            )
        
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemma-3-1b-it')
        self.conversation_history = []
        
    def get_initial_prompt(self):
        return """You are an AI travel planning assistant. Your goal is to help users create personalized travel itineraries.
        Start by asking about their:
        1. Destination and travel dates
        2. Budget range
        3. Travel preferences (e.g., adventure, relaxation, culture)
        4. Any specific interests or requirements
        
        Be conversational and gather information naturally. If any details are missing, ask follow-up questions."""
    
    def get_refinement_prompt(self, user_input):
        return f"""Based on the user's input: "{user_input}"
        Analyze if we need more information about:
        1. Dietary preferences
        2. Mobility concerns
        3. Accommodation preferences
        4. Specific interests within their stated preferences
        
        If any information is missing, ask relevant follow-up questions."""
    
    def get_suggestion_prompt(self, user_preferences):
        return f"""Based on the following user preferences:
        {user_preferences}
        
        Generate a list of suggested activities and attractions that match their interests and budget.
        Include:
        1. Must-visit attractions
        2. Hidden gems
        3. Local experiences
        4. Food recommendations
        5. Transportation options
        
        Format the suggestions in a clear, organized manner."""
    
    def get_itinerary_prompt(self, user_preferences, suggestions):
        return f"""Create a detailed day-by-day itinerary based on:
        User Preferences: {user_preferences}
        Suggested Activities: {suggestions}
        
        The itinerary should include:
        1. Daily schedule with timing
        2. Transportation details
        3. Estimated costs
        4. Restaurant recommendations
        5. Backup options for weather-dependent activities
        
        Format the itinerary in a clear, easy-to-follow structure."""
    
    def process_user_input(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Determine which prompt to use based on conversation stage
        if len(self.conversation_history) == 1:
            system_prompt = self.get_initial_prompt()
        else:
            system_prompt = self.get_refinement_prompt(user_input)
        
        # Format the conversation history
        conversation_text = "\n".join([
            f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
            for msg in self.conversation_history
        ])
        
        # Get AI response using Gemini API
        try:
            response = self.model.generate_content(
                f"{system_prompt}\n\n{conversation_text}"
            )
            
            ai_response = response.text.strip()
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            return ai_response
        except Exception as e:
            error_message = str(e)
            if "API key" in error_message:
                return """I apologize, but there seems to be an issue with the API authentication. 
                Please make sure you have:
                1. Created a Google AI Studio account at https://makersuite.google.com/
                2. Generated an API key at https://makersuite.google.com/app/apikey
                3. Added the key to your .env file as GOOGLE_API_KEY=your_key_here
                
                Would you like me to help you with any of these steps?"""
            else:
                return f"I apologize, but I encountered an error: {error_message}. Please try again."
    
    def generate_itinerary(self, user_preferences, suggestions):
        system_prompt = self.get_itinerary_prompt(user_preferences, suggestions)
        
        try:
            response = self.model.generate_content(system_prompt)
            return response.text.strip()
        except Exception as e:
            error_message = str(e)
            if "API key" in error_message:
                return """I apologize, but there seems to be an issue with the API authentication. 
                Please make sure you have:
                1. Created a Google AI Studio account at https://makersuite.google.com/
                2. Generated an API key at https://makersuite.google.com/app/apikey
                3. Added the key to your .env file as GOOGLE_API_KEY=your_key_here
                
                Would you like me to help you with any of these steps?"""
            else:
                return f"I apologize, but I encountered an error while generating the itinerary: {error_message}. Please try again." 