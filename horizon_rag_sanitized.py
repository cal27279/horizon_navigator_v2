import os
import sys
import boto3
from dotenv import load_dotenv

# Load environment variables from the .env file to maintain security
load_dotenv()

# --- PROJECT CONFIGURATION ---
# Secrets are managed via environment variables to prevent hardcoding in the repository.
KNOWLEDGE_BASE_ID = os.getenv("KNOWLEDGE_BASE_ID")
MODEL_ID = os.getenv("MODEL_ID") # IMPORTANT: We use the Inference Profile ID for the region
REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

class HorizonRAG:
    """
    Core engine for Horizon Navigator v2.
    Tuned to comply with AWS Bedrock throughput requirements.
    """
    def __init__(self):
        # Validate critical environment variables before initializing the client
        if not KNOWLEDGE_BASE_ID or not MODEL_ID:
            raise ValueError("Critical configuration missing. Please verify your .env file.")

        self.client = boto3.client('bedrock-agent-runtime', region_name=REGION)
        self.kb_id = KNOWLEDGE_BASE_ID
        self.model_arn = MODEL_ID # Changed from ARN to Profile ID as required
        self.region_name = REGION 

    def query(self, user_query: str):
        if not user_query.strip():
            return "Please provide a valid risk query."

        try:
            response = self.client.retrieve_and_generate(
                input={'text': user_query},
                retrieveAndGenerateConfiguration={
                    'type': 'KNOWLEDGE_BASE',
                    'knowledgeBaseConfiguration': {
                        'knowledgeBaseId': self.kb_id,
                        'modelArn': self.model_arn,
                        'retrievalConfiguration': {
                            'vectorSearchConfiguration': {
                                'numberOfResults': 25,
                                'overrideSearchType': 'SEMANTIC' 
                            }
                        }
                    }
                }
            )
            return response['output']['text']
        except Exception as e:
            # Print the error to the console for debugging purposes
            print(f"DEBUG AWS ERROR: {str(e)}")
            return f"⚠️ System Error: {str(e)}"

# --- TERMINAL MODE (CLI) ---
def run_terminal():
    try:
        advisor = HorizonRAG()
    except ValueError as e:
        print(f"\nInitialization Error: {e}")
        sys.exit(1)

    print("\n" + "="*60)
    print(" 🛰️  HORIZON NAVIGATOR V2 - AI RISK ADVISOR (CLI)")
    print("="*60)
    
    while True:
        prompt = input("\n[Project Manager] > ")
        if prompt.lower() in ['exit', 'quit', 'q']:
            print("\nSession closed. System shutting down securely.")
            break
        answer = advisor.query(prompt)
        print(f"\n[AI Analysis] > {answer}")

if __name__ == "__main__":
    run_terminal()
