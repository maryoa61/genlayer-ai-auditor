import openai
import json
import os

class GenLayerSecurityAuditor:
    def __init__(self, api_key=None):
        # اگر API Key در تنظیمات سیستم نباشد، از کلید ورودی استفاده می‌کند
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is missing. Please set OPENAI_API_KEY environment variable.")
        self.client = openai.OpenAI(api_key=self.api_key)

    def analyze_contract(self, solidity_code):
        """
        تحلیل امنیتی کد سالیدیتی و بازگرداندن نتیجه به صورت JSON
        """
        system_prompt = """
        You are a smart contract security expert specializing in GenLayer and BSC.
        Analyze the provided Solidity code for:
        1. Honeypot traps (restricted transfer functions, hidden taxes).
        2. Ownership exploits (unauthorized minting/pausing).
        3. Common vulnerabilities (Reentrancy, etc).
        
        Return ONLY a JSON object: 
        {"is_safe": bool, "risk_score": int, "critical_vulnerabilities": list, "summary": str, "action_recommendation": str}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": solidity_code}
                ],
                response_format={ "type": "json_object" }
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            return {"error": str(e)}

# نحوه تست در سیستم خودتان:
if __name__ == "__main__":
    # در محیط واقعی، کلید را در متغیر محیطی ست کنید
    # os.environ["OPENAI_API_KEY"] = "sk-..." 
    
    auditor = GenLayerSecurityAuditor()
    sample_code = "contract Test { ... }"
    result = auditor.analyze_contract(sample_code)
    print(json.dumps(result, indent=4))
