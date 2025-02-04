from marshmallow import Schema, fields, validate

class PlainParagrafosValidadosSchema(Schema):
    id = fields.Str(dump_only=True)
    paragrafo = fields.Str(required=True, validate=validate.Length(min=1))
    


class PlainContratosSchema(Schema):
    id = fields.Str(dump_only=True)
    contrato_uid = fields.Str(required=True, validate=validate.Length(min=1))


class UpdateContratosSchema(Schema):
    id = fields.Str(dump_only=True)
    contrato_uid = fields.Str(required=True, validate=validate.Length(min=1))
    paragrafos_validados = fields.Nested(PlainParagrafosValidadosSchema, many=True, required=True)
    
class UpdateParagrafosValidadosSchema(Schema):
    paragrafo = fields.Str(required=True, validate=validate.Length(min=1))
  
  
  
class ContratosSchema(Schema):
    id = fields.Str(dump_only=True)
    contrato_uid = fields.Str(required=True, validate=validate.Length(min=1))
    name = fields.Str(required=True, validate=validate.Length(min=1))
