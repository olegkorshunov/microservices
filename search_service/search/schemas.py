from marshmallow import Schema, fields


class SUserData(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=False)
    city = fields.String(required=False)
    about = fields.String(required=False)
    date_of_birdth = fields.Date()
