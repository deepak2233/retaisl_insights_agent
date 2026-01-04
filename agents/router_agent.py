"""
Router Agent for query classification
Categories: analytics, greeting, out_of_scope, appreciation
"""
from typing import Dict, Any, List
import re
from utils.llm_utils import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

class IntentClassification(BaseModel):
    intent: str = Field(description="One of: analytics, greeting, out_of_scope, appreciation")
    reasoning: str = Field(description="Brief reason for classification")
    response_if_not_analytics: str = Field(description="Polite response if not analytics, otherwise empty")

class RouterAgent:
    def __init__(self):
        self.llm = get_llm(temperature=0)
        self.parser = JsonOutputParser(pydantic_object=IntentClassification)
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a specialized router and conversational guardrail for a Retail Insights Assistant.
Classify the user's input into one of these categories:
1. analytics: Questions about sales, revenue, products, orders, or customers. This includes requests for SQL queries or data synthesis from reports.
2. greeting: Simple hellos, greetings, or "how are you".
3. appreciation: "thanks", "great job", "you are helpful", etc.
4. out_of_scope: Questions about topics not related to retail (e.g., weather, recipes, personal advice, news).

Information about available context:
- Database: Structured sales data is available.
- Report Context: {report_info}

Instructions for Non-Analytics responses:
- For greetings: Respond with a warm, professional welcome. Briefly mention your expertise in retail data analysis.
- For appreciation: Respond with humble professionalism and offer further assistance with data insights.
- For out_of_scope: DO NOT simply say "I can't help". Instead, acknowledge the user's input/interest politely, then explain that your primary purpose is to provide deep retail business insights. Offer a relevant bridge back to retail (e.g., "While I don't follow the weather, I can tell you how seasonal patterns usually affect retail sales based on your data!").

Return ONLY a JSON object."""),
            ("user", "{input}")
        ])
        
        self.chain = self.prompt | self.llm | self.parser

    def classify(self, question: str, report_content: str = None) -> Dict[str, Any]:
        """Classify user intent using LLM"""
        try:
            # Fast check
            q_lower = question.lower().strip()
            # ... (keep regex checks)
            if q_lower in ["hi", "hello", "hey", "hola"]:
                return {
                    "intent": "greeting",
                    "reasoning": "Simple greeting detected via regex",
                    "response_if_not_analytics": "Hello! I'm your Retail Insights Assistant. How can I help you analyze your data today?"
                }
            if q_lower in ["thanks", "thank you", "great", "awesome", "good"]:
                return {
                    "intent": "appreciation",
                    "reasoning": "Simple appreciation detected via regex",
                    "response_if_not_analytics": "You're very welcome! I'm here to help you get the most out of your retail data. Is there anything else you'd like to analyze?"
                }

            report_info = "An additional summarized report is available as context." if report_content else "No additional reports are currently loaded."
            
            result = self.chain.invoke({
                "input": question,
                "report_info": report_info
            })
            return result
        except Exception as e:
            # Fallback to analytics if LLM fails
            return {
                "intent": "analytics",
                "reasoning": f"Classification error: {str(e)}",
                "response_if_not_analytics": ""
            }
