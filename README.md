# GenLayer AI Auditor

A decentralized security auditing tool built for the GenLayer ecosystem. 
This project leverages LLMs to provide real-time security analysis for Intelligent Contracts, 
helping to prevent honeypots and rug-pulls before deployment.

## Features
- AI-driven vulnerability detection (Reentrancy, Honeypots, Ownership risks).
- Structured JSON output for on-chain integration.
- Designed to integrate with GenLayer's "Optimistic Democracy" consensus.

## How it works
The analyzer utilizes OpenAI's API to perform deep code analysis on Solidity smart contracts, 
outputting standardized risk scores that can be used by validators to reach consensus on contract safety.

"The security analysis logic is powered by GPT-4o-mini with enforced JSON-mode for on-chain integration."
