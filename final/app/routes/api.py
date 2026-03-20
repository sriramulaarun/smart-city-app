import random
from flask import Blueprint, request, jsonify
from app import db
from app.models import Report
from app.utils.email import send_confirmation_email

bp = Blueprint('api', __name__)

@bp.route("/submit_report", methods=["POST"])
def submit_report():
    data = request.json
    tracking_id = "CH-" + str(random.randint(100000,999999))

    email = data.get("email", "")

    new_report = Report(
        id=tracking_id,
        description=data["description"],
        location=data["location"],
        category=data["category"],
        status="Pending",
        email=email,
        upvotes=0
    )

    db.session.add(new_report)
    db.session.commit()

    if email:
        send_confirmation_email(email, tracking_id)

    return jsonify({"id": tracking_id})

@bp.route("/track_report/<id>")
def track_report(id):
    report = Report.query.get(id)
    if report:
        return jsonify({
            "id": report.id,
            "description": report.description,
            "location": report.location,
            "category": report.category,
            "status": report.status,
            "upvotes": report.upvotes
        })
    else:
        return jsonify({"error": "Not found"}), 404

@bp.route("/all_reports")
def all_reports():
    reports = Report.query.all()
    # Serialize to format expected by frontend
    rows = []
    for r in reports:
        rows.append([r.id, r.description, r.location, r.category, r.status, r.email, r.upvotes])
    return jsonify(rows)

@bp.route("/update_status", methods=["POST"])
def update_status():
    data = request.json
    report = Report.query.get(data["id"])
    if report:
        report.status = data["status"]
        db.session.commit()
        return jsonify({"message": "Updated"})
    return jsonify({"error": "Report not found"}), 404

@bp.route("/upvote_report", methods=["POST"])
def upvote_report():
    data = request.json
    report = Report.query.get(data["id"])
    if report:
        report.upvotes = (report.upvotes or 0) + 1
        db.session.commit()
        return jsonify({"message": "Upvoted", "upvotes": report.upvotes})
    return jsonify({"error": "Report not found"}), 404
