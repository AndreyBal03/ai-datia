// Learn more about clients at https://docs.boundaryml.com/docs/snippets/clients/overview

// Using the new OpenAI Responses API for enhanced formatting
client<llm> CustomGPT5 {
  provider "openai-generic"
  options {
    base_url "https://openrouter.ai/api/v1"
    api_key env.OPENROUTER_API_KEY
    model "openai/gpt-5"
  }
}

client<llm> CustomGPT5Mini {
  provider "openai-generic"
  options {
    base_url "https://openrouter.ai/api/v1"
    api_key env.OPENROUTER_API_KEY
    model "openai/gpt-5-mini"
  }
}

client<llm> CustomGemini {
  provider "google-ai"
  options {
    model "gemini-2.5-flash"
    api_key env.GEMINI_API_KEY
  }
}
