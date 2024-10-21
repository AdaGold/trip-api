from flask import abort, make_response
from app.models.trip import Continent
from ..db import db
import enum


class Filter_Type(enum.Enum):
    EQUAL = "EQUAL"
    LESS_OR_EQ = "LESS_OR_EQ"


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"message": f"{cls.__name__} {model_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))
    
    return model


def get_models_with_filters(cls, filters=None, filter_type=None):
    query = db.select(cls)
    
    if filters:
        for attribute, value in filters.items():
            if hasattr(cls, attribute):
                match filter_type:
                    case Filter_Type.LESS_OR_EQ:
                        query = query.where(getattr(cls, attribute) <= value)
                    case _:
                        query = query.where(getattr(cls, attribute) == value)

    models = db.session.scalars(query)
    models_response = [model.to_dict() for model in models]
    return models_response


def validate_continent(continent_param):
    try:
        continent_value = Continent(continent_param)
    except ValueError:  
        not_found_msg = f"Continent {continent_param} not found." 
        continent_options = [continent.value for continent in Continent]
        options_msg = f"Valid options are: {continent_options}."
        response = {"message": f"{not_found_msg} {options_msg}"}
        abort(make_response(response, 400))
    
    return continent_value


def validate_numeric_attr(attribute_param, attribute_name):
    try:
        attribute_value = float(attribute_param)
    except ValueError: 
        attr_capitalize = attribute_name.capitalize() 
        msg = f"{attr_capitalize} query must be a number."
        abort(make_response({"message": msg}, 400))
    
    return attribute_value