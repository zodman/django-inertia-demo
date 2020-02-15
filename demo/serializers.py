from marshmallow import Schema, fields, validate



class BaseSchema(Schema):
    id = fields.Int()
    email = fields.Email()
    phone = fields.Str()
    address = fields.Str()
    city = fields.Str()
    region = fields.Str()
    postal_code = fields.Str()    
    country = fields.Str() 

class OrganizationSchema(BaseSchema):
    name = fields.Str()

class ContactSchema(BaseSchema):
    first_name = fields.Str(validate=validate.Length(min=1))
    last_name = fields.Str(validate=validate.Length(min=1))
    organization = fields.Nested(OrganizationSchema)
    organization_id = fields.Function(lambda o: o.organization.id)
