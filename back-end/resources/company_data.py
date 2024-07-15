from flask_restful import Resource, reqparse
from models import Company_data


company_data_parser = reqparse.RequestParser()
company_data_parser.add_argument('name', type=str, required=True, help='Name is required')
company_data_parser.add_argument('title', type=str, required=True, help='Title is required')
company_data_parser.add_argument('description', type=str, required=True, help='Description is required')
company_data_parser.add_argument('image_url', type=str, required=True, help='Image URL is required')

class Company_dataResource(Resource):
    def get(self):
        company_data = Company_data.query.all()
        return [company_data.to_dict() for company_data in company_data], 200

    def post(self):
        data = request.get_json()
        company_data = Company_data(
            name=data['name'],
            title=data['title'],
            description=data['description'],
            image=data['image']
        )
        db.session.add(company_data)
        db.session.commit()
        return company_data.to_dict(), 201