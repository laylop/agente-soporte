import streamlit as st
from openai import OpenAI
from mem0 import Memory
import os
import json
from datetime import datetime, timedelta

# Streamlit App Title & Description
st.title("**Tech Gadgets Support Bot**")
st.caption("Get personalized help with your TechGadgets purchases!")

# OpenAI API Key Input with Password Masking
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

if openai_api_key:
    os.environ['OPENAI_API_KEY'] = openai_api_key

    # Customer Support AI Agent Class
    class CustomerSupportAIAgent:
        def __init__(self):
            config = {
                "vector_store": {
                    "provider": "qdrant",  # You can adjust the provider here
                    "config": {
                        "model": "gpt-4",  # You may want to use the latest OpenAI model
                        "host": "localhost",  # Adjust as needed
                        "port": 6333  # Default Qdrant port
                    }
                }
            }
            self.memory = Memory.from_config(config)  # Initialize memory
            self.client = OpenAI()  # Initialize OpenAI client
            self.app_id = "customer-support"

        def handle_query(self, query, user_id=None):
            # Search relevant memories in the memory store (Qdrant or similar)
            relevant_memories = self.memory.search(
                query=query, user_id=user_id)
            context = "**Past Conversations:**\n"
            if relevant_memories and "results" in relevant_memories:
                for memory in relevant_memories["results"]:
                    if "memory" in memory:
                        context += f"- {memory['memory']}\n"

            # Prepare the prompt for OpenAI's model
            full_prompt = f"{context}\nCustomer: {query}\nSupport Agent:"

            # Get response from OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-4",  # Ensure you are using the correct model here
                messages=[
                    {"role": "system", "content": "Hi! I'm Tech Gadgets' AI assistant. How can I help you today?"},
                    {"role": "user", "content": full_prompt}
                ]
            )
            answer = response.choices[0].message.content

            # Add the conversation to memory (for future context)
            self.memory.add(query, user_id=user_id, metadata={
                            "app_id": self.app_id, "role": "user"})
            self.memory.add(answer, user_id=user_id, metadata={
                            "app_id": self.app_id, "role": "assistant"})

            return answer

        def get_memories(self, user_id=None):
            return self.memory.get_all(user_id=user_id)

        def generate_synthetic_data(self, user_id):
            # Generate synthetic data for testing or demos
            today = datetime.now()
            order_date = (today - timedelta(days=10)).strftime("%B %d, %Y")
            expected_delivery = (today + timedelta(days=2)
                                 ).strftime("%B %d, %Y")

            prompt = f"""Generate a detailed customer profile and order history for a TechGadgets.com customer with ID {user_id}. Include:
            1. Customer name and basic info
            2. A recent order of a high-end electronic device (placed on {order_date}, to be delivered by {expected_delivery})
            3. Order details (product, price, order number)
            4. Customer's shipping address
            5. 2-3 previous orders from the past year
            6. 2-3 customer service interactions related to these orders
            7. Any preferences or patterns in their shopping behavior

            Format the output as a JSON object."""

            # Get response from OpenAI to generate synthetic data
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a data generation AI that creates realistic customer profiles and order histories. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ]
            )

            customer_data = json.loads(response.choices[0].message.content)

            # Add the generated synthetic data to memory
            for key, value in customer_data.items():
                if isinstance(value, list):
                    for item in value:
                        self.memory.add(json.dumps(item), user_id=user_id, metadata={
                                        "app_id": self.app_id})

            return customer_data

    # Initialize the support agent
    agent = CustomerSupportAIAgent()

    # Handle user query input
    user_query = st.text_input("Ask a question:")
    if user_query:
        answer = agent.handle_query(user_query)
        st.write(answer)
