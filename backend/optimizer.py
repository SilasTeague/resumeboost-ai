from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=f"{os.getenv("OPENAI_API_KEY")}"
)

def optimize_resume_text(resume_text, job_description=None):
    prompt = f"Optimize the following resume by adding relevant keywords:\n\nResume:\n{resume_text}\n"
    if job_description:
        prompt += f"\nOptimize the resume based on the following job description, such that the resume more closely reflects what the employer is looking for in a candidate:\n\n{job_description}"
    prompt += f"\nReturn the optimized resume with suggested changes highlighted (e.g., using **bold** formatting). Respond with only the optimzed resume text. Do not respond in more sentences than the input, only replace key words or phrases used in the input resume in an optimized way."
    completion = client.chat.completions.create(model="gpt-4o-mini", store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    optimized_resume = completion.choices[0].message.content
    return optimized_resume

