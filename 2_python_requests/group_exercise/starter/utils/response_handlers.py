"""Utility functions for handle request responses."""
import json


def handle_response(res):
    if 200 <= res.status_code <= 299:
        return json.dumps(
            {
                "status_code": res.status_code,
                "data": res.json()
            }
        )
    else:
        return json.dumps(
            {
                "status_code": res.status_code,
                "message": res.content
            }
        )
