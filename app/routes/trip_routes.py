from flask import Blueprint, request, jsonify, make_response
from app.models.trip import Trip
from app.models.reservation import Reservation
from ..db import db

bp = Blueprint("trips_bp", __name__, url_prefix="/trips")