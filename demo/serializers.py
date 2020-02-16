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
    deleted = fields.Boolean()

class ContactSchema(BaseSchema):
    first_name = fields.Str(validate=validate.Length(min=1))
    last_name = fields.Str(validate=validate.Length(min=1))
    organization = fields.Nested(lambda: OrganizationSchema())
    organization_id = fields.Function(lambda o: o.organization.id)
    name = fields.Function(lambda o: f"{o.first_name} {o.last_name}")

class OrganizationSchema(BaseSchema):
    name = fields.Str()
    contacts = fields.Function(lambda o: 
                                ContactSchema(many=True, exclude=("organization",)).dump(o.contacts.all()))

