from marshmallow import Schema, fields

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
    first_name = fields.Str()
    last_name = fields.Str()
    organization = fields.Nested(OrganizationSchema)
    organization_id = fields.Function(lambda o: o.organization.id)
