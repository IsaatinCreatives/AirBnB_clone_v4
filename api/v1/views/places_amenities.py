#!/usr/bin/python3
"""
Place amenity.
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.amenity import Amenity
from models.place import Place


@app_views.route('/places/<place_id>/amenities', methods=['GET'])
def all_place_amenities(place_id):
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)

    return jsonify(place.amenities.to_dict())

@app_views.route('/places/<p_id>/amenities/<a_id>', methods=['DELETE'])
def delete_place_amenity(p_id, a_id):
    """deletes the amenity based on place"""
    place = storage.get("Place", p_id)
    if place is None:
        abort(404)
    for amenity in place.amenities:
        if amenity.id == a_id:
            storage.delete(amenity)
            storage.save()
            return jsonify({}), 200
    abort(404)


@app_views.route('places/<p>/amenities/<a>', methods=['POST'])
def post_place_amenity(p, a):
    """Creates a new amenity for a place"""
    place = storage.get("Place", p)
    if place is None:
        abort(404)
    for amenity in place.amenities:
        if amenity.id == a:
            return jsonify(amenity.to_dict()), 200

    amenity = Amenity(**request.json)
    amenity.place_id = p
    amenity.save()
    return jsonify(amenity.to_dict()), 201
