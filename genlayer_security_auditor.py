import openai
import json
import os

class GenLayerSecurityAuditor:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def analyze_contract(self, solidity_code):
        # این پرامپتِ تخصصی برای تحلیل امنیتیه
        system_prompt = """
        You are a smart contract security expert. Analyze the provided Solidity code for:
        1. Honeypot patterns (restricted transfer functions).
        2. Ownership exploits.
        3. Reentrancy and common vulnerabilities.
        Return ONLY a JSON object: {"is_safe": bool, "risk_score": int, "summary": str}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": solidity_code}
            ]
        )
        return json.loads(response.choices[0].message.content)

# نحوه استفاده:
# auditor = GenLayerSecurityAuditor(api_key="YOUR_OPENAI_KEY")
# result = auditor.analyze_contract("کد سالیدیتی رو اینجا بده")
# print(result)
