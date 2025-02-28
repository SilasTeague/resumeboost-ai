from flask import Blueprint, request, jsonify
from backend.optimizer import optimize_resume_text

# Create a new Blueprint for resume optimization endpoints
resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/optimize", methods=["POST"])
def optimize():
    """
    Expects JSON with: 
      - 'resume_text'
      - 'job_description' (optional)
    """
    data = request.get_json()
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")

    if not resume_text:
        return jsonify({"error": "Missing 'resume_text' in request."}), 400
    
    try:
        optimized_resume = optimize_resume_text(resume_text, job_description)
        return jsonify({"optimized_resume": optimized_resume}), 200
    except Exception as e:
        #TODO: log error rather than just returning error details
        return jsonify({"error": str(e)}), 500
