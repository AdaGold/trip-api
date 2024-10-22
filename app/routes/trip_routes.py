from flask import Blueprint, request, make_response, abort
from sqlalchemy.exc import IntegrityError
from .route_utilities import Filter_Type, validate_model, get_models_with_filters, validate_continent, validate_numeric_attr
from app.models.trip import Trip
from app.models.reservation import Reservation
from ..db import db

bp = Blueprint("trips_bp", __name__, url_prefix="/trips")


@bp.get("")
def get_all_trips():
    return get_models_with_filters(Trip)


@bp.get("/continent")
def get_trips_by_continent():
    continent_param = request.args.get("query")
    continent_value = validate_continent(continent_param)
    filter_dict = {"continent": continent_value}
    return get_models_with_filters(Trip, filter_dict)


@bp.get("/weeks")
def get_trips_by_weeks():
    return get_trips_by_numeric_attribute(request.args, "weeks")


@bp.get("/budget")
def get_trips_by_budget():
    return get_trips_by_numeric_attribute(request.args, "cost")


def get_trips_by_numeric_attribute(request_dict, attribute_name):
    attribute_param = request_dict.get("query")
    attribute_value = validate_numeric_attr(attribute_param, attribute_name)
    filter_dict = {attribute_name: attribute_value}
    return get_models_with_filters(Trip, filter_dict, Filter_Type.LESS_OR_EQ)


@bp.get("/<trip_id>")
def get_trip_by_id(trip_id):
    trip = validate_model(Trip, trip_id)
    return trip.to_dict()


@bp.post("")
def create_trip():
    trip_data = request.json

    if not trip_data.get("name"):
        response = {"message": "Missing name field"}
        abort(make_response(response, 400))

    try:
        cost = validate_numeric_attr(trip_data["cost"], "cost")  
        weeks = validate_numeric_attr(trip_data["weeks"], "weeks")
        continent_value = validate_continent(trip_data["continent"])
    except KeyError as e:
        response = {"message": f"Missing {e} field"}
        abort(make_response(response, 400))

    trip_data["cost"] = cost
    trip_data["weeks"] = weeks
    trip_data["continent"] = continent_value

    try:
        new_trip = Trip.from_dict(trip_data)
    except KeyError as e:
        response = {"message": f"Missing {e} field"}
        abort(make_response(response, 400))
    
    db.session.add(new_trip)

    try:
        db.session.commit()
    except IntegrityError as e:
        response = {"message": "Trip name must be unique"}
        abort(make_response(response, 400))

    return new_trip.to_dict(), 201


@bp.post("/<trip_id>/reservations")
def create_reservation(trip_id):
    trip = validate_model(Trip, trip_id)
    reservation_data = request.json
    reservation_data["trip_id"] = trip.id

    try:
        new_reservation = Reservation.from_dict(reservation_data)
    except KeyError as e:
        response = {"message": f"Missing {e} field"}
        abort(make_response(response, 400))
    
    db.session.add(new_reservation)
    db.session.commit()
    return new_reservation.to_dict(), 201


@bp.get("/<trip_id>/reservations")
def get_reservations_by_trip(trip_id):
    trip = validate_model(Trip, trip_id)
    reservations = trip.reservations
    reservations_response = [booking.to_dict() for booking in reservations]
    return reservations_response
