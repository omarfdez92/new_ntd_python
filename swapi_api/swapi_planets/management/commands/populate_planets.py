import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from django.core.management.base import BaseCommand
from swapi_planets.models import Planet

def fetch_planet_data():
    transport = RequestsHTTPTransport(url="https://swapi-graphql.netlify.app/.netlify/functions/index")
    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql("""
    query Query {
        allPlanets {
            planets {
                name
                population
                terrains
                climates
            }
        }
    }
    """)

    result = client.execute(query)
    return result['allPlanets']['planets']

class Command(BaseCommand):
    help = 'Populate the database with Planet data from the SWAPI GraphQL API'

    def handle(self, *args, **options):
        planet_data = fetch_planet_data()
        for planet in planet_data:
            Planet.objects.create(
                name=planet['name'],
                population=planet['population'],
                terrains=planet['terrains'],
                climates=planet['climates'],
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated database with planet data'))

